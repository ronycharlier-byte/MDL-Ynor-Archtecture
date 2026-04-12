from execution.bitget_api import BitgetAPI
from config.settings import CAPITAL

class OrderManager:
    """
    Gere l'execution et le suivi des positions.
    """
    def __init__(self, api: BitgetAPI):
        self.api = api
        self.active_position = None

    async def execute_trade(self, decision):
        """ Transforme une decision pi_s en ordre reel """
        if decision["action"] is None:
            return None

        # Calcul direction
        side = "long" if decision["pi_s"][0] > 0 else "short"
        # Calcul taille
        amount = decision["size"] * CAPITAL 
        
        success = await self.api.place_order("BTCUSDT", side, amount)
        if success:
            self.active_position = {"side": side, "amount": amount}
            return success
        return False
