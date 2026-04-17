import yfinance as yf
from ynor_engine import YnorScoringEngine, YnorBacktestEngine
import pandas as pd

def perform_btc_backtest():
    print("🚀 Initialisation du Backtest Souverain (30 jours, BTC/USD)...")
    
    # 1. Acquisition des données
    data = yf.download("BTC-USD", period="30d", interval="1h")
    
    # 2. Préparation de l'intelligence
    engine = YnorScoringEngine()
    backtester = YnorBacktestEngine(engine)
    
    # 3. Exécution
    results = backtester.run(data)
    
    # 4. Rapport
    print("\n--- RÉSULTATS DU BACKTEST ---")
    print(f"Solde Final : ${results['final_balance']:,.2f}")
    print(f"PnL Total    : {results['total_pnl_pct']:+.2f}%")
    print(f"Max Drawdown : {results['max_drawdown_pct']:.2f}%")
    print(f"Nombre de trades : {results['trades_count']}")
    print("------------------------------\n")

if __name__ == "__main__":
    perform_btc_backtest()
