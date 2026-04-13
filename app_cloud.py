import asyncio
import sys
import os
import time
import logging
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from datetime import datetime
import yfinance as yf

# --- FIX PYTHON PATH ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- CONFIG LOGGING ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("YNOR_SYSTEM")

# --- GLOBAL BOT STATE (DASHBOARD) ---
BOT_STATE = {
    "status": "RUNNING",
    "balance": 1000.0,
    "initial_balance": 1000.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "positions": {"BTC": "HOLD", "ETH": "HOLD", "SOL": "HOLD"},
    "confidence": {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0},
    "trades_today": 0,
    "last_trade_time": None,
    "logs": []
}

def update_dashboard(symbol, signal, confidence):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["confidence"][pair] = confidence
    
    # Safe calc
    if BOT_STATE["balance"] is not None and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if BOT_STATE["drawdown"] > 0.10: BOT_STATE["status"] = "STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{pair}: {signal} (Score: {confidence:.2f})"})
    if len(BOT_STATE["logs"]) > 50: BOT_STATE["logs"] = BOT_STATE["logs"][-50:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallback placeholders
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class MillenniumGrandSolver:
        def __init__(self, *a): pass
        def compute_indicators(self, df): return df
        def compute_score(self, d): return 50
        def decide(self, s): return "HOLD"
        def compute_position_size(self, b, s, p): return 0.001

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
DRY_RUN = True
COOLDOWN_SECONDS = 300
MAX_TRADES_PER_DAY = 10
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance is not None:
        BOT_STATE["balance"] = balance
        BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"])
    sentinel = YnorEconomicSentinel("", REPORT_PATH)
    scraper = YnorNewsScraper(REPORT_PATH)

    async def news_worker():
        while True:
            try: scraper.update_report(); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        last_t_time = 0
        while True:
            try:
                if "STOPPED" in BOT_STATE["status"]: await asyncio.sleep(300); continue
                
                balance = connector.get_balance()
                if balance is not None:
                    BOT_STATE["balance"] = balance
                    if BOT_STATE["initial_balance"] <= 0: BOT_STATE["initial_balance"] = balance
                
                sentiment = sentinel.get_geo_alpha("BTC")

                for symbol in SYMBOLS:
                    # 1. Fetch
                    df = yf.Ticker(symbol).history(period="1d", interval="5m")
                    if df.empty or len(df) < 20: continue
                    
                    # 2. Indicators
                    df = solver.compute_indicators(df)
                    row = df.iloc[-1]
                    
                    data_point = {
                        "price": row["Close"],
                        "ema": row["ema"],
                        "rsi": row["rsi"],
                        "volatility": row["volatility"],
                        "sentiment": sentiment
                    }
                    
                    # 3. Score & Decide
                    score = solver.compute_score(data_point)
                    signal = solver.decide(score)
                    
                    # 4. Filters
                    if score < 65: signal = "HOLD" # Anti-overtrading filter
                    if BOT_STATE["trades_today"] >= MAX_TRADES_PER_DAY: signal = "HOLD"
                    if time.time() - last_t_time < COOLDOWN_SECONDS: signal = "HOLD"

                    update_dashboard(symbol, signal if signal != "HOLD" else "HUNTING", score / 100.0)

                    if signal != "HOLD":
                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {signal} | Score: {score}")
                        else:
                            size = solver.compute_position_size(BOT_STATE["balance"], score, row["Close"])
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=signal.lower(), size=size)
                            if res.get("code") == "00000":
                                last_t_time = time.time()
                                BOT_STATE["trades_today"] += 1
                                logger.info(f"✅ Executed: {symbol}")

                await asyncio.sleep(300)
            except Exception as e:
                logger.error(f"Loop Error: {e}")
                await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    pos_html = "".join([f"<p>{k}: <span style='color:#38bdf8'>{v}</span> ({BOT_STATE['confidence'][k]:.2f})</p>" for k,v in BOT_STATE["positions"].items()])
    log_html = "".join([f"<p style='font-size:12px; color:#94a3b8;'>[{log['time']}] {log['msg']}</p>" for log in BOT_STATE["logs"][-12:]])
    html = f"<html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR QUANT CORE V3</h1><div style='background:#0f172a; padding:20px; border-radius:10px;'><h2>Solde: ${BOT_STATE['balance']:,.2f}</h2><p>PnL: {BOT_STATE['pnl']:+.2f}$ ({BOT_STATE['drawdown']*100:.2f}%)</p>{pos_html}</div><div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div></body></html>"
    return html
