import os
from dotenv import load_dotenv

load_dotenv()

# --- REGLAGE DE SOUVERAINETE ---
SAFE_MODE = True # SI TRUE -> AUCUN ORDRE REEL

# --- VARIABLES D'ENVIRONNEMENT ---
BITGET_API_KEY = os.getenv("BITGET_API_KEY", "")
BITGET_SECRET = os.getenv("BITGET_SECRET", "")
BITGET_PASSPHRASE = os.getenv("BITGET_PASSPHRASE", "")

MODE = os.getenv("MODE", "production")
CAPITAL = float(os.getenv("CAPITAL", "1.0"))

# --- SEUILS V1.6.1 ---
S_CRIT = 0.4
TAU = 2700 # 45 min
MIN_PI_NORM = 0.08
DELTA_OOD = 0.5
