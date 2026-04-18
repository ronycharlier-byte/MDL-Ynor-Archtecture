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

from langchain_openai import ChatOpenAI








class SignalProcessor:


    """Processes trading signals to extract actionable decisions."""





    def __init__(self, quick_thinking_llm: ChatOpenAI):


        """Initialize with an LLM for processing."""


        self.quick_thinking_llm = quick_thinking_llm





    def process_signal(self, full_signal: str) -> str:


        """


        Process a full trading signal to extract the core decision.





        Args:


            full_signal: Complete trading signal text





        Returns:


            Extracted rating (BUY, OVERWEIGHT, HOLD, UNDERWEIGHT, or SELL)


        """


        messages = [


            (


                "system",


                "You are an efficient assistant that extracts the trading decision from analyst reports. "


                "Extract the rating as exactly one of: BUY, OVERWEIGHT, HOLD, UNDERWEIGHT, SELL. "


                "Output only the single rating word, nothing else.",


            ),


            ("human", full_signal),


        ]





        return self.quick_thinking_llm.invoke(messages).content
