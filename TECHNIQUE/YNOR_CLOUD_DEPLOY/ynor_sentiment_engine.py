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

class YnorSentimentEngine:
    def __init__(self):
        # Dictionnaire de pondération financière
        self.lexicon = {
            "hawkish": 2.5, "dovish": -2.5, "rate hike": 3.0, "rate cut": -3.0,
            "inflation": 1.5, "deflation": -1.5, "bullish": 2.0, "bearish": -2.0,
            "growth": 1.0, "recession": -3.0, "unemployment": -2.0, "jobs": 1.5,
            "gold rally": 2.0, "btc crash": -4.0, "fed pivot": -2.0, "cpi hot": 3.0,
            "cpi cool": -2.0, "war": -5.0, "sanctions": -2.5, "stimulus": 2.0
        }

    def calculate_sentiment_score(self, text):
        """
        Analyse le texte et retourne un score Alpha entre -10 et 10.
        """
        words = text.lower().split()
        score = 0.0
        for word, weight in self.lexicon.items():
            if word in text.lower():
                score += weight
        
        # Normalisation
        alpha = score / 5.0 # On ramène sur une échelle plus humaine
        return round(max(-10.0, min(10.0, alpha)), 2)

    def get_market_bias(self, news_list):
        if not news_list: return 0.0
        scores = [self.calculate_sentiment_score(n) for n in news_list]
        return round(sum(scores) / len(scores), 2)
