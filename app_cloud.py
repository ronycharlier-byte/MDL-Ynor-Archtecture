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

# --- FIX PYTHON PATH ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# --- CONFIG LOGGING ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("YNOR_SYSTEM")

# --- GLOBAL BOT STATE (DASHBOARD) ---
BOT_STATE = {
    "status": "RUNNING",
    "balance": 0.0,
    "initial_balance": 1.0, # Placeholder
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
    
    # Kill Switch Logic
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
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver
except Exception as e:
    logger.error(f"[BOOT ERROR] {e}")
    # Fallbacks si modules absents
    class YnorNewsScraper:
        def __init__(self, *a, **k): pass
        def update_report(self): pass
    class YnorEconomicSentinel:
        def __init__(self, *a, **k): pass
        def get_geo_alpha(self, s): return 0.8
    class YnorBitgetConnector:
        def get_balance(self): return 1000.0
        def place_order(self, **k): return {"code": "00000", "status": "mocked"}
    class MillenniumGrandSolver:
        def __init__(self, *a, **k): self.stop_trading = False
        def compute_score(self, *a): return 0.8
        def market_filter(self, *a): return True
        def compute_position_size(self, b): return b * 0.01
        def compute_drawdown(self, b): return 0

# --- PRO VERSION GLOBALS ---
DRY_RUN = True
MAX_TRADES_PER_DAY = 5
COOLDOWN_SECONDS = 300
CONFIDENCE_THRESHOLD = 0.75

REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    scraper = YnorNewsScraper(REPORT_PATH)
    connector = YnorBitgetConnector()
    
    # REAL BALANCE SYNC
    balance = connector.get_balance()
    if balance is not None:
        BOT_STATE["balance"] = balance
        BOT_STATE["initial_balance"] = balance
    
    solver = MillenniumGrandSolver(initial_balance=BOT_STATE["initial_balance"])
    sentinel = YnorEconomicSentinel("", REPORT_PATH)

    async def news_worker():
        while True:
            try: scraper.update_report(); logger.info("News updated"); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        global trades_today
        current_trades = 0
        last_t_time = 0
        
        logger.info(f"Starting Pro Trading Loop | DRY_RUN: {DRY_RUN}")
        
        while True:
            try:
                if BOT_STATE["status"] == "STOPPED (KILL SWITCH)":
                    await asyncio.sleep(300); continue

                # SYNC REAL BALANCE
                balance = connector.get_balance()
                if balance is not None:
                    BOT_STATE["balance"] = balance

                sentiment = sentinel.get_geo_alpha("BTC")
                trend = "bullish" 
                volatility = 0.01 

                if current_trades >= MAX_TRADES_PER_DAY:
                    await asyncio.sleep(300); continue

                if time.time() - last_t_time < COOLDOWN_SECONDS:
                    await asyncio.sleep(10); continue

                if not solver.market_filter(volatility, trend):
                    await asyncio.sleep(300); continue

                score = solver.compute_score(sentiment, trend, volatility)
                update_dashboard("HUNTING", score)
                
                if score < CONFIDENCE_THRESHOLD:
                    await asyncio.sleep(300); continue

                size = solver.compute_position_size(balance)
                
                if DRY_RUN:
                    logger.info(f"🧪 [DRY RUN] Trade size: {size}")
                    update_dashboard("BUY (DRY)", score)
                else:
                    response = connector.place_order(side="buy", size=size)
                    if response.get("code") == "00000":
                        update_dashboard("BUY (LIVE)", score)
                        logger.info("✅ Order success")
                    else:
                        logger.error(f"❌ Order failed: {response}")
                        await asyncio.sleep(60); continue
                
                last_t_time = time.time()
                current_trades += 1
                BOT_STATE["trades_today"] = current_trades
                BOT_STATE["last_trade_time"] = datetime.now().strftime("%H:%M:%S")

            except Exception as e:
                logger.error(f"🔥 Loop Error: {e}")
                await asyncio.sleep(60)
            
            await asyncio.sleep(30)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    logger.info("[YNOR BOOT] Engine Online")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "ynor live", "dry_run": DRY_RUN, "trades_today": BOT_STATE["trades_today"]}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    log_html = "".join([f"<p style='margin:5px 0; font-family:monospace; color:#94a3b8;'>[{log['time']}] {log['signal']} (Score: {log['confidence']:.2f})</p>" for log in BOT_STATE["logs"][-10:]])
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>YNOR | Real-Time Monitor</title>
        <meta http-equiv="refresh" content="5">
        <style>
            :root {{ --bg: #020617; --card: #0f172a; --accent: #38bdf8; --red: #f43f5e; --green: #10b981; }}
            body {{ font-family: sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; }}
            .container {{ max-width: 900px; margin: 0 auto; }}
            .box {{ padding: 20px; margin-bottom: 20px; border-radius: 12px; background: var(--card); border: 1px solid #1e293b; }}
            .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; }}
            h1 {{ font-size: 20px; color: var(--accent); }}
            .val {{ font-size: 28px; font-weight: bold; margin: 5px 0; }}
            .sub {{ font-size: 13px; color: #64748b; }}
            .log {{ background: #000; padding: 10px; border-radius: 5px; max-height: 200px; overflow: hidden; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>YNOR ZENITH | BITGET LIVE SYNC</h1>
            <div class="box">
                <div class="sub">STATUS SYSTÈME</div>
                <div class="val" style="color: {var(--green) if "RUNNING" in BOT_STATE["status"] else var(--red)}">{BOT_STATE["status"]}</div>
            </div>
            <div class="grid">
                <div class="box">
                    <div class="sub">SOLDE RÉEL (USDT)</div>
                    <div class="val">${BOT_STATE["balance"]:,.2f}</div>
                    <div class="sub">Drawdown: {round(BOT_STATE["drawdown"]*100,2)}%</div>
                </div>
                <div class="box">
                    <div class="sub">PNL SESSION</div>
                    <div class="val" style="color: {var(--green) if BOT_STATE["pnl"] >= 0 else var(--red)}">${BOT_STATE["pnl"]:+.2f}</div>
                    <div class="sub">Initial: ${BOT_STATE["initial_balance"]:,.2f}</div>
                </div>
                <div class="box">
                    <div class="sub">SIGNAL ACTUEL</div>
                    <div class="val" style="color: var(--accent)">{BOT_STATE["last_signal"]}</div>
                    <div class="sub">Score: {BOT_STATE["confidence"]:.4f}</div>
                </div>
            </div>
            <div class="box">
                <div class="sub">JOURNAL D'AUDIT</div>
                <div class="log">{log_html or "En attente de données..."}</div>
            </div>
        </div>
    </body>
    </html>
    """
    return html
