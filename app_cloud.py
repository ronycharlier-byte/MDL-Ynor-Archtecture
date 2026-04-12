import asyncio
import sys
import os
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
logger = logging.getLogger("YNOR_CLOUD")

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
        def get_geo_alpha(self, s): return 0.5
    class YnorBitgetConnector:
        def get_balance(self): return 100.0
        def place_order(self, **k): return {"status": "mocked"}
    class MillenniumGrandSolver:
        def decide(self, s): return "hold"
        def check_kill_switch(self, b): return False
        def compute_position_size(self, b, p): return 0.001

REPORT_PATH = "data/investing_full_report.json"
STATUS_PATH = "data/live_market_status.json"
os.makedirs("data", exist_ok=True)
os.makedirs("static", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    scraper = YnorNewsScraper(REPORT_PATH)
    connector = YnorBitgetConnector()
    solver = MillenniumGrandSolver()
    sentinel = YnorEconomicSentinel("", REPORT_PATH)

    async def news_worker():
        while True:
            try: scraper.update_report(); logger.info("News updated"); await asyncio.sleep(600)
            except: await asyncio.sleep(60)
    
    async def trading_loop():
        """ Boucle Autonome : Le coeur du Hedge Fund """
        logger.info("Starting Autonomous Trading Loop")
        while True:
            try:
                balance = connector.get_balance()
                if solver.check_kill_switch(balance):
                    logger.warning("Trading suspended by Kill Switch")
                    break
                
                # Récupération du Sentiment
                score = sentinel.get_geo_alpha("BTC")
                signal = solver.decide(score)
                
                if signal != "hold":
                    # Prix fictif pour calcul (en prod, fetch via yfinance ou exchange)
                    price = 65000 
                    size = solver.compute_position_size(balance, price)
                    if size > 0:
                        connector.place_order(side=signal, size=size)
                
                await asyncio.sleep(300) # Check toutes les 5 min
            except Exception as e:
                logger.error(f"Loop Error: {e}")
                await asyncio.sleep(60)

    asyncio.create_task(news_worker())
    asyncio.create_task(trading_loop())
    logger.info("[YNOR BOOT] Engine & Workers started")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return {"status": "ynor sovereign live", "timestamp": datetime.now().isoformat()}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/status")
def get_status():
    if os.path.exists(STATUS_PATH):
        with open(STATUS_PATH, 'r') as f: return json.load(f)
    return {"status": "initializing"}
