import os
import time
import hmac
import base64
import requests
import logging
import numpy as np
from hashlib import sha256

# --- CONFIG LOGGING ---
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("YNOR_TRADING")

class YnorBitgetConnector:
    def __init__(self):
        self.api_key = os.getenv("BITGET_API_KEY")
        self.secret = os.getenv("BITGET_SECRET")
        self.passphrase = os.getenv("BITGET_PASSPHRASE")
        self.base_url = "https://api.bitget.com"

    def _sign(self, timestamp, method, path, body=""):
        message = f"{timestamp}{method}{path}{body}"
        mac = hmac.new(
            self.secret.encode() if self.secret else b"",
            message.encode(),
            digestmod="sha256"
        )
        return base64.b64encode(mac.digest()).decode()

    def _headers(self, method, path, body=""):
        timestamp = str(int(time.time() * 1000))
        sign = self._sign(timestamp, method, path, body)
        return {
            "ACCESS-KEY": self.api_key or "",
            "ACCESS-SIGN": sign,
            "ACCESS-TIMESTAMP": timestamp,
            "ACCESS-PASSPHRASE": self.passphrase or "",
            "Content-Type": "application/json"
        }

    def get_balance(self):
        path = "/api/v2/mix/account/accounts?productType=USDT-FUTURES"
        url = self.base_url + path
        try:
            res = requests.get(url, headers=self._headers("GET", path))
            data = res.json()
            if data.get("code") == "00000" and data.get("data"):
                return float(data["data"][0].get("available", 0.0))
            return 1000.0 # Mock for local if keys fail
        except:
            return 1000.0

    def place_order(self, symbol="BTCUSDT", side="buy", size="0.001"):
        path = "/api/v2/mix/order/place-order"
        url = self.base_url + path
        body = {
            "symbol": symbol,
            "marginCoin": "USDT",
            "size": str(size),
            "side": side,
            "orderType": "market",
            "productType": "USDT-FUTURES"
        }
        body_str = str(body).replace("'", '"').replace(" ", "")
        headers = self._headers("POST", path, body_str)
        try:
            response = requests.post(url, headers=headers, json=body)
            return response.json()
        except Exception as e:
            return {"code": "error", "message": str(e)}

class YnorScoringEngine:
    def compute_score(self, prices, sentiment):
        """ Multi-Factor Scoring Engine V3 """
        if len(prices) < 20: return 50 # Neutre si pas assez de data
        
        score = 0
        prices = np.array(prices)

        # --- TREND (EMA) ---
        ema_fast = np.mean(prices[-5:])
        ema_slow = np.mean(prices[-20:])
        if ema_fast > ema_slow: score += 30
        else: score -= 30

        # --- MOMENTUM (RSI) ---
        gains = [max(0, prices[i] - prices[i-1]) for i in range(1, len(prices))]
        losses = [max(0, prices[i-1] - prices[i]) for i in range(1, len(prices))]
        avg_gain = np.mean(gains[-14:]) if gains else 0
        avg_loss = np.mean(losses[-14:]) if losses else 1
        rs = avg_gain / avg_loss if avg_loss != 0 else 0
        rsi = 100 - (100 / (1 + rs))

        if rsi < 30: score += 20
        elif rsi > 70: score -= 20

        # --- VOLATILITY FILTER ---
        volatility = np.std(prices[-20:])
        if volatility > np.mean(prices) * 0.02:
            return 0 # Trop dangereux

        # --- SENTIMENT (Alpha) ---
        score += (sentiment * 50) # sentiment -1.0 to 1.0

        return max(0, min(100, score))

class MillenniumGrandSolver: # Legacy support
    def __init__(self, initial_balance=1000):
        self.initial_initial = initial_balance
    def compute_position_size(self, balance):
        return balance * 0.01
