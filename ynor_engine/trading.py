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
        df["std"] = df["Close"].pct_change().rolling(20).std()
        df["volatility_norm"] = (df["std"] - df["std"].rolling(100).min()) / (df["std"].rolling(100).max() - df["std"].rolling(100).min())
        return df

    def detect_market_regime(self, trend, volatility):
        if trend == "bullish" and volatility < 0.5: return "bull"
        if trend == "bearish" and volatility < 0.5: return "bear"
        return "sideways"

    def adjust_score_by_regime(self, score, regime):
        if regime == "bull": score += 10
        elif regime == "bear": score -= 15
        elif regime == "sideways": score -= 5
        return max(0, min(100, score))

    def regime_filter(self, decision, regime):
        decision = decision.upper()
        regime = regime.lower()
        if regime == "bear" and decision in ["BUY", "STRONG_BUY"]: return "HOLD"
        if regime == "sideways" and decision != "STRONG_BUY"]: return "HOLD"
        return decision

    def compute_score(self, sentiment, trend, volatility):
        score = 50 
        score += (sentiment * 30)
        if trend == "bullish": score += 25
        elif trend == "bearish": score -= 25
        if volatility < 0.3: score += 10
        elif volatility > 0.7: score -= 15
        return max(0, min(100, score))

    def decide(self, score):
        if score >= 85: return "STRONG_BUY"
        elif score >= 65: return "BUY"
        elif score <= 20: return "STRONG_SELL"
        elif score <= 35: return "SELL"
        return "HOLD"

    def compute_allocation(self, scores):
        """ Allocation Optimizer : Répartition du risque par score """
        # On ne garde que les actifs avec un signal BUY/SELL
        active_scores = {k: v for k, v in scores.items() if v >= 65 or v <= 35}
        total = sum(active_scores.values())
        if total == 0: return {k: 0 for k in scores}
        return {k: v / total for k, v in active_scores.items()}

    def compute_position_size(self, balance, allocation, price, risk_per_trade=0.01):
        """ Position Sizing Séquentiel """
        # Capital à risquer pour cette opportunité spécifique
        opportunity_capital = balance * risk_per_trade * allocation
        return round(opportunity_capital / price, 4)
