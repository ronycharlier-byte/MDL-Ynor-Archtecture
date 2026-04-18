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

from langchain_google_genai import ChatGoogleGenerativeAI





from .base_client import BaseLLMClient, normalize_content


from .validétors import validéte_model








class NormalizedChatGoogleGenerativeAI(ChatGoogleGenerativeAI):


    """ChatGoogleGenerativeAI with normalized content output.





    Gemini 3 models return content as list of typed blocks.


    This normalizes to string for consistent downstream handling.


    """





    def invoke(self, input, config=None, **kwargs):


        return normalize_content(super().invoke(input, config, **kwargs))








class GoogleClient(BaseLLMClient):


    """Client for Google Gemini models."""





    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):


        super().__init__(model, base_url, **kwargs)





    def get_llm(self) -> Any:


        """Return configured ChatGoogleGenerativeAI instance."""


        self.warn_if_unknown_model()


        llm_kwargs = {"model": self.model}





        if self.base_url:


            llm_kwargs["base_url"] = self.base_url





        for key in ("timeout", "max_retries", "callbacks", "http_client", "http_async_client"):


            if key in self.kwargs:


                llm_kwargs[key] = self.kwargs[key]





        # Unified api_key maps to provider-specific google_api_key


        google_api_key = self.kwargs.get("api_key") or self.kwargs.get("google_api_key")


        if google_api_key:


            llm_kwargs["google_api_key"] = google_api_key





        # Map thinking_level to appropriate API param based on model


        # Gemini 3 Pro: low, high


        # Gemini 3 Flash: minimal, low, medium, high


        # Gemini 2.5: thinking_budget (0=disable, -1=dynamic)


        thinking_level = self.kwargs.get("thinking_level")


        if thinking_level:


            model_lower = self.model.lower()


            if "gemini-3" in model_lower:


                # Gemini 3 Pro doesn't support "minimal", use "low" instead


                if "pro" in model_lower and thinking_level == "minimal":


                    thinking_level = "low"


                llm_kwargs["thinking_level"] = thinking_level


            else:


                # Gemini 2.5: map to thinking_budget


                llm_kwargs["thinking_budget"] = -1 if thinking_level == "high" else 0





        return NormalizedChatGoogleGenerativeAI(**llm_kwargs)





    def validéte_model(self) -> bool:


        """validéte model for Google."""


        return validéte_model("google", self.model)
