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
DRY_RUN = True # ⚠️ Mettre à False pour le live réel
ENABLE_LIVE_TRADING = False # 🔒 Double verrou de sécurité
MAX_TRADE_SIZE_USD = 10.0 # Phase 1 : Test Live Ultra-Safe
MAX_DAILY_TRADES = 2
KILL_SWITCH_THRESHOLD = 0.10 # 10% drawdown stop total

def normalize_sentiment(val):
    return max(-1.0, min(1.0, (val - 0.5) * 2))

def check_kill_switch():
    if BOT_STATE["initial_balance"] > 0:
        drawdown = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        if drawdown > KILL_SWITCH_THRESHOLD:
            return True
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
        def detect_market_regime(self, t, v): return "sideways"
        def adjust_score_by_regime(self, s, r): return s
        def regime_filter(self, d, r): return d
        def compute_score(self, s, t, v): return 50
        def decide(self, s): return "HOLD"
        def compute_allocation(self, s): return {k: 0 for k in s}
        def compute_position_size(self, *a): return 0.001

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
                # 1. Kill Switch Check
                if check_kill_switch() or "STOPPED" in BOT_STATE["status"]:
                    BOT_STATE["status"] = "🚨 STOPPED (KILL SWITCH)"
                    logger.critical("🚨 CRITICAL: KILL SWITCH ACTIVATED. TRADING HALTED.")
                    await asyncio.sleep(3600); continue
                
                # 2. Daily Limits
                if BOT_STATE["trades_today"] >= MAX_DAILY_TRADES:
                    logger.info("Daily trade limit reached. Waiting for next cycle.")
                    await asyncio.sleep(3600); continue

                balance = connector.get_balance() or BOT_STATE["balance"]
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
                    decision = solver.decide(score)
                    decision = solver.regime_filter(decision, regime)
                    
                    update_dashboard(symbol, decision, alloc_share, regime)

                    # LIVE EXECUTION BLOCK
                    if decision != "HOLD" and alloc_share > 0:
                        # Safety checks pre-execution
                        if time.time() - l_trade_t < 1800: continue # Cooldown 30min en phase 1

                        # Allocation logic
                        raw_size_usd = balance * 0.01 * alloc_share
                        # Hard Cap Safety
                        size_usd = min(raw_size_usd, MAX_TRADE_SIZE_USD)
                        size_coin = round(size_usd / asset_data[symbol]["price"], 4)

                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {decision} | Size: ${size_usd:.2f}")
                        elif ENABLE_LIVE_TRADING:
                            if size_coin <= 0: continue
                            logger.info(f"🚀 LIVE ORDER: {symbol} | {decision} | ${size_usd:.2f}")
                            side = "buy" if "BUY" in decision else "sell"
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=side, size=size_coin)
                            if res.get("code") == "00000":
                                l_trade_t = time.time(); BOT_STATE["trades_today"] += 1
                                logger.info(f"✅ LIVE CONFIRMED: {symbol}")
                        else:
                            logger.warning(f"🔒 LIVE BLOCKED: Double-lock active. Enable ENABLE_LIVE_TRADING to proceed.")

                await asyncio.sleep(1200) # Scan toutes les 20 min en phase 1
            except Exception as e:
                logger.error(f"Loop Error: {e}")
                await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    status_color = "red" if "STOPPED" in BOT_STATE["status"] else "#10b981"
    mode_text = "LIVE SOUVERAIN" if BOT_STATE["live_mode"] else "OBSERVATION (DRY RUN)"
    mode_color = "#38bdf8" if BOT_STATE["live_mode"] else "#94a3b8"
    
    pos_html = "".join([f"<p style='margin:5px 0;'>{k}: <span style='color:#38bdf8'>{v}</span></p>" for k,v in BOT_STATE["positions"].items()])
    log_html = "".join([f"<p style='color:#64748b; font-family:monospace; font-size:12px;'>[{l['time']}] {l['msg']}</p>" for l in BOT_STATE["logs"][-10:]])
    
    html = f"""
    <html><body style='background:#020617; color:white; font-family:sans-serif; padding:40px;'>
        <div style='max-width:800px; margin:0 auto;'>
            <h1 style='font-size:14px; letter-spacing:2px; color:#64748b; margin-bottom:5px;'>YNOR ZENITH V18.8.0</h1>
            <div style='background:#0f172a; padding:20px; border-radius:12px; border:1px solid #1e293b;'>
                <div style='display:flex; justify-content:space-between; align-items:center;'>
                    <h2 style='margin:0; font-size:24px;'>$ {BOT_STATE['balance']:,.2f}</h2>
                    <div style='color:{mode_color}; font-weight:bold; font-size:12px; border:1px solid {mode_color}; padding:4px 10px; border-radius:30px;'>{mode_text}</div>
                </div>
                <p style='color:#64748b; font-size:12px;'>Status: <span style='color:{status_color}'>{BOT_STATE['status']}</span> | Regime: {BOT_STATE['regime'].upper()}</p>
                <div style='margin-top:20px; display:grid; grid-template-columns: 1fr 1fr; gap:20px;'>
                    <div><h3 style='font-size:12px; color:#64748b;'>PORTFOLIO</h3>{pos_html}</div>
                    <div><h3 style='font-size:12px; color:#64748b;'>PERFORMANCE</h3><p>PnL: ${BOT_STATE['pnl']:+.2f}</p><p>Drawdown: {BOT_STATE['drawdown']*100:.2f}%</p></div>
                </div>
            </div>
            <div style='margin-top:20px; background:#000; padding:15px; border-radius:10px;'>{log_html}</div>
        </div>
    </body></html>
    """
    return html
