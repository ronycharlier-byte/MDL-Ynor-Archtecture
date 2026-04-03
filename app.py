from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import sys
import json
import numpy as np
import traceback
from typing import Optional, Any
from datetime import datetime

# MDL YNOR ELITE STABILITY V11.10.11 - OMEGA MEMORY OPTIMIZATION
# FORCING LINUX COMPATIBILITY (LF ONLY)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
NEXUS_PATH = os.path.join(BASE_DIR, "YNOR_MARKET_DYNAMICS_NEXUS")
if NEXUS_PATH not in sys.path:
    sys.path.append(NEXUS_PATH)

IMPORT_ERROR = None
YNOR_MARKET_NEXUS = None
INDEX_MATRIX = None
INDEX_TEXTS = None

# FONCTION DE CHARGEMENT À LA DEMANDE (ANTI-STATUS 2)
def load_market():
    global YNOR_MARKET_NEXUS, IMPORT_ERROR
    if YNOR_MARKET_NEXUS is None:
        try:
            from ynor_market_bridge import YNOR_MARKET_NEXUS as nexus_instance
            YNOR_MARKET_NEXUS = nexus_instance
        except Exception:
            IMPORT_ERROR = traceback.format_exc()

def load_index():
    global INDEX_MATRIX, INDEX_TEXTS, IMPORT_ERROR
    if INDEX_MATRIX is None:
        VECT_PATH = os.path.join(BASE_DIR, "index_vectors.npy")
        META_PATH = os.path.join(BASE_DIR, "index_meta.json")
        try:
            if os.path.exists(VECT_PATH):
                INDEX_MATRIX = np.load(VECT_PATH, mmap_mode='r')
            if os.path.exists(META_PATH):
                with open(META_PATH, "r", encoding="utf-8") as f:
                    INDEX_TEXTS = json.load(f)
        except Exception as e:
            IMPORT_ERROR = (IMPORT_ERROR or "") + "\nErreur Corpus: " + str(e)

app = FastAPI(title="MDL YNOR ELITE V11.10.11", version="11.10.11")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "LIVE", 
        "mu": 1.0, 
        "message": "MDL Ynor Elite V11.10.11 (On-Demand Loading Active).",
        "timestamp": datetime.now().isoformat()
    }

class DispatchRequest(BaseModel):
    action: str
    payload: Any
    license_key: str

@app.post("/dispatch")
async def dispatch(request: DispatchRequest):
    valid_keys = ["MDL-SINGULARITY-2026-V11.8-OMEGA-BRIDGE", "MDL-SINGULARITY-2026-V11.5-OMEGA-BRIDGE"]
    if request.license_key not in valid_keys:
        return JSONResponse(status_code=403, content={"status": "ERROR", "message": "Licence Invalide."})

    action = request.action.lower()
    user_payload = str(request.payload)

    # ACTIONS MARKET (CHARGEMENT À LA DEMANDE)
    if "market" in action:
        load_market()
        if not YNOR_MARKET_NEXUS:
            return {"status": "ERROR", "projection": IMPORT_ERROR, "message": "Échec chargement Nexus."}
        try:
            symbol = user_payload.strip().upper().split()[0]
            return await YNOR_MARKET_NEXUS.process_market_query(symbol)
        except Exception as e:
            return {"status": "ERROR", "projection": str(e)}

    # ACTIONS LOGOS (CHARGEMENT À LA DEMANDE)
    if "logos" in action:
        load_index()
        return {
            "status": "SUCCESS", 
            "mu": 1.0, 
            "vectors": len(INDEX_TEXTS) if INDEX_TEXTS else 0,
            "message": "Logos Inference Ready."
        }

    return {"status": "SUCCESS", "mu": 1.0, "message": f"Action {action} acquittée."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
