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

from .base_client import BaseLLMClient


from .openai_client import OpenAIClient


from .anthropic_client import AnthropicClient


from .google_client import GoogleClient








def create_llm_client(


    provider: str,


    model: str,


    base_url: Optional[str] = None,


    **kwargs,


) -> BaseLLMClient:


    """Create an LLM client for the specified provider.





    Args:


        provider: LLM provider (openai, anthropic, google, xai, ollama, openrouter)


        model: Model name/identifier


        base_url: Optional base URL for API endpoint


        **kwargs: Additional provider-specific arguments


            - http_client: Custom httpx.Client for SSL proxy or certificate customization


            - http_async_client: Custom httpx.AsyncClient for async operations


            - timeout: Request timeout in seconds


            - max_retries: Maximum retry attempts


            - api_key: API key for the provider


            - callbacks: LangChain callbacks





    Returns:


        Configured BaseLLMClient instance





    Raises:


        ValueError: If provider is not supported


    """


    provider_lower = provider.lower()





    if provider_lower in ("openai", "ollama", "openrouter"):


        return OpenAIClient(model, base_url, provider=provider_lower, **kwargs)





    if provider_lower == "xai":


        return OpenAIClient(model, base_url, provider="xai", **kwargs)





    if provider_lower == "anthropic":


        return AnthropicClient(model, base_url, **kwargs)





    if provider_lower == "google":


        return GoogleClient(model, base_url, **kwargs)





    raise ValueError(f"Unsupported LLM provider: {provider}")
