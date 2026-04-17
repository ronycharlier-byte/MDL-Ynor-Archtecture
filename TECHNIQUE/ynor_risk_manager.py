# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Gestion du risque
# **Centre Doctrinal Local :** AI Manager garde gestion du risque en limitant le bruit local et la friction structurelle.
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

class YnorRiskManager:
    def __init__(self, risk_per_trade=0.02, max_drawdown=0.05):
        self.risk_per_trade = risk_per_trade  # 2% max par trade
        self.max_drawdown = max_drawdown      # 5% max par jour
        self.daily_pnl = 0.0
        self.safety_lock = False

    def calculate_position_size(self, balance, price, volatility):
        """
        Calcule la taille de position idéale en fonction de l'équité
        et de la volatilité du marché.
        """
        if self.safety_lock: return 0.0
        
        # Formule simplifiée : on adapte l'exposition au capital
        cash_risk = balance * self.risk_per_trade
        amount = cash_risk / (price * volatility if volatility > 0 else price * 0.02)
        
        return round(amount, 6)

    def check_safety(self, current_pnl):
        """
        Vérifie si le drawdown quotidien a été atteint.
        """
        if current_pnl <= -self.max_drawdown:
            self.safety_lock = True
            print("[RISK] SAFETY LOCK ACTIVATED (MAX DRAWDOWN REACHED)")
            return False
        return True

    def get_stop_loss(self, entry_price, side, volatility):
        offset = entry_price * (volatility * 2 if volatility > 0 else 0.02)
        if side == "buy": return round(entry_price - offset, 2)
        return round(entry_price + offset, 2)
