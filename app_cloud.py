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

# --- FIX PYTHON PATH ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- CONFIG LOGGING ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("YNOR_SYSTEM")

# --- GLOBAL BOT STATE (DASHBOARD) ---
BOT_STATE = {
    "status": "RUNNING",
    "balance": 1000.0, # Seed value
    "initial_balance": 1000.0, 
    "pnl": 0.0,
    "drawdown": 0.0,
    "positions": {"BTC": "HOLD", "ETH": "HOLD", "SOL": "HOLD"},
    "confidence": {"BTC": 0.0, "ETH": 0.0, "SOL": 0.0},
    "trades_today": 0,
    "max_trades": 10,
    "last_trade_time": None,
    "logs": []
}

def update_dashboard(symbol, signal, confidence):
    pair = symbol.split("-")[0]
    BOT_STATE["positions"][pair] = signal
    BOT_STATE["confidence"][pair] = confidence
    
    # --- SAFE CALCULATION ---
    if BOT_STATE["balance"] and BOT_STATE["initial_balance"]:
        BOT_STATE["pnl"] = BOT_STATE["balance"] - BOT_STATE["initial_balance"]
        BOT_STATE["drawdown"] = (BOT_STATE["initial_balance"] - BOT_STATE["balance"]) / BOT_STATE["initial_balance"]
        
        # --- KILL SWITCH PROTECTION ---
        if BOT_STATE["drawdown"] > 0.10:
            BOT_STATE["status"] = "STOPPED (KILL SWITCH)"
            logger.warning("🚨 KILL SWITCH ACTIVATED")

    BOT_STATE["logs"].append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "msg": f"{pair}: {signal} ({confidence:.2f})"
    })
    if len(BOT_STATE["logs"]) > 50: BOT_STATE["logs"] = BOT_STATE["logs"][-50:]

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, YnorScoringEngine
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallback minimal constants
    class YnorScoringEngine:
        def compute_score(self, p, s): return 80
        def compute_position_size(self, b, s, p): return 0.001
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000"}
    class YnorNewsScraper:
        def __init__(self, *a): pass
        def update_report(self): pass
    class YnorEconomicSentinel:
        def __init__(self, *a, **k): pass
        def get_geo_alpha(self, s): return 0.8

SYMBOLS = ["BTC-USD", "ETH-USD", "SOL-USD"]
DRY_RUN = True
COOLDOWN_SECONDS = 300
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

async def fetch_history(ticker):
    try: return yf.Ticker(ticker).history(period="1d", interval="5m")['Close'].tolist()
    except: return []

@asynccontextmanager
async def lifespan(app: FastAPI):
    scraper = YnorNewsScraper(REPORT_PATH)
    connector = YnorBitgetConnector()
    
    # SAFE INITIAL BALANCE
    balance = connector.get_balance()
    if balance is not None and balance > 0:
        BOT_STATE["balance"] = balance
        BOT_STATE["initial_balance"] = balance
        logger.info(f"Initial balance synchronized: {balance} USDT")
    
    engine = YnorScoringEngine()
    sentinel = YnorEconomicSentinel("", REPORT_PATH)

    async def news_worker():
        while True:
            try: scraper.update_report(); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        l_trade_t = 0
        logger.info("Starting Pro Trading Loop")
        while True:
            try:
                if "STOPPED" in BOT_STATE["status"]: await asyncio.sleep(300); continue
                
                # SAFE BALANCE UPDATE
                balance = connector.get_balance()
                if balance is not None:
                    BOT_STATE["balance"] = balance
                    # Auto-calibration si initial_balance est nul
                    if BOT_STATE["initial_balance"] <= 0:
                        BOT_STATE["initial_balance"] = balance
                else:
                    logger.warning("Balance fetch failed, skipping cycle safety check")
                
                sentiment = sentinel.get_geo_alpha("BTC")

                for symbol in SYMBOLS:
                    prices = await fetch_history(symbol)
                    if not prices or len(prices) < 20: continue
                    
                    score = engine.compute_score(prices, sentiment)
                    signal = "HOLD"
                    if score > 75: signal = "BUY"
                    elif score < 25: signal = "SELL"
                    
                    # COOLDOWN CHECK
                    if time.time() - l_trade_t < COOLDOWN_SECONDS: signal = "HOLD"
                    if BOT_STATE["trades_today"] >= BOT_STATE["max_trades"]: signal = "HOLD"

                    update_dashboard(symbol, signal if signal != "HOLD" else "HUNTING", score / 100.0)

                    if signal != "HOLD":
                        if DRY_RUN:
                            logger.info(f"🧪 [DRY] {symbol}: {signal} | Score: {score}")
                        else:
                            size = engine.compute_position_size(BOT_STATE["balance"], score, prices[-1])
                            res = connector.place_order(symbol=symbol.replace("-", ""), side=signal.lower(), size=size)
                            if res.get("code") == "00000":
                                l_trade_t = time.time()
                                BOT_STATE["trades_today"] += 1
                                logger.info(f"✅ Order Executed: {symbol}")

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
    pos_html = "".join([f"<p style='margin:5px 0;'>{k}: <span style='color:#38bdf8; font-weight:bold;'>{v}</span> (Score: {BOT_STATE['confidence'][k]:.2f})</p>" for k,v in BOT_STATE["positions"].items()])
    log_html = "".join([f"<p style='margin:2px 0; font-family:monospace; font-size:12px; color:#94a3b8;'>[{log['time']}] {log['msg']}</p>" for log in BOT_STATE["logs"][-12:]])
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>YNOR ZENITH | Live</title>
        <meta http-equiv="refresh" content="5">
        <style>
            body {{ background:#020617; color:white; font-family: sans-serif; padding:20px; }}
            .card {{ background:#0f172a; padding:20px; border-radius:12px; border:1px solid #1e293b; margin-bottom:20px; }}
            .val {{ font-size: 24px; font-weight: bold; color: #38bdf8; }}
            .red {{ color: #f43f5e; }}
            .green {{ color: #10b981; }}
        </style>
    </head>
    <body>
        <div style="max-width:800px; margin:0 auto;">
            <h1 style="font-size:18px; color:#94a3b8; letter-spacing:2px;">YNOR ENGINE SOUVERAIN</h1>
            <div class="card">
                <div style="font-size:12px; color:#64748b;">STATUT</div>
                <div class="{ 'red' if 'STOPPED' in BOT_STATE['status'] else 'green' }" style="font-size:20px; font-weight:bold;">{BOT_STATE['status']}</div>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
                <div class="card">
                    <div style="font-size:12px; color:#64748b;">SOLDE RÉEL</div>
                    <div class="val">${BOT_STATE['balance']:,.2f}</div>
                    <div style="font-size:12px; color:#64748b; margin-top:5px;">PnL: {BOT_STATE['pnl']:+.2f}$ ({BOT_STATE['drawdown']*100:.2f}%)</div>
                </div>
                <div class="card">
                    <div style="font-size:12px; color:#64748b;">PORTFOLIO</div>
                    {pos_html}
                </div>
            </div>
            <div class="card">
                <div style="font-size:12px; color:#64748b; margin-bottom:10px;">ACTIVITY LOG</div>
                <div style="background:#000; padding:15px; border-radius:8px;">{log_html}</div>
            </div>
        </div>
    </body>
    </html>
    """
    return html
