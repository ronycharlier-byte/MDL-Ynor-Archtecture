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

class SymbolicAdvanced:

    def __init__(self):
        self.population = []
        self.best = None

        self.variables = ["E", "G", "S"]
        self.ops = ["+", "-", "*", "/"]

    # =============================
    # RANDOM EQUATION
    # =============================
    def random_expr(self):
        a = random.choice(self.variables)
        b = random.choice(self.variables)
        op = random.choice(self.ops)

        return f"({a} {op} {b})"

    def random_equation(self):
        expr = self.random_expr()

        for _ in range(random.randint(1, 3)):
            expr = f"({expr} {random.choice(self.ops)} {self.random_expr()})"

        return expr

    # =============================
    # SAFE EVAL
    # =============================
    def eval_expr(self, expr, E, G, S):
        try:
            return eval(expr, {"__builtins__": {}}, {
                "E": E,
                "G": G,
                "S": S
            })
        except:
            return 0

    # =============================
    # FITNESS
    # =============================
    def fitness(self, expr, data):
        error = 0

        for d in data:
            pred = self.eval_expr(expr, d["E"], d["G"], d["S"])
            target = d["y"]

            error += (pred - target) ** 2

        return -error  # max fitness

    # =============================
    # MUTATION
    # =============================
    def mutate(self, expr):
        if random.random() < 0.5:
            return self.random_equation()
        return expr

    # =============================
    # EVOLUTION
    # =============================
    def evolve(self, dataset, generations=10, pop_size=20):

        # init
        population = [self.random_equation() for _ in range(pop_size)]

        for g in range(generations):
            scored = []

            for expr in population:
                fit = self.fitness(expr, dataset)
                scored.append((expr, fit))

            scored.sort(key=lambda x: x[1], reverse=True)

            best_expr = scored[0][0]
            print(f"\n🧬 Gen {g+1} best:", best_expr)

            # sélection
            survivors = [e for e, _ in scored[:5]]

            # reproduction
            new_population = survivors.copy()

            while len(new_population) < pop_size:
                parent = random.choice(survivors)
                child = self.mutate(parent)
                new_population.append(child)

            population = new_population

        self.best = scored[0][0]
        return self.best
