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

def normalize_sentiment(val):
    """ Mappe 0->1 en -1->+1 """
    return max(-1.0, min(1.0, (val - 0.5) * 2))

def update_dashboard(signal, confidence):
    BOT_STATE["last_signal"] = signal
    BOT_STATE["confidence"] = confidence
    if BOT_STATE["balance"] and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if BOT_STATE["drawdown"] > 0.10: BOT_STATE["status"] = "STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{signal} (Conf: {confidence:.2f})" })
    if len(BOT_STATE["logs"]) > 20: BOT_STATE["logs"] = BOT_STATE["logs"][-20:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class MillenniumGrandSolver:
        def __init__(self, initial_balance=1000): pass
        def compute_indicators(self, df): return df
        def compute_score(self, s, t, v): return 50
        def decide(self, s): return "HOLD"
        def compute_position_size(self, *a): return 0.001

DRY_RUN = True
MAX_TRADES_PER_DAY = 5
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
                
                bal = connector.get_balance()
                if bal: BOT_STATE["balance"] = bal
                
                # Normalisation Sentiment (-1 à +1)
                raw_sentimentArr = sentinel.get_geo_alpha("BTC") # Suppose return 0-1
                sentiment = normalize_sentiment(raw_sentimentArr)

                for symbol in SYMBOLS:
                    await asyncio.sleep(2) 
                    
                    df = yf.Ticker(symbol).history(period="1d", interval="5m")
                    if df.empty or len(df) < 50: continue
                    
                    df = solver.compute_indicators(df)
                    row = df.iloc[-1]
                    trend = "bullish" if row["Close"] > row["ema"] else "bearish"
                    volatility = row.get("volatility_norm", 0.1)

                    score = solver.compute_score(sentiment, trend, volatility)
                    decision = solver.decide(score)
                    
                    # LOGIQUE SELECTIVE
                    if decision == "HOLD": continue
                    
                    # FILTRES ANTI-FASH-CRASH / OVERTRADE
                    if volatility > 0.8: 
                        logger.warning(f"⚠️ Market too dangerous ({symbol}): Volatility {volatility:.2f}")
                        continue
                    
                    if BOT_STATE["trades_today"] >= MAX_TRADES_PER_DAY: 
                        logger.info("🚫 Max daily trades reached")
                        break # Stop for the session

                    if time.time() - l_trade_t < 600: continue # Cooldown 10min

                    update_dashboard(f"{symbol.split('-')[0]}: {decision}", score / 100.0)

                    if DRY_RUN:
                        logger.info(f"🧪 [DRY] {symbol}: {decision} | Score: {score}")
                    else:
                        size = solver.compute_position_size(BOT_STATE["balance"], score, row["Close"])
                        side = "buy" if "BUY" in decision else "sell"
                        res = connector.place_order(symbol=symbol.replace("-", ""), side=side, size=size)
                        if res.get("code") == "00000":
                            l_trade_t = time.time(); BOT_STATE["trades_today"] += 1
                            logger.info(f"✅ Executed: {symbol} {decision}")

                await asyncio.sleep(600) 

            except Exception as e:
                logger.error(f"Loop Error: {e}")
                await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root(): return {"status": "ynor live", "version": "18.5.0"}

@app.get("/health")
def health(): return {"status": "healthy"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    log_html = "".join([f"<p style='color:#94a3b8; font-family:monospace; font-size:12px;'>[{l['time']}] {l['msg']}</p>" for l in BOT_STATE["logs"][-12:]])
    html = f"<html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | SIGNAL ENGINE V1</h1><div style='background:#0f172a; padding:20px; border-radius:12px;'><h2>Balance: ${BOT_STATE['balance']:,.2f}</h2><p>Last Trade Quality: {BOT_STATE['last_signal']}</p></div><div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div></body></html>"
    return html
