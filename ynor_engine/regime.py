import yfinance as yf
import numpy as np

class YnorMarketRegime:
    def __init__(self):
        pass

    def detect(self, symbol="BTC-USD"):
        """
        Détection du régime de marché basé sur les 24 dernières heures.
        🎯 BULL, BEAR, RANGE, VOLATILE
        """
        try:
            # On récupère les données intraday (5 min interval)
            data = yf.download(symbol, period="1d", interval="5m", progress=False)
            
            if data.empty:
                return "UNKNOWN"

            # 1. Calcul de la tendance (Variation Price Start/End)
            start_price = data["Close"].iloc[0]
            end_price = data["Close"].iloc[-1]
            trend_pct = (end_price - start_price) / start_price

            # 2. Calcul de la volatilité (Ecart-type des rendements)
            returns = data["Close"].pct_change().dropna()
            volatility = returns.std()

            # --- LOGIC DE CLASSIFICATION ---
            # Seuil de volatilité critique (instabilité)
            if volatility > 0.005: # Environ 0.5% d'écart standard par 5min
                return "VOLATILE"

            # Marché neutre / Latéralisation
            if abs(trend_pct) < 0.005: # Moins de 0.5% de variation sur 24h
                return "RANGE"

            # Directionnel
            if trend_pct >= 0.005:
                return "BULL"
            
            return "BEAR"

        except Exception as e:
            return "UNKNOWN"
