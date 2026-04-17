# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur operatoire
# **Centre Doctrinal Local :** AI Manager garde moteur operatoire en limitant le bruit local et la friction structurelle.
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

import numpy as np

class YnorCorrelationEngine:
    def __init__(self):
        self.macro_assets = ["^GSPC", "GC=F"] # SP500 et Or

    def calculate_macro_drift(self, btc_history, macro_histories):
        """
        Détermine si le Bitcoin est en retard ou en avance sur la Macro.
        """
        try:
            btc_returns = np.diff(btc_history) / btc_history[:-1]
            drift_score = 0.0
            
            for asset, hist in macro_histories.items():
                asset_returns = np.diff(hist) / hist[:-1]
                # Corrélation de Pearson simplifiée
                corr = np.corrcoef(btc_returns[-10:], asset_returns[-10:])[0, 1]
                
                # Si l'indice monte et que le BTC stagne (Divergence Bullish)
                if asset == "^GSPC" and np.mean(asset_returns[-3:]) > 0 and np.mean(btc_returns[-3:]) < 0:
                    drift_score += 1.5
                    
            return round(max(-2.0, min(2.0, drift_score)), 2)
        except:
            return 0.0
