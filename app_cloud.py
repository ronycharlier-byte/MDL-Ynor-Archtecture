import asyncio
import sys
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
from datetime import datetime
import json

# --- FIX PYTHON PATH ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper, YnorBitgetConnector, MillenniumGrandSolver
except Exception as e:
    print(f"[BOOT ERROR] {e}")
    # Fallback / Mocks
    class YnorNewsScraper:
        def __init__(self, *a, **k): pass
        def update_report(self): pass
    class YnorEconomicSentinel:
        def __init__(self, *a, **k): pass
        def get_geo_alpha(self, s): return 0
    class YnorBitgetConnector:
        def place_order(self, **k): return {"status": "mocked"}
    class MillenniumGrandSolver:
        def decide(self, s): return "hold"

REPORT_PATH = "data/investing_full_report.json"
STATUS_PATH = "data/live_market_status.json"
os.makedirs("data", exist_ok=True)
os.makedirs("static", exist_ok=True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Lancement des workers en arrière-plan
    scraper = YnorNewsScraper(REPORT_PATH)
    async def news_worker():
        while True:
            try: scraper.update_report(); await asyncio.sleep(300)
            except: await asyncio.sleep(60)
    
    asyncio.create_task(news_worker())
    print("[YNOR BOOT] Engine started")
    yield

app = FastAPI(lifespan=lifespan)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"status": "ynor live", "timestamp": datetime.now().isoformat()}

@app.get("/trade")
def trade():
    connector = YnorBitgetConnector()
    solver = MillenniumGrandSolver()
    
    # Test avec un score fictif pour la validation
    signal = solver.decide(0.8) 
    
    if signal != "hold":
        return connector.place_order(side=signal)
    
    return {"status": "no trade", "reason": "signal hold"}

@app.get("/health")
def health():
    return {"status": "healthy"}
