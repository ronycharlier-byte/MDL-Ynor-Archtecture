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

class SymbolicEngine:

    def __init__(self):
        self.X = []
        self.y = []
        self.model = None

    # =============================
    # ADD SAMPLE
    # =============================
    def add_sample(self, sim_result):
        try:
            x = [
                float(sim_result.get("energy", 0)),
                float(sim_result.get("gradient", 0)),
                float(sim_result.get("kolmogorov_slope", 0))
            ]

            # évite NaN / inf
            if any(np.isnan(x)) or any(np.isinf(x)):
                return

            # label stabilité robuste
            stable = (
                sim_result.get("energy", 0) < sim_result.get("gradient", 1e-6)
                and not sim_result.get("singularity", False)
            )

            y = 1 if stable else 0

            self.X.append(x)
            self.y.append(y)

        except Exception as e:
            print("⚠️ Symbolic add error:", e)

    # =============================
    # FIT MODEL
    # =============================
    def fit(self):
        if len(self.X) < 8:
            return None

        try:
            X = np.array(self.X)
            y = np.array(self.y)

            model = LinearRegression()
            model.fit(X, y)

            self.model = model
            return model

        except Exception as e:
            print("⚠️ Fit error:", e)
            return None

    # =============================
    # PREDICT STABILITY
    # =============================
    def predict(self, sim_result):
        if self.model is None:
            return None

        x = np.array([[
            sim_result.get("energy", 0),
            sim_result.get("gradient", 0),
            sim_result.get("kolmogorov_slope", 0)
        ]])

        return float(self.model.predict(x)[0])

    # =============================
    # EXTRACT LAW
    # =============================
    def extract_law(self):
        if self.model is None:
            return "Pas assez de données."

        coefs = self.model.coef_
        intercept = self.model.intercept_

        return f"""
=============================
📐 LOI SYMBOLIQUE DÉTECTÉE
=============================

μ* ≈ {coefs[0]:.4f}·E + {coefs[1]:.4f}·G + {coefs[2]:.4f}·S + {intercept:.4f}

Interprétation :
- E → énergie totale
- G → dissipation (gradient²)
- S → structure turbulente

➡️ μ* ≈ score de stabilité du système
"""
