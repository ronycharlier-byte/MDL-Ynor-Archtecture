# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Cartographie de liquidite
# **Centre Doctrinal Local :** AI Manager garde cartographie de liquidite en limitant le bruit local et la friction structurelle.
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

class YnorLiquidityScanner:
    def __init__(self, exchange_connector):
        self.exchange = exchange_connector

    def get_order_book_imbalance(self, symbol):
        """
        Analyse le carnet d'ordres pour détecter la pression acheteuse/vendeuse.
        """
        try:
            # Récupération des 20 meilleurs niveaux
            order_book = self.exchange.fetch_order_book(symbol, limit=20)
            bids = order_book['bids'] # Acheteurs
            asks = order_book['asks'] # Vendeurs
            
            total_buy_vol = sum([b[1] for b in bids])
            total_sell_vol = sum([a[1] for a in asks])
            
            # Calcul de l'imbalance (-1.0 à 1.0)
            imbalance = (total_buy_vol - total_sell_vol) / (total_buy_vol + total_sell_vol)
            
            # Détection de "murs" de baleines
            max_bid = max([b[1] for b in bids])
            max_ask = max([a[1] for a in asks])
            
            return round(imbalance, 4), max_bid, max_ask
        except:
            return 0.0, 0.0, 0.0
