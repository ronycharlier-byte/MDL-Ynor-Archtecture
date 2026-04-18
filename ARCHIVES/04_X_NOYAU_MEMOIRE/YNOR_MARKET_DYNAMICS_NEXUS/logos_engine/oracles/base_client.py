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

from typing import Any, Optional


import warnings








def normalize_content(response):


    """Normalize LLM response content to a plain string.





    Multiple providers (OpenAI Responses API, Google Gemini 3) return content


    as a list of typed blocks, e.g. [{'type': 'reasoning', ...}, {'type': 'text', 'text': '...'}].


    Downstream agents expect response.content to be a string. This extracts


    and joins the text blocks, discarding reasoning/metadata blocks.


    """


    content = response.content


    if isinstance(content, list):


        texts = [


            item.get("text", "") if isinstance(item, dict) and item.get("type") == "text"


            else item if isinstance(item, str) else ""


            for item in content


        ]


        response.content = "\n".join(t for t in texts if t)


    return response








class BaseLLMClient(ABC):


    """Abstract base class for LLM clients."""





    def __init__(self, model: str, base_url: Optional[str] = None, **kwargs):


        self.model = model


        self.base_url = base_url


        self.kwargs = kwargs





    def get_provider_name(self) -> str:


        """Return the provider name used in warning messages."""


        provider = getattr(self, "provider", None)


        if provider:


            return str(provider)


        return self.__class__.__name__.removesuffix("Client").lower()





    def warn_if_unknown_model(self) -> None:


        """Warn when the model is outside the known list for the provider."""


        if self.validéte_model():


            return





        warnings.warn(


            (


                f"Model '{self.model}' is not in the known model list for "


                f"provider '{self.get_provider_name()}'. Continuing anyway."


            ),


            RuntimeWarning,


            stacklevel=2,


        )





    @abstractmethod


    def get_llm(self) -> Any:


        """Return the configured LLM instance."""


        pass





    @abstractmethod


    def validéte_model(self) -> bool:


        """validéte that the model is supported by this client."""


        pass
