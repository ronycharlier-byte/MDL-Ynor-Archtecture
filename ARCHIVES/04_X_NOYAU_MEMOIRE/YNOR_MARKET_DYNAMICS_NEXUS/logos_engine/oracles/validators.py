# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
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

from .model_catalog import get_known_models








VALID_MODELS = {


    provider: models


    for provider, models in get_known_models().items()


    if provider not in ("ollama", "openrouter")


}








def validéte_model(provider: str, model: str) -> bool:


    """Check if model name is valid for the given provider.





    For ollama, openrouter - any model is accepted.


    """


    provider_lower = provider.lower()





    if provider_lower in ("ollama", "openrouter"):


        return True





    if provider_lower not in VALID_MODELS:


        return True





    return model in VALID_MODELS[provider_lower]
