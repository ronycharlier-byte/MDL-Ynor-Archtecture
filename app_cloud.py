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

    BOT_STATE["logs"].append({"time": datetime.now().strftime("%H:%M:%S"), "msg": f"{pair}: {signal} (Rel: {confidence:.2f})" })
    if len(BOT_STATE["logs"]) > 50: BOT_STATE["logs"] = BOT_STATE["logs"][-50:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver, YnorMarketRegime, YnorPortfolioEngine
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallback minimal mocks
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class YnorPortfolioEngine:
        def __init__(self, **k): pass
        def allocate(self, b, s): return {}
    class MillenniumGrandSolver:
        def __init__(self, initial_balance=1000): 
            self.initial_balance = initial_balance
        def compute_indicators(self, df): return df
        def compute_score(self, d): return 50
        def decide_adaptive(self, s, r): return "HOLD"
        def compute_position_size(self, *a): return 0.001
    class YnorMarketRegime:
        def detect(self, df): return "range"

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
DRY_RUN = True
COOLDOWN_SECONDS = 300
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

async def fetch_history(ticker):
    try: return yf.Ticker(ticker).history(period="1d", interval="5m")
    except: return pd.DataFrame()

@asynccontextmanager
async def lifespan(app: FastAPI):
    connector = YnorBitgetConnector()
    balance = connector.get_balance()
    if balance:
        BOT_STATE["balance"] = balance; BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"])
    regime_engine = YnorMarketRegime()
    portfolio_engine = YnorPortfolioEngine(max_total_exposure=0.70, max_asset_allocation=0.30)
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
                
                # 1. Collect Signals
                signals = []
                asset_data = {}

                for symbol in SYMBOLS:
                    df = await fetch_history(symbol)
                    if df.empty or len(df) < 50: continue
                    
                    df_proc = solver.compute_indicators(df)
                    regime = regime_engine.detect(df_proc)
                    row = df_proc.iloc[-1]
                    
                    data_point = {"price": row["Close"], "ema": row["ema"], "rsi": row["rsi"], "volatility": row["volatility"], "sentiment": sentiment}
                    score = solver.compute_score(data_point)
                    action = solver.decide_adaptive(score, regime)
                    
                    signals.append({"symbol": symbol, "score": score, "action": action, "regime": regime})
                    asset_data[symbol] = {"price": row["Close"]}

                # 2. Portfolio Optimized Allocation
                allocations = portfolio_engine.allocate(balance, signals)

                # 3. Execution based on allocations
                for s_info in signals:
                    sym = s_info["symbol"]
                    if sym in allocations and time.time() - l_trade_t > COOLDOWN_SECONDS:
                        allocated_val = allocations[sym]
                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {sym}: {s_info['action']} | Capital: ${allocated_val:.2f} (Score: {s_info['score']})")
                        else:
                            size = allocated_val / asset_data[sym]["price"]
                            res = connector.place_order(symbol=sym.replace("-", ""), side=s_info["action"].lower(), size=size)
                            if res.get("code") == "00000":
                                l_trade_t = time.time(); BOT_STATE["trades_today"] += 1
                                logger.info(f"✅ Executed {sym}")
                    
                    # Log to dashboard regardless of trade
                    update_dashboard(sym, s_info["action"] if s_info["action"] != "HOLD" else "HUNTING", s_info["score"] / 100.0, s_info["regime"])

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
    html = f"<html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'><h1>YNOR ZENITH | PORTFOLIO MASTER</h1><div style='background:#0f172a; padding:20px; border-radius:12px;'><h2>Capital Allocation Live</h2><p>Balance: ${BOT_STATE['balance']:,.2f}</p>{pos_html}</div><div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div></body></html>"
    return html
