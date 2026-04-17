# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Modele PDE
# **Centre Doctrinal Local :** AI Manager garde modele pde en limitant le bruit local et la friction structurelle.
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

class PDELearner:

    def __init__(self):
        self.X = []
        self.y = []
        self.model = None

    # =============================
    # BUILD DATASET
    # =============================
    def add_sample(self, u_t, u_next, dx=1.0, dt=0.005):

        dudt = (u_next - u_t) / dt

        dudx = np.gradient(u_t, dx)
        d2udx2 = np.gradient(dudx, dx)

        for i in range(len(u_t)):
            self.X.append([
                u_t[i],
                u_t[i] * dudx[i],
                d2udx2[i]
            ])
            self.y.append(dudt[i])

    # =============================
    # FIT PDE
    # =============================
    def fit(self):
        if len(self.X) < 200:
            return None

        X = np.array(self.X)
        y = np.array(self.y)

        model = LinearRegression()
        model.fit(X, y)

        self.model = model
        return model

    # =============================
    # EXTRACT EQUATION
    # =============================
    def extract_equation(self):
        if self.model is None:
            return "Pas assez de données."

        c = self.model.coef_
        b = self.model.intercept_

        return f"""
=============================
🧠 ÉQUATION APPRISE
=============================

∂u/∂t ≈ {c[0]:.4f}·u
       + {c[1]:.4f}·(u ∂u/∂x)
       + {c[2]:.4f}·(∂²u/∂x²)
       + {b:.4f}

Interprétation :
- u → dynamique linéaire
- u∂u/∂x → convection (Navier-Stokes)
- ∂²u/∂x² → diffusion (viscosité)
"""
