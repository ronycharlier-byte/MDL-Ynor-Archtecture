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

# =============================
# EXTRACTION FEATURES
# =============================
def extract_features(result):
    return {
        "E": result["energy"],
        "S": result["kolmogorov_slope"],
        "G": result["max_gradient"],
        "Sing": int(result["singularity"])
    }

# =============================
# GENERATE EQUATION
# =============================
def generate_equation():
    forms = [
        "E = a * G + b",
        "E = a * G^2 + b",
        "E = a * exp(G) + b",
        "E = a * log(G+1) + b",
        "E = a * G + b * S",
        "E = a * G^2 + b * S",
        "E = a * G * S + b"
    ]

    eq = random.choice(forms)

    a = random.uniform(0.001, 2)
    b = random.uniform(-2, 2)

    return eq, a, b

# =============================
# APPLY EQUATION
# =============================
def evaluate_equation(eq, a, b, features):

    G = features["G"]
    S = features["S"]

    try:
        if "G^2" in eq:
            val = a * (G**2) + b
        elif "exp" in eq:
            val = a * np.exp(G) + b
        elif "log" in eq:
            val = a * np.log(G + 1) + b
        elif "G * S" in eq:
            val = a * G * S + b
        elif "G + b * S" in eq:
            val = a * G + b * S
        else:
            val = a * G + b

        return val
    except:
        return None

# =============================
# SCORE EQUATION
# =============================
def score_equation(pred, real):
    if pred is None:
        return -999

    error = abs(pred - real)

    return -error  # plus proche = meilleur

# =============================
# DISCOVER LAW
# =============================
def discover_law(results, trials=50):

    best_eq = None
    best_score = -999

    for _ in range(trials):

        eq, a, b = generate_equation()

        scores = []

        for r in results:
            features = extract_features(r)

            pred = evaluate_equation(eq, a, b, features)
            real = features["E"]

            s = score_equation(pred, real)
            scores.append(s)

        avg_score = np.mean(scores)

        if avg_score > best_score:
            best_score = avg_score
            best_eq = (eq, a, b)

    return best_eq, best_score
