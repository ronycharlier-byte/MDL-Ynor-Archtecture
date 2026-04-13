import os
import time
import hmac
import base64
import requests
import logging
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
        """ Récupération du solde disponible (API V2) """
        path = "/api/v2/mix/account/accounts?productType=USDT-FUTURES"
        url = self.base_url + path
        try:
            res = requests.get(url, headers=self._headers("GET", path))
            data = res.json()
            # On cherche le solde disponible dans la liste des comptes
            if data.get("code") == "00000" and data.get("data"):
                # On prend le premier compte (USDT par défaut)
                return float(data["data"][0].get("available", 0.0))
            return None
        except Exception as e:
            logger.error(f"Balance fetch failed: {e}")
            return None

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
        body_str = str(body).replace("'", '"').replace(" ", "") # standard JSON string formatting
        
        headers = self._headers("POST", path, body_str)
        try:
            response = requests.post(url, headers=headers, json=body)
            return response.json()
        except Exception as e:
            return {"code": "error", "message": str(e)}

class MillenniumGrandSolver:
    def __init__(self, initial_balance=1000):
        self.initial_balance = initial_balance
        self.stop_trading = False

    def compute_score(self, sentiment, trend, volatility):
        score = (sentiment * 40)
        if trend == "bullish": score += 30
        if volatility < 0.02: score += 30
        return score / 100

    def compute_position_size(self, balance):
        return balance * 0.01

    def market_filter(self, volatility, trend):
        return volatility < 0.05 and trend != "unclear"
