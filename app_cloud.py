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
import numpy as np

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
    "last_signal": "NONE",
    "confidence": 0.0,
    "trades_today": 0,
    "max_trades": 5,
    "last_trade_time": None,
    "logs": []
}

def update_dashboard(signal, confidence):
    BOT_STATE["last_signal"] = signal
    BOT_STATE["confidence"] = confidence
    BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
    if BOT_STATE["initial_balance"] > 0:
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
    
    if BOT_STATE["drawdown"] > 0.10:
        BOT_STATE["status"] = "STOPPED (KILL SWITCH)"
        logger.warning("🚨 KILL SWITCH ACTIVATED")

    BOT_STATE["logs"].append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "signal": signal,
        "confidence": confidence
    })
    if len(BOT_STATE["logs"]) > 50:
        BOT_STATE["logs"] = BOT_STATE["logs"][-50:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, YnorScoringEngine
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallback minimal
    class YnorScoringEngine:
        def compute_score(self, p, s): return 80
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class YnorNewsScraper:
        def __init__(self, *a): pass
        def update_report(self): pass
    class YnorEconomicSentinel:
        def __init__(self, *a, **k): pass
        def get_geo_alpha(self, s): return 0.8

DRY_RUN = True
MAX_TRADES_PER_DAY = 10
COOLDOWN_SECONDS = 300
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

async def fetch_history(ticker="BTC-USD", interval="5m", period="1d"):
    try:
        data = yf.Ticker(ticker).history(period=period, interval=interval)
        return data['Close'].tolist()
    except: return []

@asynccontextmanager
async def lifespan(app: FastAPI):
    scraper = YnorNewsScraper(REPORT_PATH)
    connector = YnorBitgetConnector()
    
    # Init Balance
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
        global last_trade_time
        l_trade_t = 0
        
        while True:
            try:
                if "STOPPED" in BOT_STATE["status"]:
                    await asyncio.sleep(300); continue

                # DATA
                prices = await fetch_history()
                sentiment = sentinel.get_geo_alpha("BTC")
                balance = connector.get_balance()
                if balance: BOT_STATE["balance"] = balance

                # DECISION
                score = engine.compute_score(prices, sentiment)
                BOT_STATE["confidence"] = score / 100.0
                
                # SIGNAL SELECTION
                signal = "HOLD"
                if score > 75: signal = "BUY"
                elif score < 25: signal = "SELL"
                
                # SAFETY FILTERS
                if BOT_STATE["trades_today"] >= BOT_STATE["max_trades"]:
                    signal = "HOLD"
                if time.time() - l_trade_t < COOLDOWN_SECONDS:
                    signal = "HOLD"

                update_dashboard(signal if signal != "HOLD" else "HUNTING", score / 100.0)

                if signal != "HOLD":
                    if DRY_RUN:
                        logger.info(f"🧪 [DRY RUN] Signal: {signal} | Score: {score}")
                    else:
                        size = balance * 0.01 / prices[-1] if prices else 0.001
                        res = connector.place_order(side=signal.lower(), size=size)
                        if res.get("code") == "00000":
                            l_trade_t = time.time()
                            BOT_STATE["trades_today"] += 1
                            BOT_STATE["last_trade_time"] = datetime.now().strftime("%H:%M:%S")

            except Exception as e:
                logger.error(f"Loop Error: {e}")
            
            await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "ynor live", "dry_run": DRY_RUN}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    # ... Dashboard HTML (Identique au précédent mais avec score V3) ...
    log_html = "".join([f"<p style='margin:5px 0; font-family:monospace; color:#94a3b8;'>[{log['time']}] {log['signal']} (Score: {log['confidence']:.2f})</p>" for log in BOT_STATE["logs"][-10:]])
    html = f"<html><head><title>YNOR V3</title><meta http-equiv='refresh' content='5'></head><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH V3 | LIVE MONITOR</h1><div style='background:#0f172a; padding:20px; border-radius:10px;'><h2>Status: {BOT_STATE['status']}</h2><p>Balance: ${BOT_STATE['balance']:,.2f}</p><p>PnL: {BOT_STATE['pnl']:+.2f}$</p><p>Score Actuel: <span style='color:#38bdf8; font-weight:bold;'>{BOT_STATE['confidence']:.4f}</span></p><p>Signal: {BOT_STATE['last_signal']}</p></div><div style='margin-top:20px; background:#000; padding:15px;'>{log_html}</div></body></html>"
    return html
