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
    "balance": 1000.0,
    "initial_balance": 1000.0,
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
        def kill_switch(self, d): return False

# --- PRO VERSION GLOBALS ---
DRY_RUN = True  # ⚠️ SAFE MODE ACTIF
MAX_TRADES_PER_DAY = 5
COOLDOWN_SECONDS = 300
CONFIDENCE_THRESHOLD = 0.75

last_trade_time = 0
trades_today = 0
REPORT_PATH = "data/investing_full_report.json"
os.makedirs("data", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    global last_trade_time, trades_today
    
    scraper = YnorNewsScraper(REPORT_PATH)
    connector = YnorBitgetConnector()
    initial_balance = connector.get_balance()
    BOT_STATE["balance"] = initial_balance
    BOT_STATE["initial_balance"] = initial_balance
    
    solver = MillenniumGrandSolver(initial_balance=initial_balance)
    sentinel = YnorEconomicSentinel("", REPORT_PATH)

    async def news_worker():
        while True:
            try: scraper.update_report(); logger.info("News updated"); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        global last_trade_time, trades_today
        logger.info(f"Starting Pro Trading Loop | DRY_RUN: {DRY_RUN}")
        
        while True:
            try:
                sentiment = sentinel.get_geo_alpha("BTC")
                trend = "bullish" 
                volatility = 0.01 
                balance = connector.get_balance()
                BOT_STATE["balance"] = balance

                drawdown = solver.compute_drawdown(balance)
                if solver.kill_switch(drawdown):
                    BOT_STATE["status"] = "STOPPED (KILL SWITCH)"
                    await asyncio.sleep(300); continue

                if trades_today >= MAX_TRADES_PER_DAY:
                    await asyncio.sleep(300); continue

                if time.time() - last_trade_time < COOLDOWN_SECONDS:
                    await asyncio.sleep(10); continue

                if not solver.market_filter(volatility, trend):
                    await asyncio.sleep(300); continue

                score = solver.compute_score(sentiment, trend, volatility)
                update_dashboard("HUNTING", score)
                
                if score < CONFIDENCE_THRESHOLD:
                    await asyncio.sleep(300); continue

                size = solver.compute_position_size(balance)
                
                if DRY_RUN:
                    logger.info(f"🧪 [DRY RUN] Trade size: {size} | Score: {score}")
                    update_dashboard("BUY (DRY)", score)
                else:
                    response = connector.place_order(side="buy", size=size)
                    if response.get("code") == "00000":
                        update_dashboard("BUY (LIVE)", score)
                    else:
                        logger.error(f"❌ Order failed: {response}")
                        await asyncio.sleep(60); continue
                
                last_trade_time = time.time()
                trades_today += 1
                BOT_STATE["trades_today"] = trades_today
                BOT_STATE["last_trade_time"] = datetime.now().strftime("%H:%M:%S")

            except Exception as e:
                logger.error(f"🔥 Loop Error: {e}")
                await asyncio.sleep(60)
            
            await asyncio.sleep(30) # Fréquence monitoring accrue

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    logger.info("[YNOR BOOT] Engine Online")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "ynor live", "dry_run": DRY_RUN, "trades_today": trades_today}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    log_html = "".join([f"<p style='margin:5px 0; font-family:monospace; color:#94a3b8;'>[{log['time']}] {log['signal']} (Score: {log['confidence']:.2f})</p>" for log in BOT_STATE["logs"][-10:]])
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>YNOR | Sovereign Dashboard</title>
        <meta http-equiv="refresh" content="5">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&family=JetBrains+Mono&display=swap" rel="stylesheet">
        <style>
            :root {{ --bg: #0f172a; --card: #1e293b; --accent: #38bdf8; --red: #f43f5e; --green: #10b981; }}
            body {{ font-family: 'Outfit', sans-serif; background: var(--bg); color: white; margin: 0; padding: 20px; }}
            .container {{ max-width: 800px; margin: 0 auto; }}
            .header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
            .live-dot {{ width: 10px; height: 10px; background: var(--accent); border-radius: 50%; display: inline-block; margin-right: 10px; box-shadow: 0 0 10px var(--accent); }}
            .box {{ padding: 25px; margin-bottom: 20px; border-radius: 16px; background: var(--card); border: 1px solid #334155; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1); }}
            .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
            h1 {{ font-size: 24px; margin: 0; letter-spacing: -1px; }}
            h2 {{ font-size: 14px; text-transform: uppercase; color: #94a3b8; margin-top: 0; margin-bottom: 15px; letter-spacing: 1px; }}
            .value {{ font-size: 32px; font-weight: 700; margin-bottom: 5px; }}
            .sub-value {{ font-size: 14px; color: var(--accent); }}
            .log-container {{ background: #020617; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; }}
            @media (max-width: 600px) {{ .grid {{ grid-template-columns: 1fr; }} }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1><span class="live-dot"></span>YNOR ZENITH</h1>
                <div style="font-size: 14px; color: #94a3b8;">{"[TEST MODE]" if DRY_RUN else "[LIVE]"}</div>
            </div>

            <div class="box">
                <h2>Système Status</h2>
                <div class="value" style="color: {var(--green) if BOT_STATE["status"]=="RUNNING" else var(--red)}">{BOT_STATE["status"]}</div>
                <div class="sub-value">SYNC: {datetime.now().strftime("%H:%M:%S")}</div>
            </div>

            <div class="grid">
                <div class="box">
                    <h2>Capital & Performance</h2>
                    <div class="value">${BOT_STATE["balance"]:,.2f}</div>
                    <div class="sub-value">PnL: {BOT_STATE["pnl"]:+.2f}$ ({round(BOT_STATE["drawdown"]*100,2)}%)</div>
                </div>
                <div class="box">
                    <h2>Dernière Décision</h2>
                    <div class="value" style="color: var(--accent)">{BOT_STATE["last_signal"]}</div>
                    <div class="sub-value">Score: {BOT_STATE["confidence"]:.4f}</div>
                </div>
            </div>

            <div class="box">
                <h2>Contrôle du Risque</h2>
                <div style="font-size: 18px; font-weight: 700;">{BOT_STATE["trades_today"]} / {BOT_STATE["max_trades"]} trades <span style="font-weight: 400; color: #94a3b8; font-size: 14px;">(Last: {BOT_STATE["last_trade_time"] or "N/A"})</span></div>
            </div>

            <div class="box">
                <h2>Audit Log (Sovereign)</h2>
                <div class="log-container">
                    {log_html or "<p style='color:#475569'>Initialisation du manifold...</p>"}
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return html
