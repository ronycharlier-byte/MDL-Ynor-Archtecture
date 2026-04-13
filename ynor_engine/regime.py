import numpy as np

class YnorMarketRegime:
    def detect(self, df):
        """ Détection du régime de marché (Bull, Bear, Range) """
        if len(df) < 50: return "range"
        
        price = df["Close"]
        
        # Trend via EMA crossovers
        ema_fast = price.ewm(span=20).mean()
        ema_slow = price.ewm(span=50).mean()
        
        # Volatility index
        volatility = price.pct_change().rolling(10).std().iloc[-1]
        
        # Trend strength (relative difference)
        trend_strength = (ema_fast.iloc[-1] - ema_slow.iloc[-1]) / ema_slow.iloc[-1]
        
        # --- LOGIQUE DÉCISIONNELLE ---
        if trend_strength > 0.02:
            return "bull"
        elif trend_strength < -0.02:
            return "bear"
        else:
            # Sécurité anti-chop
            if volatility > 0.04: return "range" # "High Vol Range" -> Prudence
            return "range"
