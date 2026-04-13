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
    "regime": "RANGE", 
    "balance": 1000.0, 
    "initial_balance": 1000.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "last_signal": "NONE",
    "confidence": 0.0,
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
MAX_TRADE_SIZE_USD = 50.0
MAX_DAILY_TRADES = 5
KILL_SWITCH_THRESHOLD = 0.10

# --- SECURE BOOTSTRAP ---
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver, YnorMarketRegime
    BOOT_SUCCESS = True
except Exception as e:
    logger.critical(f"🔥 CRITICAL IMPORT ERROR: {e}")
    BOOT_SUCCESS = False
    class YnorMarketRegime:
        def detect(self, *a): return "RANGE"
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "error"}
    class MillenniumGrandSolver:
        def __init__(self, initial_balance=1000): pass
        def compute_indicators(self, df): return df
        def compute_score(self, s, t, v): return 50
        def decide(self, s, r): return "HOLD"
        def compute_allocation(self, s, b): return 0.0

def normalize_sentiment(val):
    return max(-1.0, min(1.0, (val - 0.5) * 2))

def is_valid_data(df):
    return df is not None and not df.empty and len(df) > 5

def check_kill_switch():
    if BOT_STATE["kill_switch"]: return True
    if BOT_STATE["initial_balance"] > 0:
        drawdown = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if drawdown > KILL_SWITCH_THRESHOLD: return True
    return False

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance:
        BOT_STATE["balance"] = balance; BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"])
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
                # 1. Régime & Sentiment
                regime = regime_engine.detect("BTC-USD")
                BOT_STATE["regime"] = regime
                sentiment = normalize_sentiment(sentinel.get_geo_alpha("BTC"))

                if check_kill_switch():
                    BOT_STATE["status"] = "🚨 STOPPED (KILL SWITCH)"
                    return 
                if BOT_STATE.get("paused"):
                    await asyncio.sleep(60); continue

                # 3. Decision Logic (Signal + Mock Allocation)
                df = yf.download("BTC-USD", period="1d", interval="5m", progress=False)
                if is_valid_data(df):
                    df = solver.compute_indicators(df)
                    
                    # Extraction Scalaire
                    close_prices = df["Close"]
                    if isinstance(close_prices, pd.DataFrame): close_prices = close_prices.iloc[:, 0]
                    
                    last_price = float(close_prices.iloc[-1])
                    ema_val = float(df["ema"].iloc[-1]) if "ema" in df.columns else last_price
                    
                    trend = "bullish" if last_price > ema_val else "bearish"
                    volatility = float(df["volatility_norm"].iloc[-1]) if "volatility_norm" in df.columns else 0.1

                    # --- SIGNAL ENGINE V2 ---
                    score = solver.compute_score(sentiment, trend, volatility)
                    decision = solver.decide(score, regime)
                    
                    # Update Observability
                    BOT_STATE["last_signal"] = decision
                    BOT_STATE["confidence"] = score
                    
                    # --- MOCK EXECUTION & ALLOCATION ---
                    if decision == "BUY":
                        alloc_usd = solver.compute_allocation(score, BOT_STATE["balance"])
                        BOT_STATE["allocation"]["BTC"] = alloc_usd
                        BOT_STATE["positions"]["BTC"] = "LONG"
                        logger.info(f"🚀 MOCK TRADE: BTC LONG | Alloc: ${alloc_usd:.2f}")
                    
                    elif decision == "SELL":
                        alloc_usd = solver.compute_allocation(score, BOT_STATE["balance"])
                        BOT_STATE["allocation"]["BTC"] = alloc_usd
                        BOT_STATE["positions"]["BTC"] = "SHORT"
                        logger.info(f"📉 MOCK TRADE: BTC SHORT | Alloc: ${alloc_usd:.2f}")
                    
                    else:
                        BOT_STATE["allocation"]["BTC"] = 0.0
                        BOT_STATE["positions"]["BTC"] = "HUNTING"

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
        "market_regime": BOT_STATE["regime"],
        "last_signal": BOT_STATE["last_signal"],
        "confidence": BOT_STATE["confidence"],
        "positions": BOT_STATE["positions"],
        "allocation": BOT_STATE["allocation"]
    }

@app.get("/status")
def status():
    BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
    return BOT_STATE

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    status_color = "red" if BOT_STATE["kill_switch"] else ("orange" if BOT_STATE["paused"] else "#10b981")
    pos_html = "".join([f"<p>{k}: <span style='color:#38bdf8;'>{v}</span> (Alloc: ${BOT_STATE['allocation'][k]:.2f})</p>" for k,v in BOT_STATE["positions"].items()])
    html = f"""
    <html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'>
        <h1 style='color:#38bdf8;'>YNOR ZENITH | EXECUTION ACTIVE</h1>
        <div style='background:#0f172a; padding:25px; border-radius:12px;'>
            <h2 style='color:{status_color};'>{BOT_STATE['status']}</h2>
            <div style='display:grid; grid-template-columns: 1fr 1fr; gap:30px;'>
                <div>
                    <h3 style='color:#64748b;'>RÉGIME: {BOT_STATE['regime']}</h3>
                    <p>Dernier Signal: {BOT_STATE['last_signal']}</p>
                    {pos_html}
                </div>
                <div>
                    <h3 style='color:#64748b;'>SOLDE: ${BOT_STATE['balance']:,.2f}</h3>
                    <p>Confiance: {BOT_STATE['confidence']:.0f}%</p>
                </div>
            </div>
        </div>
    </body></html>
    """
    return html
