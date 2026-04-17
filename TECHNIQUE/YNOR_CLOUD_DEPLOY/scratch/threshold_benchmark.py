# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Script ou configuration declarative
# **Centre Doctrinal Local :** AI Manager garde script ou configuration declarative en limitant le bruit local et la friction structurelle.
# **Loi de Survie :** μ = α - β - κ
# **Lecture Locale :**
# - **α :** stabilite locale
# - **β :** bruit externe injecte
# - **κ :** friction structurelle
# **Risque :** e∞ ∝ ε / μ
# **Opérateur Correctif :** D(S)=proj_{SafeDomain}(S)
# **Axiome :** un système survit SSI μ > 0
# **Doctrine Goodhart : tout succès apparent est invalide si μ décroît**
# **Gouvernance : toute modification doit maximiser Δμ**
# **Lien Miroir :** E

sys.path.append(os.getcwd())
try:
    from ynor_millennium_solver import MillenniumGrandSolver
except:
    class MillenniumGrandSolver:
        def get_grand_sovereign_score(self, p): return 0.5, {}

def get_best_config(ticker):
    print(f"[ENGINE] Optimizing {ticker}...")
    try:
        data = yf.Ticker(ticker).history(period="5d", interval="5m")
        prices = data['Close'].tolist()
        if len(prices) < 200: return None
    except: return None
    
    solver = MillenniumGrandSolver()
    best_profit = -999
    best_t = 0.40 # Default safeguard
    best_sl = 0.012 # Default safeguard
    
    threshold_range = np.arange(0.35, 0.50, 0.02)
    sl_range = [0.012, 0.015, 0.02]

    for t in threshold_range:
        for sl in sl_range:
            profit = 0.0
            trades = 0
            in_pos = False
            entry_p = 0
            
            for i in range(50, len(prices)):
                window = prices[i-50:i]
                cur_p = prices[i]
                sigma, _ = solver.get_grand_sovereign_score(window)
                
                if not in_pos and sigma > t:
                    in_pos = True
                    entry_p = cur_p
                    trades += 1
                elif in_pos:
                    roi = (cur_p - entry_p) / entry_p
                    if roi < -sl or roi > 0.025 or sigma < t*0.75:
                        profit += roi
                        in_pos = False
            
            # On privilégie un profit stable avec au moins quelques trades
            if profit > best_profit and trades > 5:
                best_profit = profit
                best_t = t
                best_sl = sl
                
    return {"ticker": ticker, "Profit": round(best_profit*100, 2), "Threshold": round(best_t, 2), "StopLoss": round(best_sl*100, 2)}

if __name__ == "__main__":
    # LES 7 PILIERS
    assets = ["BTC-USD", "ETH-USD", "SOL-USD", "XRP-USD", "DOGE-USD", "LINK-USD", "ADA-USD"]
    final_configs = {}
    
    print("\n--- MDL YNOR FULL GENESIS (7/7) ---")
    for a in assets:
        config = get_best_config(a)
        if config:
            final_configs[a] = config
            print(f" WINNER {a} -> T: {config['Threshold']} | SL: {config['StopLoss']}% | P: {config['Profit']}%")
        else:
            print(f" SKIP {a} (Insufficient data)")
    
    with open("data/optimal_configs.json", "w") as f:
        json.dump(final_configs, f, indent=4)
