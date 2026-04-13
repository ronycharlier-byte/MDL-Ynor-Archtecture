import asyncio
import sys
import os
import time
import logging
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from datetime import datetime
import json
import yfinance as yf

# --- FIX PYTHON PATH ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- CONFIG LOGGING ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("YNOR_SYSTEM")

# --- GLOBAL BOT STATE (DASHBOARD) ---
BOT_STATE = {
    "status": "RUNNING",
    "balance": 0.0,
    "initial_balance": 1.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "positions": {"BTC": "HOLD", "ETH": "HOLD", "SOL": "HOLD"},
    "confidence": {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0},
    "trades_today": 0,
    "max_trades": 10,
    "last_trade_time": None,
    "logs": []
}

def update_dashboard(symbol, signal, confidence):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["confidence"][pair] = confidence
    BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
    if BOT_STATE["initial_balance"] > 0:
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
    
    if BOT_STATE["drawdown"] > 0.10: BOT_STATE["status"] = "STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "msg": f"{pair}: {signal} (Score: {confidence:.2f})"
    })
    if len(BOT_STATE["logs"]) > 50: BOT_STATE["logs"] = BOT_STATE["logs"][-50:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, YnorScoringEngine
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    class YnorScoringEngine:
        def compute_score(self, p, s): return 80
        def compute_position_size(self, b, s, p): return 0.001
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class YnorNewsScraper:
        def __init__(self, *a): pass
        def update_report(self): pass
    class YnorEconomicSentinel:
        def __init__(self, *a, **k): pass
        def get_geo_alpha(self, s): return 0.8

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
DRY_RUN = True
COOLDOWN_SECONDS = 300
MAX_TOTAL_EXPOSURE = 0.05
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

async def fetch_history(ticker):
    try: return yf.Ticker(ticker).history(period="1d", interval="5m")['Close'].tolist()
    except: return []

@asynccontextmanager
async def lifespan(app: FastAPI):
    scraper = YnorNewsScraper(REPORT_PATH)
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance:
        BOT_STATE["balance"] = balance
        BOT_STATE["initial_balance"] = balance
    
    engine = YnorScoringEngine()
    sentinel = YnorEconomicSentinel("", REPORT_PATH)

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
                if balance: BOT_STATE["balance"] = balance
                sentiment = sentinel.get_geo_alpha("BTC")

                for symbol in SYMBOLS:
                    prices = await fetch_history(symbol)
                    if not prices: continue
                    
                    score = engine.compute_score(prices, sentiment)
                    signal = "HOLD"
                    if score > 75: signal = "BUY"
                    elif score < 25: signal = "SELL"
                    
                    # RISK: Total Exposure check Placeholder
                    # (In a real scenario we'd check active positions on exchange)
                    
                    update_dashboard(symbol, signal if signal != "HOLD" else "HUNTING", score / 100.0)

                    if signal != "HOLD" and time.time() - last_t_time > COOLDOWN_SECONDS:
                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {signal} | Score: {score}")
                        else:
                            size = engine.compute_position_size(balance, score, prices[-1])
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=signal.lower(), size=size)
                            if res.get("code") == "00000":
                                last_t_time = time.time()
                                BOT_STATE["trades_today"] += 1

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
    log_html = "".join([f"<p style='color:#94a3b8;'>{log['time']} | {log['msg']}</p>" for log in BOT_STATE["logs"][-10:]])
    html = f"<html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | MULTI-ASSET ADAPTATIVE</h1><div style='background:#0f172a; padding:20px; border-radius:10px;'><h2>Portfolio Status</h2>{pos_html}<p>Balance: ${BOT_STATE['balance']:,.2f}</p></div><div style='margin-top:20px; background:#000; padding:15px;'>{log_html}</div></body></html>"
    return html
