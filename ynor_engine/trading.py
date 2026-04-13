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
        self.last_call = 0
        self.cooldown = 1.0 

    def _sign(self, timestamp, method, path, body=""):
        message = f"{timestamp}{method}{path}{body}"
        mac = hmac.new(self.secret.encode() if self.secret else b"", message.encode(), digestmod="sha256")
        return base64.b64encode(mac.digest()).decode()

    def _headers(self, method, path, body=""):
        timestamp = str(int(time.time() * 1000))
        sign = self._sign(timestamp, method, path, body)
        return {"ACCESS-KEY": self.api_key or "", "ACCESS-SIGN": sign, "ACCESS-TIMESTAMP": timestamp, "ACCESS-PASSPHRASE": self.passphrase or "", "Content-Type": "application/json"}

    def _safe_request(self, method, path, body=None, retries=3):
        elapsed = time.time() - self.last_call
        if elapsed < self.cooldown: time.sleep(self.cooldown - elapsed)
        delay = 2
        for i in range(retries):
            try:
                self.last_call = time.time()
                url = self.base_url + path
                if method == "GET": res = requests.get(url, headers=self._headers("GET", path))
                else:
                    body_str = str(body).replace("'", '"').replace(" ", "")
                    res = requests.post(url, headers=self._headers("POST", path, body_str), json=body)
                data = res.json()
                if data.get("code") == "429" or "rate limit" in str(data).lower():
                    time.sleep(delay); delay *= 2; continue
                return data
            except: time.sleep(delay); delay *= 2
        return {"code": "error"}

    def get_balance(self):
        path = "/api/v2/mix/account/accounts?productType=USDT-FUTURES"
        data = self._safe_request("GET", path)
        if data.get("code") == "00000" and data.get("data"):
            return float(data["data"][0].get("available", 0.0))
        return None

    def place_order(self, symbol="BTCUSDT", side="buy", size="0.001"):
        path = "/api/v2/mix/order/place-order"
        body = {"symbol": symbol, "marginCoin": "USDT", "size": str(size), "side": side, "orderType": "market", "productType": "USDT-FUTURES"}
        return self._safe_request("POST", path, body)

class MillenniumGrandSolver:
    def __init__(self, initial_balance=1000):
        self.initial_balance = initial_balance

    def compute_indicators(self, df):
        if len(df) < 20: return df
        df = df.copy()
        df["ema"] = df["Close"].ewm(span=20).mean()
        # Volatility normalization (0 - 1) sur une fenêtre de 20
        df["std"] = df["Close"].pct_change().rolling(20).std()
        df["volatility_norm"] = (df["std"] - df["std"].rolling(100).min()) / (df["std"].rolling(100).max() - df["std"].rolling(100).min())
        return df

    def compute_score(self, sentiment, trend, volatility):
        """ Signal Engine V1 : Multi-Factor Scoring """
        score = 50 
        
        # 1. SENTIMENT (30%) - Normalisé -1 à +1
        score += (sentiment * 30)
        
        # 2. TREND (40%)
        if trend == "bullish": score += 25
        elif trend == "bearish": score -= 25
        
        # 3. VOLATILITY (20%) - 0: calme, 1: tempête
        if volatility < 0.3: score += 10
        elif volatility > 0.7: score -= 15
        
        # 4. REGIME BONUS
        if trend == "bullish" and sentiment > 0.5: score += 10
        elif trend == "bearish" and sentiment < -0.5: score -= 10
        
        return max(0, min(100, score))

    def decide(self, score):
        """ Échelles de décision nuancées """
        if score >= 80: return "STRONG_BUY"
        elif score >= 65: return "BUY"
        elif score <= 20: return "STRONG_SELL"
        elif score <= 35: return "SELL"
        return "HOLD"

    def compute_position_size(self, balance, score, price):
        if balance is None or balance <= 0: balance = 1000.0
        base_risk = 0.01 * balance
        confidence = score / 100.0
        # Multiplicateur de conviction
        if score >= 80: confidence *= 1.5
        return round((base_risk * confidence) / price, 4)
