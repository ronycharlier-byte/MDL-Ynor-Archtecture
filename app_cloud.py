import asyncio
import sys
import os
from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager
import uvicorn
import json
import yfinance as yf
from datetime import datetime
import numpy as np
import subprocess

# --- FIX PYTHON PATH ---
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Imports souverains
try:
    from ynor_engine import YnorEconomicSentinel, YnorNewsScraper
    from ynor_notifier import YnorTelegramNotifier
    from ynor_millennium_solver import MillenniumGrandSolver
    from ynor_bitget import YnorBitgetConnector
except Exception as e:
    print(f"[BOOT ERROR] {e}")
    
    class YnorNewsScraper:
        def __init__(self, *args, **kwargs): pass
        def update_report(self): pass

    class YnorEconomicSentinel:
        def __init__(self, *args, **kwargs): pass
        def get_geo_alpha(self, s): return 0

    class YnorTelegramNotifier:
        def send_alert(self, msg): print(f"[MOCK NOTIFY] {msg}")

    class MillenniumGrandSolver:
        def get_grand_sovereign_score(self, p): return 0.4, {}

    class YnorBitgetConnector:
        def get_balance(self): return 0.0
        def get_open_position(self, s): return None
        def execute_margin_order(self, *args, **kwargs): return False
        def close_position(self, s): pass

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(news_worker())
    asyncio.create_task(mutation_worker())
    asyncio.create_task(ynor_background_engine())
    yield

app = FastAPI(lifespan=lifespan)
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

REPORT_PATH = "data/investing_full_report.json"
STATUS_PATH = "data/live_market_status.json"
CONFIG_PATH = "data/optimal_configs.json"
ENTRY_PRICES = {}
# Safe Boot Initialization
try:
    SCRAPER = YnorNewsScraper(REPORT_PATH)
    NOTIFIER = YnorTelegramNotifier()
except Exception as e:
    print(f"[SAFE BOOT] {e}")
    SCRAPER = YnorNewsScraper(REPORT_PATH) # Use mock if import failed
    NOTIFIER = YnorTelegramNotifier()

def load_genome():
    try:
        if os.path.exists(CONFIG_PATH):
            with open(CONFIG_PATH, 'r') as f: return json.load(f)
    except: pass
    return {"BTC-USD":0.39,"ETH-USD":0.37,"SOL-USD":0.41,"XRP-USD":0.43,"DOGE-USD":0.41,"LINK-USD":0.39,"ADA-USD":0.49}

async def news_worker():
    while True:
        try:
            SCRAPER.update_report()
            await asyncio.sleep(60)
        except: await asyncio.sleep(10)

async def mutation_worker():
    while True:
        try:
            await asyncio.sleep(86400)
            subprocess.run(["python", "scratch/threshold_benchmark.py"], check=True)
            NOTIFIER.send_alert("🧬 *YNOR EVOLUTION COMPLETE* (7/7 DNA SYNC)")
        except: await asyncio.sleep(3600)

async def fetch_history(ticker, interval="5m", period="1d"):
    try:
        data = yf.Ticker(ticker).history(period=period, interval=interval)
        return data['Close'].tolist()
    except: return []

async def ynor_background_engine():
    global ENTRY_PRICES
    assets = ["BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD", "DOGE-USD", "LINK-USD", "ADA-USD"]
    sentinel = YnorEconomicSentinel("", REPORT_PATH)
    solver = MillenniumGrandSolver()
    bitget = YnorBitgetConnector()
    
    while True:
        try:
            current_balance = bitget.get_balance()
            genome = load_genome()
            status = {
                "balance": current_balance, 
                "pnl": 0.0, # À lier à la DB pour historique réeel
                "win_rate": 0.0,
                "timestamp": datetime.now().strftime("%H:%M:%S"), 
                "assets": {}, 
                "shield": "ACTIVE"
            }
            
            # --- FLASH-CRASH SENSOR (MONITORING BTC) ---
            btc_prices = await fetch_history("BTC-USD", "5m", "1d")
            flash_crash = False
            if len(btc_prices) > 5:
                drop_5m = (btc_prices[-1] - btc_prices[-2]) / btc_prices[-2]
                if drop_5m < -0.01: # -1% EN 5 MINUTTES = FLASH CRASH
                    flash_crash = True
                    status["shield"] = "FLASH CRASH LOCK 🔥"

            for s in assets:
                threshold = genome.get(s, 0.45)
                prices_5m = await fetch_history(s, "5m", "1d")
                prices_1h = await fetch_history(s, "1h", "1d")
                if not prices_5m or not prices_1h: continue
                current_price = prices_5m[-1]
                
                sigma, pillars = solver.get_grand_sovereign_score(prices_5m)
                macro_trend = "UP" if current_price > np.mean(prices_1h[-20:]) else "DOWN"
                alpha = sentinel.get_geo_alpha(s)
                
                spot_symbol = s.replace("-USD", "USDT") 
                pos_type = bitget.get_open_position(spot_symbol)
                action = "HUNTING"
                lev_str = "1x"
                
                if pos_type:
                    roi = (current_price - ENTRY_PRICES.get(s, current_price)) / ENTRY_PRICES.get(s, current_price)
                    if roi < -0.015 or (flash_crash and roi < 0): 
                        bitget.close_position(spot_symbol)
                        if s in ENTRY_PRICES: del ENTRY_PRICES[s]
                    else: action = "HOLDING"
                
                elif sigma > threshold:
                    if flash_crash:
                        action = "SHIELDED"
                    else:
                        # --- DYNAMIC LEVERAGE CALCULATION (DSL) ---
                        conviction_gap = (sigma - threshold) / threshold
                        if conviction_gap > 0.4: target_lev = 20
                        elif conviction_gap > 0.2: target_lev = 12
                        else: target_lev = 5
                        
                        side = "buy" if alpha >= 0 else "sell"
                        if (side == "buy" and macro_trend == "UP") or (side == "sell" and macro_trend == "DOWN"):
                            amt = 0.001 if "BTC" in s else (0.4 if "SOL" in s else 30)
                            if bitget.execute_margin_order(spot_symbol, side, amt, leverage=target_lev):
                                ENTRY_PRICES[s] = current_price
                                action = f"STRIKE {target_lev}X"
                                lev_str = f"{target_lev}x"
                
                status["assets"][s] = {"price": current_price, "sigma": sigma, "action": action, "leverage": lev_str}
            
            with open(STATUS_PATH, "w") as f: json.dump(status, f, indent=4)
            await asyncio.sleep(5)
        except Exception as e:
            print(f"[ENGINE ERROR] {e}")
            await asyncio.sleep(10)

@app.get("/")
def root():
    return {"status": "ynor live"}

@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard():
    try:
        with open(STATUS_PATH, 'r') as f: m = json.load(f)
    except: return "INITIALIZING QUANT TERMINAL..."
    
    asset_grid = ""
    for s, d in m['assets'].items():
        color = "var(--accent)" if "STRIKE" in d['action'] else ("#ff2d55" if d['action']=="SHIELDED" else "var(--dim)")
        sigma_percent = min(100, d['sigma'] * 100)
        
        asset_block = f"""
        <div class="stat-card" style="border-color:{color if "STRIKE" in d['action'] else 'var(--border)'}">
            <div class="label" style="display:flex; justify-content:space-between;">
                {s} <span style="color:var(--accent)">{d['leverage']}</span>
            </div>
            <div class="value">${d['price']:,.2f}</div>
            <div class="sub-value">Σ INTEGRITY: {d['sigma']:.4f}</div>
            <div class="sigma-meter">
                <div class="sigma-fill" style="width:{sigma_percent}%; background:{color}"></div>
            </div>
            <div class="action-badge" style="color:{color}; border-color:{color}">{d['action']}</div>
        </div>"""
        asset_grid += asset_block

    return f"""<!DOCTYPE html><html><head><title>YNOR ZENITH</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;700;900&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/static/quant_terminal.css">
    <script>setTimeout(() => location.reload(), 5000);</script></head>
    <body>
    <div class="terminal-header">
        <span class="live-dot"></span> {m['shield']} | ZENITH v16.5 SOUVERAIN
    </div>
    <div class="balance-panel stat-card">
        <div class="label">SOVEREIGN EQUITY</div>
        <div class="value">${m['balance']:,.2f}</div>
        <div class="sub-value" style="color:var(--accent)">SYNC: {m['timestamp']}</div>
    </div>
    <div class="monolith-grid">{asset_grid}</div>
    </body></html>"""

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
