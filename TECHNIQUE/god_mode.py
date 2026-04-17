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

# =============================
# INIT
# =============================
memory = VectorMemory()

memory.load_from_json(
    r"C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\vector_memory.json"
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

knowledge = []

# =============================
# QUESTION GENERATOR
# =============================
def generate_question(context):
    prompt = f"""
Tu es un chercheur de niveau avancé.

CONTEXTE:
{context}

Génère UNE question profonde qui :
- explore une limite
- ou propose une rupture
- ou cherche une preuve

Réponds uniquement avec la question.
"""
    return llm.invoke(prompt).content.strip()


# =============================
# SEARCH + ANALYZE
# =============================
def analyze(question):
    results = memory.search(question, top_k=5)

    if not results:
        return "Aucune donnée."

    context = "\n\n".join([r["text"] for r in results])

    prompt = f"""
Analyse les extraits et réponds.

QUESTION:
{question}

CONTEXTE:
{context}

FORMAT:
- idées clés
- mécanismes
- limites
"""
    return llm.invoke(prompt).content


# =============================
# HYPOTHESIS GENERATOR
# =============================
def generate_hypothesis(analysis):
    prompt = f"""
Tu es un mathématicien.

ANALYSE:
{analysis}

Formule une hypothèse :

- testable
- falsifiable
- précise

Réponds uniquement avec l'hypothèse.
"""
    return llm.invoke(prompt).content.strip()


# =============================
# HYPOTHESIS TEST (NUMERICAL PROXY)
# =============================
def test_hypothesis():
    # simulation simplifiée (proxy Navier-Stokes)
    u = np.random.rand(100)

    energy = np.sum(u**2)
    grad = np.gradient(u)
    dissipation = np.sum(grad**2)

    mu = dissipation

    stable = energy < mu

    return {
        "energy": float(energy),
        "mu": float(mu),
        "stable": stable
    }


# =============================
# SCORING
# =============================
def score_hypothesis(hypothesis, test_result):
    score = 0

    if test_result["stable"]:
        score += 1

    if "critique" in hypothesis.lower():
        score += 1

    if "seuil" in hypothesis.lower():
        score += 1

    return score


# =============================
# LOOP ENGINE
# =============================
def god_mode(topic, iterations=10):

    context = topic

    for i in range(iterations):
        print(f"\n🧠 ITERATION {i+1}")

        question = generate_question(context)
        print(f"\n❓ Question:\n{question}")

        analysis = analyze(question)
        print(f"\n📊 Analyse:\n{analysis}")

        hypothesis = generate_hypothesis(analysis)
        print(f"\n💡 Hypothèse:\n{hypothesis}")

        test = test_hypothesis()
        print(f"\n🧪 Test:\n{test}")

        score = score_hypothesis(hypothesis, test)
        print(f"\n🏁 Score: {score}")

        knowledge.append({
            "question": question,
            "analysis": analysis,
            "hypothesis": hypothesis,
            "test": test,
            "score": score
        })

        # UPDATE CONTEXT (important)
        context = hypothesis


# =============================
# RUN
# =============================
if __name__ == "__main__":
    topic = input("🎯 Sujet: ")
    god_mode(topic, iterations=10)
