import yfinance as yf
import numpy as np
import pandas as pd

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
            
            # RÈGLE D'OR : Jamais d'UNKNOWN en prod -> Fallback RANGE
            if data is None or data.empty or len(data) < 2:
                return "RANGE"

            # Sécurisation des colonnes (extraction scalaire propre)
            prices = data["Close"]
            if isinstance(prices, pd.DataFrame):
                prices = prices.iloc[:, 0]
            
            start_price = float(prices.iloc[0])
            end_price = float(prices.iloc[-1])
            trend_pct = (end_price - start_price) / start_price if start_price != 0 else 0

            # 2. Calcul de la volatilité (Ecart-type des rendements)
            returns = prices.pct_change().dropna()
            volatility = float(returns.std())

            # --- LOGIC DE CLASSIFICATION ---
            if volatility > 0.005: 
                return "VOLATILE"

            if abs(trend_pct) < 0.003: # Plus strict pour le range
                return "RANGE"

            if trend_pct >= 0.003:
                return "BULL"
            
            return "BEAR"

        except Exception:
            return "RANGE" # Fallback sécurisé
