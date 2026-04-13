import pandas as pd
import numpy as np
import logging

class YnorBacktestEngine:
    def __init__(self, engine, initial_balance=1000, fee=0.0006):
        """
        engine: L'instance de YnorScoringEngine
        fee: Commission moyenne par trade (Taker fee Bitget ~0.06%)
        """
        self.engine = engine
        self.initial_balance = initial_balance
        self.fee = fee

    def run(self, data):
        """ 
        Exécute la simulation sur un DataFrame (doit contenir 'Close') 
        """
        balance = self.initial_balance
        position = None
        entry_price = 0
        history = []
        trades = []
        
        # On commence à l'index 20 pour avoir assez de data pour les indicateurs (EMA20)
        for i in range(20, len(data)):
            # Extraction de la fenêtre glissante pour le Scoring Engine
            window = data['Close'].iloc[i-20:i+1].tolist()
            current_price = window[-1]
            
            # Sentiment simulé (virevolte autour de 0.5 par défaut)
            sentiment = data.get('sentiment', pd.Series([0.5]*len(data))).iloc[i]
            
            score = self.engine.compute_score(window, sentiment)
            
            # LOGIQUE DE TRADING
            # BUY (SIGNAL > 75)
            if score > 75 and position is None:
                position = "LONG"
                entry_price = current_price
                balance *= (1 - self.fee) # Paiement des frais à l'entrée
                trades.append({"type": "BUY", "price": entry_price, "time": data.index[i]})

            # SELL (SIGNAL < 25)
            elif score < 25 and position == "LONG":
                pnl = (current_price - entry_price) / entry_price
                balance *= (1 + pnl)
                balance *= (1 - self.fee) # Paiement des frais à la sortie
                position = None
                trades.append({"type": "SELL", "price": current_price, "pnl": pnl, "time": data.index[i]})

            history.append({"time": data.index[i], "balance": balance, "score": score})

        df_history = pd.DataFrame(history)
        
        # METRIQUES FINALES
        final_balance = balance
        total_pnl = (final_balance - self.initial_balance) / self.initial_balance
        max_drawdown = 0
        if not df_history.empty:
            peak = df_history['balance'].cummax()
            drawdown = (peak - df_history['balance']) / peak
            max_drawdown = drawdown.max()

        return {
            "final_balance": final_balance,
            "total_pnl_pct": total_pnl * 100,
            "max_drawdown_pct": max_drawdown * 100,
            "trades_count": len(trades),
            "history": df_history,
            "trades": trades
        }
