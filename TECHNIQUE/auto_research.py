# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Collecte et ingestion
# **Centre Doctrinal Local :** AI Manager garde collecte et ingestion en limitant le bruit local et la friction structurelle.
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

knowledge = []

# =============================
# STEP 1 : ANALYZE
# =============================
def analyze(question):
    results = memory.search(question, top_k=5)

    if not results:
        return None, None

    context = "\n\n".join([r["text"] for r in results])

    prompt = f"""
Tu es un analyste STRICT du corpus.

RÈGLES :
- Tu dois UNIQUEMENT utiliser le contexte
- Interdiction d'inventer
- Interdiction de généraliser

QUESTION :
{question}

CONTEXTE :
{context}

FORMAT :
1. idées extraites
2. mécanismes concrets
3. limites réelles
"""

    response = llm.invoke(prompt).content

    return response, context


# =============================
# STEP 2 : NEXT QUESTION (SAFE)
# =============================
def next_question(previous_q, analysis, context):
    prompt = f"""
Tu es un chercheur STRICT.

CONTEXTE :
{context}

ANALYSE :
{analysis}

RÈGLES :
- reste STRICTEMENT dans le contenu
- ne crée PAS de nouveaux concepts
- approfondis UNIQUEMENT ce qui existe

Génère UNE question plus précise qui :
- creuse un point existant
- ou clarifie une limite

QUESTION :
"""
    return llm.invoke(prompt).content.strip()


# =============================
# STEP 3 : GROUNDING CHECK
# =============================
def is_grounded(question, context):
    prompt = f"""
QUESTION :
{question}

CONTEXTE :
{context}

Est-ce que la question est STRICTEMENT basée sur le contexte ?

Réponds uniquement par :
YES ou NO
"""
    answer = llm.invoke(prompt).content.strip()
    return "YES" in answer


# =============================
# MAIN LOOP
# =============================
def auto_research(topic, iterations=5):

    question = topic

    for i in range(iterations):

        print(f"\n🔎 ITERATION {i+1}")
        print(f"❓ Question: {question}")

        analysis, context = analyze(question)

        if not analysis:
            print("❌ Aucun résultat trouvé.")
            break

        print("\n🧠 Analyse:\n")
        print(analysis)

        knowledge.append({
            "question": question,
            "analysis": analysis
        })

        next_q = next_question(question, analysis, context)

        # 🔒 sécurité anti-dérive
        if not is_grounded(next_q, context):
            print("\n⚠️ DÉRIVE DÉTECTÉE → STOP")
            break

        question = next_q


# =============================
# RUN
# =============================
if __name__ == "__main__":
    topic = input("🎯 Sujet de recherche: ")
    auto_research(topic, iterations=10)
