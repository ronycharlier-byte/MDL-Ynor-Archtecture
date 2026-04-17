# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur de sentiment
# **Centre Doctrinal Local :** AI Manager garde moteur de sentiment en limitant le bruit local et la friction structurelle.
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

class YnorGeoSentimentEngine:
    def __init__(self):
        # Lexique Polyglotte (EN, JP, FR, CN)
        self.lexicon = {
            # Anglais
            "hawkish": 2.5, "dovish": -2.5, "rate hike": 3.0, "crash": -5.0,
            # Japonais (Signaux Forex/Global)
            "下落": -2.0, "介入": 3.0, "金利": 1.5, # Baisse, Intervention, Taux
            # Français
            "récession": -3.5, "inflation": 2.0, "crise": -4.0,
            # Chinois (Signaux Marchés Asie)
            "牛市": 2.0, "熊市": -3.0, "破产": -5.0 # Bull market, Bear market, Bankruptcy
        }

    def analyze_global_feed(self, text):
        score = 0.0
        for term, weight in self.lexicon.items():
            if term in text.lower():
                score += weight
        return round(max(-10.0, min(10.0, score / 4.0)), 2)

    def detect_black_swan(self, alpha, riemann):
        """
        Détecte une divergence fatale (Alpha et Riemann opposés violemment).
        """
        if abs(alpha) > 8.0 and riemann < 0.2:
            return True # ALERTE ANOMALIE
        return False
