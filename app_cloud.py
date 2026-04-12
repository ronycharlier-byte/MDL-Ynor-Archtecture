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
    # Initial balance via API si possible
    initial_balance = connector.get_balance()
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
                # --- DATA ACQUISITION ---
                sentiment = sentinel.get_geo_alpha("BTC")
                trend = "bullish" # À brancher sur un indicateur TA
                volatility = 0.01 # À brancher sur un indicateur TA
                balance = connector.get_balance()

                # --- KILL SWITCH & SAFETY ---
                drawdown = solver.compute_drawdown(balance)
                if solver.kill_switch(drawdown):
                    logger.warning("🛑 Trading stopped (drawdown)")
                    await asyncio.sleep(300); continue

                if trades_today >= MAX_TRADES_PER_DAY:
                    logger.info("📉 Max trades reached for today")
                    await asyncio.sleep(300); continue

                if time.time() - last_trade_time < COOLDOWN_SECONDS:
                    await asyncio.sleep(60); continue

                # --- MARKET FILTER ---
                if not solver.market_filter(volatility, trend):
                    logger.info("🚫 Market not safe (Filter Active)")
                    await asyncio.sleep(300); continue

                # --- SCORING ---
                score = solver.compute_score(sentiment, trend, volatility)
                
                if score < CONFIDENCE_THRESHOLD:
                    await asyncio.sleep(300); continue

                # --- EXECUTION ---
                size = solver.compute_position_size(balance)
                
                if DRY_RUN:
                    logger.info(f"🧪 [DRY RUN] Trade size: {size} | Score: {score}")
                else:
                    response = connector.place_order(side="buy", size=size)
                    if response.get("code") != "00000":
                        logger.error(f"❌ Order failed: {response}")
                        await asyncio.sleep(60); continue
                
                # --- UPDATE STATE ---
                last_trade_time = time.time()
                trades_today += 1
                logger.info(f"✅ Trade executed | Score: {score}")

            except Exception as e:
                logger.error(f"🔥 Loop Error: {e}")
                await asyncio.sleep(60)
            
            await asyncio.sleep(300)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    logger.info("[YNOR BOOT] Engine Online")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "ynor live", "dry_run": DRY_RUN, "trades_today": trades_today}

@app.get("/health")
def health():
    return {"status": "healthy"}
