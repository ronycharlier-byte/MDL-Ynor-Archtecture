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
    "regime": "RANGE",
    "balance": 1000.0,
    "initial_balance": 1000.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "positions": {"BTC": "HOLD", "ETH": "HOLD", "SOL": "HOLD"},
    "confidence": {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0},
    "trades_today": 0,
    "logs": []
}

def update_dashboard(symbol, signal, confidence, regime):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["confidence"][pair] = confidence
    BOT_STATE["regime"] = regime
    
    if BOT_STATE["balance"] is not None and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if BOT_STATE["drawdown"] > 0.10: BOT_STATE["status"] = "STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{pair}: {signal} | Conf: {confidence:.2f}"})
    if len(BOT_STATE["logs"]) > 50: BOT_STATE["logs"] = BOT_STATE["logs"][-50:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver, YnorMarketRegime, YnorPortfolioEngine
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallbacks 
    class YnorPortfolioEngine:
        def allocate(self, b, s): return {}
    class YnorMarketRegime:
        def detect(self, df): return "range"
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class MillenniumGrandSolver:
        def __init__(self, *a): pass
        def compute_indicators(self, df): return df
        def compute_score(self, d): return 50
        def decide_adaptive(self, s, r): return "HOLD"

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
DRY_RUN = True
COOLDOWN_SECONDS = 300
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance is not None:
        BOT_STATE["balance"] = balance; BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"])
    regime_engine = YnorMarketRegime()
    portfolio_engine = YnorPortfolioEngine(max_total_exposure=0.05)
    sentinel = YnorEconomicSentinel("", REPORT_PATH)
    scraper = YnorNewsScraper(REPORT_PATH)

    async def news_worker():
        while True:
            try: scraper.update_report(); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        l_trade_t = 0
        while True:
            try:
                if "STOPPED" in BOT_STATE["status"]: await asyncio.sleep(300); continue
                
                balance = connector.get_balance() or BOT_STATE["balance"]
                sentiment = sentinel.get_geo_alpha("BTC")
                
                # 1. Collect Scores
                asset_scores = {}
                asset_data = {}
                global_regime = "range"

                for symbol in SYMBOLS:
                    df = yf.Ticker(symbol).history(period="1d", interval="5m")
                    if df.empty or len(df) < 50: continue
                    
                    df = solver.compute_indicators(df)
                    regime = regime_engine.detect(df)
                    if symbol == "BTC-USD": global_regime = regime # On suit le régime BTC
                    
                    row = df.iloc[-1]
                    data_point = {"price": row["Close"], "ema": row["ema"], "rsi": row["rsi"], "volatility": row["volatility"], "sentiment": sentiment}
                    
                    score = solver.compute_score(data_point)
                    asset_scores[symbol] = score
                    asset_data[symbol] = {"price": row["Close"], "regime": regime}

                # 2. Portfolio Allocation
                allocations = portfolio_engine.allocate(balance, asset_scores)

                # 3. Execution
                for symbol, allocated_usdt in allocations.items():
                    score = asset_scores[symbol]
                    regime = asset_data[symbol]["regime"]
                    signal = solver.decide_adaptive(score, regime)
                    
                    update_dashboard(symbol, signal, score / 100.0, regime)

                    if signal != "HOLD" and time.time() - l_trade_t > COOLDOWN_SECONDS:
                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {signal} (Alloc: ${allocated_usdt:.2f})")
                        else:
                            size = allocated_usdt / asset_data[symbol]["price"]
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=signal.lower(), size=size)
                            if res.get("code") == "00000":
                                l_trade_t = time.time(); BOT_STATE["trades_today"] += 1

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
    pos_html = "".join([f"<p style='margin:5px 0;'>{k}: <span style='color:#38bdf8'>{v}</span> ({BOT_STATE['confidence'][k]:.2f})</p>" for k,v in BOT_STATE["positions"].items()])
    html = f"<html><head><meta http-equiv='refresh' content='10'></head><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | PORTFOLIO ENGINE</h1><div style='background:#0f172a; padding:20px; border-radius:12px;'><h2>Global Regime: {BOT_STATE['regime'].upper()}</h2><p>Balance: ${BOT_STATE['balance']:,.2f}</p>{pos_html}</div></body></html>"
    return html
