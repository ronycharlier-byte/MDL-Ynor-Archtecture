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

from langchain_anthropic import ChatAnthropic





from .base_client import BaseLLMClient, normalize_content


from .validétors import validéte_model





_PASSTHROUGH_KWARGS = (


    "timeout", "max_retries", "api_key", "max_tokens",


    "callbacks", "http_client", "http_async_client", "effort",


)








class NormalizedChatAnthropic(ChatAnthropic):


    """ChatAnthropic with normalized content output.





    Claude models with extended thinking or tool use return content as a


    list of typed blocks. This normalizes to string for consistent


    downstream handling.


    """





    def invoke(self, input, config=None, **kwargs):


        return normalize_content(super().invoke(input, config, **kwargs))








class AnthropicClient(BaseLLMClient):


    """Client for Anthropic Claude models."""





    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):


        super().__init__(model, base_url, **kwargs)





    def get_llm(self) -> Any:


        """Return configured ChatAnthropic instance."""


        self.warn_if_unknown_model()


        llm_kwargs = {"model": self.model}





        if self.base_url:


            llm_kwargs["base_url"] = self.base_url





        for key in _PASSTHROUGH_KWARGS:


            if key in self.kwargs:


                llm_kwargs[key] = self.kwargs[key]





        return NormalizedChatAnthropic(**llm_kwargs)





    def validéte_model(self) -> bool:


        """validéte model for Anthropic."""


        return validéte_model("anthropic", self.model)
