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
    "last_signal": "NONE",
    "confidence": 0.0,
    "trades_today": 0,
    "logs": []
}

def update_dashboard(signal, confidence):
    BOT_STATE["last_signal"] = signal
    BOT_STATE["confidence"] = confidence
    if BOT_STATE["balance"] and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if BOT_STATE["drawdown"] > 0.10: BOT_STATE["status"] = "STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{signal} (Score: {confidence:.2f})" })
    if len(BOT_STATE["logs"]) > 20: BOT_STATE["logs"] = BOT_STATE["logs"][-20:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver, YnorMarketRegime
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallback minimal 
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class MillenniumGrandSolver:
        def __init__(self, initial_balance=1000): pass
        def compute_indicators(self, df): return df
        def compute_score(self, s, t, v): return 50
        def decide(self, s): return "HOLD"
        def compute_position_size(self, *a): return 0.001
    class YnorMarketRegime:
        def detect(self, df): return "range"

DRY_RUN = True
MAX_TRADES_PER_DAY = 10
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    connector = YnorBitgetConnector()
    # Safe balance sync
    balance = connector.get_balance()
    if balance is not None:
        BOT_STATE["balance"] = balance; BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"])
    regime_engine = YnorMarketRegime() if 'YnorMarketRegime' in globals() else None
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
                
                # Update balance
                bal = connector.get_balance()
                if bal: BOT_STATE["balance"] = bal

                # Fetch market data (BTC primary)
                df = yf.Ticker("BTC-USD").history(period="1d", interval="5m")
                if df.empty or len(df) < 50: await asyncio.sleep(60); continue
                
                df = solver.compute_indicators(df)
                sentiment = sentinel.get_geo_alpha("BTC")
                
                # Adaptive Trend Detection
                row = df.iloc[-1]
                trend = "range"
                if row["Close"] > row["ema"]: trend = "bullish"
                elif row["Close"] < row["ema"]: trend = "bearish"
                
                volatility = row.get("volatility", 0.01)

                # Solve & Decide
                score = solver.compute_score(sentiment, trend, volatility)
                signal = solver.decide(score)
                
                # Limits
                if BOT_STATE["trades_today"] >= MAX_TRADES_PER_DAY: signal = "HOLD"
                if time.time() - last_t_time < 300: signal = "HOLD"

                update_dashboard(signal if signal != "HOLD" else "HUNTING", score / 100.0)

                if signal != "HOLD":
                    if DRY_RUN:
                        logger.info(f"🧪 [DRY] Signal: {signal} | Score: {score}")
                    else:
                        size = solver.compute_position_size(BOT_STATE["balance"], score, row["Close"])
                        res = connector.place_order(symbol="BTCUSDT", side=signal.lower(), size=size)
                        if res.get("code") == "00000":
                            last_t_time = time.time(); BOT_STATE["trades_today"] += 1

            except Exception as e:
                logger.error(f"Loop Error: {e}")
            
            await asyncio.sleep(300) # Deep scan every 5 min

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root(): return {"status": "ynor live", "version": "18.3.0"}

@app.get("/health")
def health(): return {"status": "healthy"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    log_html = "".join([f"<p style='color:#94a3b8;'>[{l['time']}] {l['msg']}</p>" for l in BOT_STATE["logs"][-10:]])
    html = f"<html><body style='background:#111; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | STABLE CORE</h1><div style='background:#222; padding:20px; border-radius:10px;'><h2>Balance: ${BOT_STATE['balance']:,.2f}</h2><p>PnL: {BOT_STATE['pnl']:+.2f}$</p><p>Signal: {BOT_STATE['last_signal']}</p></div><div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div></body></html>"
    return html
