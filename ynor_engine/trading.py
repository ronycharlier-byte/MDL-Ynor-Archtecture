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
        return {"ACCESS-KEY": self.api_key or "", "ACCESS-SIGN": sign, "ACCESS-TIMESTAMP": timestamp, "ACCESS-PASSPHRASE": self.passphrase or "", "Content-Type": "application/json"}

    def get_balance(self):
        path = "/api/v2/mix/account/accounts?productType=USDT-FUTURES"
        try:
            res = requests.get(self.base_url + path, headers=self._headers("GET", path))
            data = res.json()
            if data.get("code") == "00000" and data.get("data"):
                return float(data["data"][0].get("available", 0.0))
            return 1000.0
        except: return 1000.0

    def place_order(self, symbol="BTCUSDT", side="buy", size="0.001"):
        path = "/api/v2/mix/order/place-order"
        body = {"symbol": symbol, "marginCoin": "USDT", "size": str(size), "side": side, "orderType": "market", "productType": "USDT-FUTURES"}
        body_str = str(body).replace("'", '"').replace(" ", "")
        headers = self._headers("POST", path, body_str)
        try:
            res = requests.post(self.base_url + path, headers=headers, json=body)
            return res.json()
        except Exception as e: return {"code": "error", "message": str(e)}

class YnorScoringEngine:
    def detect_market_regime(self, prices):
        """ Detection du Regime de Marche """
        if len(prices) < 20: return "UNKNOWN"
        p = np.array(prices)
        volatility = np.std(p[-20:])
        trend = np.mean(p[-5:]) - np.mean(p[-20:])
        avg_price = np.mean(p)

        if volatility > avg_price * 0.03: return "HIGH_VOL"
        if abs(trend) < avg_price * 0.005: return "RANGE"
        return "TREND"

    def compute_score(self, prices, sentiment):
        if len(prices) < 20: return 50
        p = np.array(prices)
        score = 0
        
        # --- FACTEURS ---
        # 1. EMA Trend
        ema_f, ema_s = np.mean(p[-5:]), np.mean(p[-20:])
        score += 30 if ema_f > ema_s else -30
        
        # 2. RSI Momentum
        diff = np.diff(p)
        gain = np.mean([max(0, x) for x in diff[-14:]])
        loss = np.mean([max(0, -x) for x in diff[-14:]])
        rsi = 100 - (100 / (1 + gain/loss)) if loss > 0 else 100
        if rsi < 30: score += 20
        elif rsi > 70: score -= 20

        # --- ADAPTATION STRATEGIQUE ---
        regime = self.detect_market_regime(prices)
        if regime == "HIGH_VOL": score *= 0.5
        elif regime == "RANGE": score *= 0.7
        elif regime == "TREND": score *= 1.2
        
        # --- SENTIMENT ---
        score += (sentiment * 50)
        
        return max(0, min(100, score))

    def compute_position_size(self, balance, score, price):
        """ Allocation Intelligente """
        base_risk = 0.01
        multiplier = score / 100.0
        pos_val = balance * base_risk * multiplier
        return round(pos_val / price, 4)
