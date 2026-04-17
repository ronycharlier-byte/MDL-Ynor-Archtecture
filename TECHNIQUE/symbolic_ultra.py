# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
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

class SymbolicUltra:

    def __init__(self):
        self.variables = ["E", "G", "S"]
        self.ops = ["+", "-", "*", "/"]

    # =============================
    # SAFE OPERATIONS
    # =============================
    def safe_div(self, a, b):
        return a / (b + 1e-6)

    def safe_log(self, x):
        return np.log(abs(x) + 1e-6)

    # =============================
    # RANDOM EXPRESSION
    # =============================
    def random_expr(self):
        a = random.choice(self.variables)
        b = random.choice(self.variables)
        op = random.choice(self.ops)

        return f"self.safe_div({a},{b})" if op == "/" else f"({a} {op} {b})"

    def build_equation(self):
        expr = self.random_expr()

        for _ in range(random.randint(1, 3)):
            expr = f"({expr} {random.choice(self.ops)} {self.random_expr()})"

        return expr

    # =============================
    # EVALUATION
    # =============================
    def eval_expr(self, expr, E, G, S):
        try:
            return eval(expr, {"self": self}, {"E": E, "G": G, "S": S})
        except:
            return 0

    # =============================
    # PHYSICS LOSS
    # =============================
    def physics_loss(self, expr, data):
        loss = 0

        for d in data:
            E = d["E"]
            G = d["G"]
            S = d["S"]

            pred = self.eval_expr(expr, E, G, S)

            # stabilité cible
            target = d["y"]

            # erreur classique
            loss += (pred - target) ** 2

            # pénalité physique
            if pred < 0:
                loss += 5  # µ doit être positif

            if not (-3 < S < -0.5):
                loss += 2  # turbulence invalide

        return loss

    # =============================
    # EVOLUTION
    # =============================
    def evolve(self, dataset, generations=10, pop_size=30):

        population = [self.build_equation() for _ in range(pop_size)]

        for g in range(generations):

            scored = []

            for expr in population:
                loss = self.physics_loss(expr, dataset)
                scored.append((expr, loss))

            scored.sort(key=lambda x: x[1])

            best_expr = scored[0][0]
            print(f"\n🧬 Gen {g+1} best:", best_expr)

            survivors = [e for e, _ in scored[:5]]

            new_pop = survivors.copy()

            while len(new_pop) < pop_size:
                parent = random.choice(survivors)

                if random.random() < 0.5:
                    child = self.build_equation()
                else:
                    child = parent

                new_pop.append(child)

            population = new_pop

        return scored[0][0]
