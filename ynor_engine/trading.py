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
        """ Récupération du solde réel pour Risk Management """
        timestamp = str(int(time.time() * 1000))
        request_path = f"/api/mix/v1/account/account?symbol=BTCUSDT&marginCoin={coin}"
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
            # Parsing simplifié du solde disponible
            return float(data.get("data", {}).get("available", 0.0))
        except:
            return 0.0

    def place_order(self, symbol="BTCUSDT", side="buy", size="0.001"):
        timestamp = str(int(time.time() * 1000))
        body = {
            "symbol": symbol,
            "marginCoin": "USDT",
            "size": str(size),
            "side": side,
            "orderType": "market"
        }
        request_path = "/api/mix/v1/order/placeOrder"
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
    def __init__(self):
        self.stop_trading = False
        self.initial_balance = None

    def check_kill_switch(self, current_balance):
        if self.initial_balance is None:
            self.initial_balance = current_balance
            return False
        
        if self.initial_balance > 0:
            drawdown = (self.initial_balance - current_balance) / self.initial_balance
            if drawdown > 0.10: # 10% Kill Switch
                logger.warning(f"🛑 KILL SWITCH TRIGGERED | Drawdown: {drawdown:.2%}")
                self.stop_trading = True
                return True
        return False

    def compute_position_size(self, balance, price, risk_pct=0.01):
        """ Risk Management: 1% du capital par trade """
        if balance <= 0: return 0
        position_value = balance * risk_pct
        return round(position_value / price, 3)

    def decide(self, sentiment_score, price_data=None):
        if self.stop_trading: return "hold"
        
        # Logique augmentée : Sentiment + Momentum Basique
        if sentiment_score > 0.75:
            return "buy"
        elif sentiment_score < 0.25:
            return "sell"
        return "hold"
