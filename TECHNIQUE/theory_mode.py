# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Theorie et demonstration
# **Centre Doctrinal Local :** AI Manager garde theorie et demonstration en limitant le bruit local et la friction structurelle.
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

memory = VectorMemory()

memory.load_from_json(
    r"C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\vector_memory.json"
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

theory = []

# =============================
# STEP 1 : EXTRACT PATTERNS
# =============================
def extract_patterns(topic):
    results = memory.search(topic, top_k=8)

    context = "\n\n".join([r["text"] for r in results])

    prompt = f"""
Analyse ces extraits et identifie les PATTERNS récurrents.

CONTEXTE :
{context}

FORMAT :
- concepts récurrents
- relations entre concepts
- structures implicites
"""

    return llm.invoke(prompt).content, context


# =============================
# STEP 2 : GENERATE HYPOTHESIS
# =============================
def generate_hypothesis(patterns):
    prompt = f"""
À partir de ces patterns :

{patterns}

Génère UNE hypothèse forte.

RÈGLES :
- doit être testable
- doit être précise
- doit expliquer le système
"""

    return llm.invoke(prompt).content.strip()


# =============================
# STEP 3 : TEST HYPOTHESIS
# =============================
def test_hypothesis(hypothesis, context):
    prompt = f"""
Teste cette hypothèse STRICTEMENT avec le contexte.

HYPOTHÈSE :
{hypothesis}

CONTEXTE :
{context}

FORMAT :
- éléments qui CONFIRMENT
- éléments qui INFIRMENT
- verdict : VALID / PARTIAL / INVALID
"""

    return llm.invoke(prompt).content


# =============================
# STEP 4 : REFINE
# =============================
def refine(hypothesis, test_result):
    prompt = f"""
HYPOTHÈSE :
{hypothesis}

TEST :
{test_result}

Améliore l'hypothèse pour la rendre plus correcte.

Nouvelle hypothèse :
"""

    return llm.invoke(prompt).content.strip()


# =============================
# MAIN LOOP
# =============================
def theory_mode(topic, iterations=5):

    patterns, context = extract_patterns(topic)

    print("\n🧩 PATTERNS:\n")
    print(patterns)

    hypothesis = generate_hypothesis(patterns)

    for i in range(iterations):

        print(f"\n🔬 ITERATION {i+1}")
        print(f"\n💡 Hypothèse:\n{hypothesis}")

        test = test_hypothesis(hypothesis, context)

        print("\n🧪 Test:\n")
        print(test)

        theory.append({
            "hypothesis": hypothesis,
            "test": test
        })

        # stop si valid fort
        if "VALID" in test:
            print("\n✅ THÉORIE VALIDÉE")
            break

        hypothesis = refine(hypothesis, test)


# =============================
# RUN
# =============================
if __name__ == "__main__":
    topic = input("🎯 Sujet: ")
    theory_mode(topic, iterations=5)
