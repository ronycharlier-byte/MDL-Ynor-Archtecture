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
    "logs": []
}

# --- LIVE SAFETY PROTOCOLS ---
DRY_RUN = True
ENABLE_LIVE_TRADING = False
MAX_TRADE_SIZE_USD = 10.0
MAX_DAILY_TRADES = 2
KILL_SWITCH_THRESHOLD = 0.10

# --- SECURE BOOTSTRAP (WITH ALL FALLBACKS) ---
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver
    BOOT_SUCCESS = True
except Exception as e:
    logger.critical(f"🔥 CRITICAL IMPORT ERROR: {e}")
    BOOT_SUCCESS = False
    
    # DUMMY FALLBACKS TO PREVENT NameError
    class YnorBitgetConnector:
        def get_balance(self): return None
        def place_order(self, **k): return {"code": "error"}
    
    class YnorEconomicSentinel:
        def __init__(self, *a): pass
        def get_geo_alpha(self, a): return 0.5
    
    class YnorNewsScraper:
        def __init__(self, *a): pass
        def update_report(self): pass

    class MillenniumGrandSolver:
        def __init__(self, initial_balance=1000): self.initial_balance = initial_balance
        def compute_indicators(self, df): return df
        def detect_market_regime(self, t, v): return "sideways"
        def adjust_score_by_regime(self, s, r): return s
        def regime_filter(self, d, r): return d
        def compute_score(self, s, t, v): return 50
        def decide(self, s): return "HOLD"
        def compute_allocation(self, s): return {k: 0 for k in s}
        def compute_position_size(self, *a): return 0.0

def normalize_sentiment(val):
    return max(-1.0, min(1.0, (val - 0.5) * 2))

def check_kill_switch():
    if BOT_STATE["initial_balance"] > 0:
        drawdown = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if drawdown > KILL_SWITCH_THRESHOLD: return True
    return False

def update_dashboard(symbol, signal, allocation, regime):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["allocation"][pair] = allocation
    BOT_STATE["regime"] = regime
    BOT_STATE["live_mode"] = ENABLE_LIVE_TRADING and not DRY_RUN
    
    if BOT_STATE["balance"] and BOT_STATE["initial_balance"] > 0:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if BOT_STATE["drawdown"] > KILL_SWITCH_THRESHOLD:
            BOT_STATE["status"] = "🚨 STOPPED (KILL SWITCH)"

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{pair}: {signal} | ({allocation:.2f})" })
    if len(BOT_STATE["logs"]) > 20: BOT_STATE["logs"] = BOT_STATE["logs"][-20:]

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialisation sécurisée des composants
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance:
        BOT_STATE["balance"] = balance; BOT_STATE["initial_balance"] = balance
    
    try:
        solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"] or 1000)
    except:
        solver = MillenniumGrandSolver()

    # Initialisation Sentinel et Scraper (même si BOOT_SUCCESS est False, les classes dummy existent)
    sentinel = YnorEconomicSentinel("", REPORT_PATH)
    scraper = YnorNewsScraper(REPORT_PATH)
    
    if BOOT_SUCCESS:
        BOT_STATE["status"] = "RUNNING"
    else:
        BOT_STATE["status"] = "🛠️ RUNNING (DEGRADED MODE - IMPORTS FAILED)"

    # Workers en arrière-plan
    async def news_worker():
        while True:
            try: scraper.update_report(); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        l_trade_t = 0
        while True:
            try:
                if check_kill_switch() or "STOPPED" in BOT_STATE["status"]:
                    BOT_STATE["status"] = "🚨 STOPPED (KILL SWITCH)"
                    await asyncio.sleep(3600); continue
                
                if BOT_STATE["trades_today"] >= MAX_DAILY_TRADES:
                    await asyncio.sleep(3600); continue

                bal = connector.get_balance()
                if bal: BOT_STATE["balance"] = bal
                sentiment = normalize_sentiment(sentinel.get_geo_alpha("BTC"))
                
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
                    asset_data[symbol] = {"price": row["Close"], "regime": regime}

                allocations = solver.compute_allocation(current_scores)

                for symbol, alloc_share in allocations.items():
                    score = current_scores[symbol]
                    regime = asset_data[symbol]["regime"]
                    decision = solver.regime_filter(solver.decide(score), regime)
                    
                    update_dashboard(symbol, decision, alloc_share, regime)

                    if decision != "HOLD" and alloc_share > 0:
                        if time.time() - l_trade_t < 1800: continue

                        size_usd = min(balance * 0.01 * alloc_share, MAX_TRADE_SIZE_USD)
                        size_coin = round(size_usd / asset_data[symbol]["price"], 4)

                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {decision}")
                        elif ENABLE_LIVE_TRADING and size_coin > 0:
                            side = "buy" if "BUY" in decision else "sell"
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=side, size=size_coin)
                            if res.get("code") == "00000":
                                l_trade_t = time.time(); BOT_STATE["trades_today"] += 1

                await asyncio.sleep(1200) 
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
        "mode": "autonomous trading"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/status")
def status():
    return BOT_STATE

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    status_color = "red" if "STOPPED" in BOT_STATE["status"] or "FAILED" in BOT_STATE["status"] else "#10b981"
    mode_text = "LIVE SOUVERAIN" if BOT_STATE["live_mode"] else "OBSERVATION"
    mode_color = "#38bdf8" if BOT_STATE["live_mode"] else "#94a3b8"
    pos_html = "".join([f"<p style='margin:5px 0;'>{k}: <span style='color:#38bdf8'>{v}</span></p>" for k,v in BOT_STATE["positions"].items()])
    log_html = "".join([f"<p style='font-size:12px; color:#64748b; margin:2px 0;'>[{l['time']}] {l['msg']}</p>" for l in BOT_STATE["logs"][-12:]])
    html = f"<html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | HYBRID BOOT OK</h1><div style='background:#0f172a; padding:20px; border-radius:12px;'><h2 style='color:{status_color}; margin:0;'>{BOT_STATE['status']}</h2><p style='color:{mode_color}; font-weight:bold;'>{mode_text}</p><p>Balance: ${BOT_STATE['balance']:,.2f}</p>{pos_html}</div><div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div></body></html>"
    return html
