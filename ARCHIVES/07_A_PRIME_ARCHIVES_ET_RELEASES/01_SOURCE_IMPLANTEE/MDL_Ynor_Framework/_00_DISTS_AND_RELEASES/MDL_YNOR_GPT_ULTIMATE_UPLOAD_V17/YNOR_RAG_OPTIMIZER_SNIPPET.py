# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** B'
# **Rôle du Fichier :** Chaine RAG
# **Centre Doctrinal Local :** AI Manager garde chaine rag en limitant le bruit local et la friction structurelle.
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
# **Lien Miroir :** B

def compress_context(files_content, max_tokens=1500):
    """
    Optimise le contexte envoyé à l'IA pour réduire les coûts (Stratégie MDL Ynor).
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    optimized_context = ""
    
    for filename, text in files_content.items():
        tokens = encoding.encode(text)
        if len(tokens) > 500:
            # On ne garde que le début, le milieu et la fin (Résumé extractif)
            summary = text[:300] + "\n[...]\n" + text[-300:]
            optimized_context += f"### SOURCE: {filename} (Compressed)\n{summary}\n\n"
        else:
            optimized_context += f"### SOURCE: {filename}\n{text}\n\n"
            
    return optimized_context
