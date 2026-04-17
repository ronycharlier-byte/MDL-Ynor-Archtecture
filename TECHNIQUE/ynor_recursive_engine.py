# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
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

import json
import os

class YnorRecursiveEngine:
    def __init__(self, config_path="data/dynamic_config.json"):
        self.config_path = config_path
        self.default_config = {"riemann_threshold": 0.85, "alpha_weight": 1.0}
        self.load_config()

    def load_config(self):
        if os.path.exists(self.config_path):
            with open(self.config_path, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = self.default_config
            self.save_config()

    def save_config(self):
        with open(self.config_path, 'w') as f:
            json.dump(self.config, f, indent=4)

    def evolve(self, recent_trades):
        """
        Analyse les trades passés pour ajuster la sensibilité du bot.
        """
        if not recent_trades: return
        
        # Calcul du Win Rate réel depuis la DB
        wins = sum(1 for t in recent_trades if t.get('pnl', 0) > 0)
        win_rate = wins / len(recent_trades)
        
        print(f"[RECURSIVE] Analyzing {len(recent_trades)} trades. Win Rate: {win_rate:.2%}")
        
        # LOGIQUE D'ÉVOLUTION
        if win_rate < 0.50:
            # On devient plus sélcetif
            self.config["riemann_threshold"] = min(0.98, self.config["riemann_threshold"] + 0.02)
            print(f"[RECURSIVE] Win Rate too low. Increasing Selection Threshold to {self.config['riemann_threshold']}")
        elif win_rate > 0.75:
            # On s'autorise plus de liberté car le modèle est chaud
            self.config["riemann_threshold"] = max(0.80, self.config["riemann_threshold"] - 0.01)
            print(f"[RECURSIVE] High Performance detected. Lowering Threshold to {self.config['riemann_threshold']}")
            
        self.save_config()
