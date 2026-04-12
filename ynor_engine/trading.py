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
        self.api_secret = os.getenv("BITGET_SECRET")
        self.passphrase = os.getenv("BITGET_PASSPHRASE")
        self.base_url = "https://api.bitget.com"

    def _sign(self, message):
        if not self.api_secret: return ""
        return base64.b64encode(
            hmac.new(self.api_secret.encode(), message.encode(), sha256).digest()
        ).decode()

    def get_balance(self, coin="USDT"):
        timestamp = str(int(time.time() * 1000))
        request_path = f"/api/v2/mix/account/account?symbol=BTCUSDT&marginCoin={coin}"
        message = timestamp + "GET" + request_path
        signature = self._sign(message)
        headers = {
            "ACCESS-KEY": self.api_key or "",
            "ACCESS-SIGN": signature,
            "ACCESS-TIMESTAMP": timestamp,
            "ACCESS-PASSPHRASE": self.passphrase or "",
            "Content-Type": "application/json"
        }
        try:
            res = requests.get(self.base_url + request_path, headers=headers)
            data = res.json()
            return float(data.get("data", [{}])[0].get("available", 100.0))
        except:
            return 100.0

    def place_order(self, symbol="BTCUSDT", side="buy", size="0.001"):
        timestamp = str(int(time.time() * 1000))
        body = {
            "symbol": symbol,
            "marginCoin": "USDT",
            "size": str(size),
            "side": side,
            "orderType": "market"
        }
        request_path = "/api/v2/mix/order/place-order" # Updated to V2
        message = timestamp + "POST" + request_path + str(body)
        signature = self._sign(message)
        headers = {
            "ACCESS-KEY": self.api_key or "",
            "ACCESS-SIGN": signature,
            "ACCESS-TIMESTAMP": timestamp,
            "ACCESS-PASSPHRASE": self.passphrase or "",
            "Content-Type": "application/json"
        }
        try:
            response = requests.post(self.base_url + request_path, headers=headers, json=body)
            logger.info(f"ORDER SENT | {side} {size} {symbol} | Response: {response.status_code}")
            return response.json()
        except Exception as e:
            logger.error(f"ORDER FAILED | {e}")
            return {"status": "error", "message": str(e)}

class MillenniumGrandSolver:
    def __init__(self, initial_balance=1000):
        self.initial_balance = initial_balance
        self.stop_trading = False

    def compute_score(self, sentiment, trend, volatility):
        """ Score Intelligent (0.0 -> 1.0) """
        score = 0
        score += sentiment * 40 # Sentiment (0 -> 1)
        
        if trend == "bullish": score += 30
        elif trend == "bearish": score += 30
        
        if volatility < 0.02: score += 30
        elif volatility > 0.05: score -= 20
        
        return score / 100

    def market_filter(self, volatility, trend):
        """ Filtre Sécurité Marché """
        if volatility > 0.05: return False
        if trend == "unclear": return False
        return True

    def compute_position_size(self, balance):
        return balance * 0.01 # 1% Risk

    def compute_drawdown(self, current_balance):
        if self.initial_balance <= 0: return 0
        return (self.initial_balance - current_balance) / self.initial_balance

    def kill_switch(self, drawdown):
        if drawdown > 0.1:
            logger.warning("🚨 KILL SWITCH ACTIVATED")
            self.stop_trading = True
            return True
        return False
