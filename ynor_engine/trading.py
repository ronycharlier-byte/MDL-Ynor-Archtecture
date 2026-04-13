import os
import time
import hmac
import base64
import requests
import logging
import numpy as np
import pandas as pd
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
        mac = hmac.new(self.secret.encode() if self.secret else b"", message.encode(), digestmod="sha256")
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
        except: return {"code": "error"}

class MillenniumGrandSolver:
    def __init__(self, initial_balance=1000):
        self.initial_balance = initial_balance
        self.current_balance = initial_balance

    def compute_indicators(self, df):
        """ Calcul des indicateurs de base """
        if len(df) < 20: return df
        df = df.copy()
        df["ema"] = df["Close"].ewm(span=20).mean()
        df["volatility"] = df["Close"].pct_change().rolling(10).std()
        return df

    def compute_score(self, sentiment, trend, volatility):
        """ Source de Vérité Unique pour le Scoring """
        score = 50 # Base neutre
        
        # Sentiment Alpha
        if sentiment > 0.5: score += 15
        elif sentiment < 0.4: score -= 15
        
        # Trend Alpha
        if trend == "bullish": score += 20
        elif trend == "bearish": score -= 20
        
        # Volatility Filter
        if volatility < 0.05: score += 10
        else: score -= 10
        
        return max(0, min(100, score))

    def decide(self, score):
        if score > 70: return "BUY"
        elif score < 30: return "SELL"
        return "HOLD"

    def compute_position_size(self, balance, score, price):
        if balance is None or balance <= 0: balance = 1000.0
        base_risk = 0.01
        confidence = score / 100.0
        return round((balance * base_risk * confidence) / price, 4)
