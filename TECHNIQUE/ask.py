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

memory = VectorMemory()

# ⚠️ chemin ABSOLU vers ton fichier
memory.load_from_json(
    r"C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\vector_memory.json"
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

history = []

def ask(query):

    global history

    # 🔥 mode intelligent
    if "analyse" in query.lower():
        top_k = 10
    else:
        top_k = 5

    results = memory.search(query, top_k=top_k)

    if not results:
        print("❌ Aucun résultat trouvé.")
        return

    # 🔥 reranking
    results = sorted(results, key=lambda x: x["score"], reverse=True)[:5]

    # 🔥 contexte avec sources
    context = "\n\n".join([
        f"[SOURCE {i+1}] {r['text']}"
        for i, r in enumerate(results)
    ])

    history.append(f"User: {query}")

    prompt = f"""
Tu es une IA experte du corpus MDL Ynor.

OBJECTIF :
Produire une réponse intelligente, structurée et profonde.

STRUCTURE OBLIGATOIRE :
1. 🧩 Interprétation
2. ⚙️ Mécanisme
3. 🔗 Logique
4. 📌 Conclusion

RÈGLES :
- analyse avant de répondre
- relie les sources entre elles
- cite les sources (SOURCE 1, etc.)
- ne copie pas, explique

HISTORIQUE :
{history}

CONTEXTE :
{context}

QUESTION :
{query}
"""

    response = llm.invoke(prompt)

    print("\n🧠 Réponse :\n")
    print(response.content)

    # 🔥 auto-amélioration
    critique_prompt = f"""
Améliore cette réponse pour la rendre plus claire et plus intelligente :

{response.content}
"""

    improved = llm.invoke(critique_prompt)

    print("\n🚀 Version améliorée :\n")
    print(improved.content)

    history.append(f"AI: {improved.content}")


# =============================
# LOOP
# =============================
while True:
    q = input("\n❓ Question (ou 'exit'): ")

    if q.lower() == "exit":
        break

    ask(q)
