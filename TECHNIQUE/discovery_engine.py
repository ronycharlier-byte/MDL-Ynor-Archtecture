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
# INIT
# =============================
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)

knowledge = []
elite_pool = []

# =============================
# IMPORTS
# =============================
from navier_stokes_2d import simulate_2d
from law_engine import discover_law

# =============================
# SAFE LLM CALL
# =============================
def safe_llm(prompt):
    try:
        res = llm.invoke(prompt)
        return res.content.strip() if res and res.content else "Hypothèse vide"
    except Exception as e:
        print("⚠️ LLM error:", e)
        return "Hypothèse invalide"

# =============================
# GENERATE HYPOTHESIS
# =============================
def generate_hypothesis(context):
    prompt = f"""
Tu es un chercheur en physique mathématique.

CONTEXTE:
{context}

Génère une hypothèse testable sur :
- dissipation µ
- turbulence
- stabilité

Format court.
"""
    return safe_llm(prompt)

# =============================
# MUTATION ENGINE
# =============================
def mutate_hypothesis(hypothesis):
    prompt = f"""
Améliore cette hypothèse :

{hypothesis}

Ajoute :
- seuil critique
- condition mathématique
- précision
"""
    return safe_llm(prompt)

# =============================
# CROSSOVER
# =============================
def crossover(h1, h2):
    if h1 == h2:
        return h1

    prompt = f"""
Fusionne ces hypothèses :

H1:
{h1}

H2:
{h2}

Crée une version meilleure.
"""
    return safe_llm(prompt)

# =============================
# TEST
# =============================
def test_hypothesis():
    try:
        result = simulate_2d()
    except Exception as e:
        print("⚠️ Simulation error:", e)
        return {}, False

    if not result:
        return {}, False

    stable = (
        result.get("energy", 999) < 20 and
        not result.get("singularity", True) and
        -2.2 < result.get("kolmogorov_slope", 0) < -1.2
    )

    return result, stable

# =============================
# SCORE
# =============================
def score(hypothesis, stable):
    s = 0

    if stable:
        s += 5

    keywords = ["seuil", "critique", "μ", "mu", "turbulence", "stabilité"]

    for k in keywords:
        if k in hypothesis.lower():
            s += 1

    # diversité (évite stagnation)
    s += random.uniform(0, 1)

    return s

# =============================
# SELECTION
# =============================
def select_elite(population, top_k=3):
    population = [p for p in population if p["result"]]  # filtre invalides

    if not population:
        return []

    sorted_pop = sorted(population, key=lambda x: x["score"], reverse=True)
    return sorted_pop[:top_k]

# =============================
# DISCOVERY LOOP
# =============================
def discovery_engine(seed, generations=8, population_size=6):

    global elite_pool

    context = seed

    for g in range(generations):
        print(f"\n🧬 GENERATION {g+1}")

        population = []

        for i in range(population_size):

            # =============================
            # STRATEGY
            # =============================
            if elite_pool and random.random() > 0.6:
                parent = random.choice(elite_pool)["hypothesis"]
                hypothesis = mutate_hypothesis(parent)
            else:
                hypothesis = generate_hypothesis(context)

            # crossover
            if len(elite_pool) >= 2 and random.random() > 0.7:
                h1 = random.choice(elite_pool)["hypothesis"]
                h2 = random.choice(elite_pool)["hypothesis"]
                hypothesis = crossover(h1, h2)

            # =============================
            # TEST
            # =============================
            result, stable = test_hypothesis()

            if not result:
                continue

            s = score(hypothesis, stable)

            print(f"\n💡 {hypothesis}")
            print("🧪", result)
            print("🏁 score:", s)

            population.append({
                "hypothesis": hypothesis,
                "result": result,
                "stable": stable,
                "score": s
            })

        # =============================
        # SELECTION
        # =============================
        elite = select_elite(population)

        if not elite:
            print("⚠️ Aucun elite trouvé → reset")
            elite_pool = []
            continue

        print("\n🏆 ELITE:")
        for e in elite:
            print("→", e["hypothesis"])

        elite_pool = elite

        # =============================
        # LAW DISCOVERY (NOUVEAU)
        # =============================
        results_only = [p["result"] for p in population]

        if results_only:
            law, law_score = discover_law(results_only)

            print("\n📐 LOI DÉCOUVERTE:")
            print(law, "score:", law_score)

        # nouveau contexte = meilleur
        context = elite[0]["hypothesis"]

        knowledge.extend(population)

        save_knowledge()

# =============================
# SAVE
# =============================
def save_knowledge():
    try:
        with open("discovery.json", "w", encoding="utf-8") as f:
            json.dump(knowledge, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("⚠️ Save error:", e)

# =============================
# RUN
# =============================
if __name__ == "__main__":
    seed = input("🎯 Seed idea: ")
    discovery_engine(seed)
