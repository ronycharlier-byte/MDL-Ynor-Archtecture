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
    "regime": "SIDEWAYS",
    "balance": 1000.0,
    "initial_balance": 1000.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "positions": {"BTC": "HUNTING", "ETH": "HUNTING", "SOL": "HUNTING"},
    "allocation": {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0},
    "trades_today": 0,
    "logs": []
}

def normalize_sentiment(val):
    return max(-1.0, min(1.0, (val - 0.5) * 2))

def update_dashboard(symbol, signal, allocation, regime):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["allocation"][pair] = allocation
    BOT_STATE["regime"] = regime
    if BOT_STATE["balance"] and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if BOT_STATE["drawdown"] > 0.10: BOT_STATE["status"] = "STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{pair}: {signal} (Alloc: {allocation:.2f})" })
    if len(BOT_STATE["logs"]) > 30: BOT_STATE["logs"] = BOT_STATE["logs"][-30:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Minimal Fallbacks
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class MillenniumGrandSolver:
        def __init__(self, *a): pass
        def compute_indicators(self, df): return df
        def detect_market_regime(self, t, v): return "sideways"
        def adjust_score_by_regime(self, s, r): return s
        def regime_filter(self, d, r): return d
        def compute_score(self, s, t, v): return 50
        def decide(self, s): return "HOLD"
        def compute_allocation(self, s): return {k: 0 for k in s}
        def compute_position_size(self, *a): return 0.001

DRY_RUN = True
MAX_TRADES_PER_DAY = 10
MAX_EXPOSURE = 0.3 # Max 30% du capital engagé
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
                sentiment = normalize_sentiment(sentinel.get_geo_alpha("BTC"))
                
                # 1. Pipeline Multi-Assets (Collect Scores)
                current_scores = {}
                asset_data = {}

                for symbol in SYMBOLS:
                    await asyncio.sleep(2) 
                    df = yf.Ticker(symbol).history(period="1d", interval="5m")
                    if df.empty or len(df) < 50: continue
                    
                    df_proc = solver.compute_indicators(df)
                    row = df_proc.iloc[-1]
                    trend = "bullish" if row["Close"] > row["ema"] else "bearish"
                    volatility = row.get("volatility_norm", 0.1)

                    regime = solver.detect_market_regime(trend, volatility)
                    score = solver.compute_score(sentiment, trend, volatility)
                    score = solver.adjust_score_by_regime(score, regime)
                    
                    current_scores[symbol] = score
                    asset_data[symbol] = {"price": row["Close"], "regime": regime, "volatility": volatility}

                # 2. Optimized Portfolio Allocation
                allocations = solver.compute_allocation(current_scores)

                # 3. Execution
                for symbol, alloc_share in allocations.items():
                    score = current_scores[symbol]
                    regime = asset_data[symbol]["regime"]
                    decision = solver.decide(score)
                    decision = solver.regime_filter(decision, regime)
                    
                    update_dashboard(symbol, decision, alloc_share, regime)

                    if decision != "HOLD" and alloc_share > 0:
                        # Safety Checks
                        if BOT_STATE["trades_today"] >= MAX_TRADES_PER_DAY: continue
                        if time.time() - l_trade_t < 600: continue
                        
                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {decision} | Alloc: {alloc_share:.2f}")
                        else:
                            size = solver.compute_position_size(balance, alloc_share, asset_data[symbol]["price"])
                            side = "buy" if "BUY" in decision else "sell"
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=side, size=size)
                            if res.get("code") == "00000":
                                l_trade_t = time.time(); BOT_STATE["trades_today"] += 1

                await asyncio.sleep(600) 
            except Exception as e:
                logger.error(f"Loop Error: {e}")
                await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    pos_html = "".join([f"<p style='margin:5px 0;'>{k}: <span style='color:#38bdf8; font-weight:bold;'>{v}</span> (Alloc: {BOT_STATE['allocation'][k]:.2f})</p>" for k,v in BOT_STATE["positions"].items()])
    log_html = "".join([f"<p style='color:#94a3b8; font-family:monospace; font-size:12px; margin:2px 0;'>[{l['time']}] {l['msg']}</p>" for l in BOT_STATE["logs"][-12:]])
    html = f"<html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | PORTFOLIO ENGINE V1</h1><div style='background:#0f172a; padding:20px; border-radius:12px;'><h2>Global Regime: {BOT_STATE['regime'].upper()}</h2><p>Balance: ${BOT_STATE['balance']:,.2f}</p>{pos_html}</div><div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div></body></html>"
    return html
