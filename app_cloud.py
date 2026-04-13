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

# --- GLOBAL BOT STATE ---
BOT_STATE = {
    "status": "BOOTING",
    "regime": "UNKNOWN",
    "balance": 0.0,
    "initial_balance": 0.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "positions": {"BTC": "HUNTING", "ETH": "HUNTING", "SOL": "HUNTING"},
    "allocation": {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0},
    "trades_today": 0,
    "live_mode": False,
    "paused": False,
    "kill_switch": False,
    "logs": []
}

# --- LIVE SAFETY PROTOCOLS ---
DRY_RUN = True
ENABLE_LIVE_TRADING = False
MAX_TRADE_SIZE_USD = 10.0
MAX_DAILY_TRADES = 5
KILL_SWITCH_THRESHOLD = 0.10

# --- SECURE BOOTSTRAP ---
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver, YnorMarketRegime
    BOOT_SUCCESS = True
except Exception as e:
    logger.critical(f"🔥 CRITICAL IMPORT ERROR: {e}")
    BOOT_SUCCESS = False
    # Fallbacks 
    class YnorMarketRegime:
        def detect(self, *a): return "UNKNOWN"
    class YnorBitgetConnector:
        def get_balance(self): return None
        def place_order(self, **k): return {"code": "error"}
    class MillenniumGrandSolver:
        def __init__(self, *a): pass
    class YnorEconomicSentinel:
        def __init__(self, *a): pass
        def get_geo_alpha(self, a): return 0.5
    class YnorNewsScraper:
        def __init__(self, *a): pass
        def update_report(self): pass

def normalize_sentiment(val):
    return max(-1.0, min(1.0, (val - 0.5) * 2))

def check_kill_switch():
    if BOT_STATE["kill_switch"]: return True
    if BOT_STATE["initial_balance"] > 0:
        drawdown = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if drawdown > KILL_SWITCH_THRESHOLD: return True
    return False

def update_dashboard(symbol, signal, allocation, regime):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["allocation"][pair] = allocation
    BOT_STATE["regime"] = regime
    if BOT_STATE["balance"] and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{pair}: {signal} | ({regime})" })
    if len(BOT_STATE["logs"]) > 20: BOT_STATE["logs"] = BOT_STATE["logs"][-20:]

REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance:
        BOT_STATE["balance"] = balance; BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"] or 1000)
    regime_engine = YnorMarketRegime()
    sentinel = YnorEconomicSentinel("", REPORT_PATH)
    scraper = YnorNewsScraper(REPORT_PATH)
    BOT_STATE["status"] = "RUNNING"

    async def news_worker():
        while True:
            try: scraper.update_report(); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        while True:
            try:
                # Detection du régime MARCHÉ (Source de Vérité)
                regime = regime_engine.detect("BTC-USD")
                BOT_STATE["regime"] = regime
                
                if check_kill_switch():
                    BOT_STATE["status"] = "🚨 STOPPED (KILL SWITCH)"
                    return 

                if BOT_STATE.get("paused"):
                    await asyncio.sleep(60); continue
                
                # ... (Le reste de la loop trading ici — On simplifie pour le déploiement)
                # On valide juste la détection pour l'instant
                logger.info(f"Market Regime Detected: {regime}")

                await asyncio.sleep(300) 
            except Exception as e:
                logger.error(f"Loop Error: {e}"); await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/", response_class=JSONResponse)
def root():
    return {
        "status": "ynor sovereign live",
        "engine": "quant regime",
        "mode": "autonomous trading",
        "market_regime": BOT_STATE["regime"],
        "dashboard": "/dashboard"
    }

@app.get("/regime")
def get_regime():
    return {"market_regime": BOT_STATE.get("regime")}

@app.get("/health")
def health():
    return {"status": "healthy", "regime": BOT_STATE["regime"]}

@app.get("/status")
def status():
    return BOT_STATE

@app.get("/control/pause")
def pause():
    BOT_STATE["paused"] = True
    return {"trading": "paused"}

@app.get("/control/resume")
def resume():
    BOT_STATE["paused"] = False
    return {"trading": "resumed"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    status_color = "red" if BOT_STATE["kill_switch"] else ("orange" if BOT_STATE["paused"] else "#10b981")
    html = f"<html><body style='background:#111; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | INTEL ACTIVE</h1><div style='background:#222; padding:20px; border-radius:10px;'><h2 style='color:{status_color}; margin:0;'>{BOT_STATE['status']}</h2><p>Market Regime: <span style='color:#38bdf8; font-weight:bold;'>{BOT_STATE['regime']}</span></p><p>Balance: ${BOT_STATE['balance']:,.2f}</p></div></body></html>"
    return html
