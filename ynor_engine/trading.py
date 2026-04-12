import os
import time
import hmac
import base64
import requests
from hashlib import sha256

class YnorBitgetConnector:
    def __init__(self):
        self.api_key = os.getenv("BITGET_API_KEY")
        self.api_secret = os.getenv("BITGET_SECRET")
        self.passphrase = os.getenv("BITGET_PASSPHRASE")
        self.base_url = "https://api.bitget.com"

    def _sign(self, message):
        return base64.b64encode(
            hmac.new(self.api_secret.encode() if self.api_secret else b"", message.encode(), sha256).digest()
        ).decode()

    def place_order(self, symbol="BTCUSDT", side="buy", size="0.001"):
        timestamp = str(int(time.time() * 1000))
        body = {
            "symbol": symbol,
            "marginCoin": "USDT",
            "size": size,
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
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

class MillenniumGrandSolver:
    def __init__(self):
        pass

    def decide(self, sentiment_score):
        if sentiment_score > 0.7:
            return "buy"
        elif sentiment_score < 0.3:
            return "sell"
        return "hold"
