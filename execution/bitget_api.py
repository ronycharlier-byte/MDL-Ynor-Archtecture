import os
import time
import requests
from config.settings import BITGET_API_KEY, BITGET_SECRET, BITGET_PASSPHRASE, SAFE_MODE

class BitgetAPI:
    """
    Interface simplifiee avec l'API Bitget.
    Gere le SAFE_MODE pour empecher les ordres reels.
    """
    def __init__(self):
        self.api_key = BITGET_API_KEY
        self.secret = BITGET_SECRET
        self.passphrase = BITGET_PASSPHRASE

    async def fetch_market_snapshot(self):
        """ Recupere les donnees temps-reel (Mock) """
        # Simulation d'acquisition
        return {"price": 65000.0, "timestamp": time.time()}

    async def place_order(self, symbol, side, amount, leverage=1):
        """ Place un ordre (Bloque par SAFE_MODE) """
        if SAFE_MODE:
            print(f"🛡️ [SAFE_MODE] Simulation d'ordre : {side} {amount} sur {symbol}")
            return True # Succes simule
        
        # Logique reelle ici (utilisant requests et signature)
        # return self._execute_real_order(...)
        print("❌ [EXECUTION] Ordre reel bloque : SAFE_MODE non desactive.")
        return False
