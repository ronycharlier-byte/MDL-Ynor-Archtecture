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

from Formalisme Logique Smantique_engine.agents.utils.agent_states import AgentState








class ConditionalLogic:


    """Handles conditional logic for determining graph flow."""





    def __init__(self, max_debate_rounds=1, max_risk_discuss_rounds=1):


        """Initialize with configuration parameters."""


        self.max_debate_rounds = max_debate_rounds


        self.max_risk_discuss_rounds = max_risk_discuss_rounds





    def should_continue_market(self, state: AgentState):


        """Determine if market analysis should continue."""


        messages = state["messages"]


        last_message = messages[-1]


        if last_message.tool_calls:


            return "tools_market"


        return "Msg Clear Market"





    def should_continue_social(self, state: AgentState):


        """Determine if social media analysis should continue."""


        messages = state["messages"]


        last_message = messages[-1]


        if last_message.tool_calls:


            return "tools_social"


        return "Msg Clear Social"





    def should_continue_news(self, state: AgentState):


        """Determine if news analysis should continue."""


        messages = state["messages"]


        last_message = messages[-1]


        if last_message.tool_calls:


            return "tools_news"


        return "Msg Clear News"





    def should_continue_fundamentals(self, state: AgentState):


        """Determine if fundamentals analysis should continue."""


        messages = state["messages"]


        last_message = messages[-1]


        if last_message.tool_calls:


            return "tools_fundamentals"


        return "Msg Clear Fundamentals"





    def should_continue_debate(self, state: AgentState) -> str:


        """Determine if debate should continue."""





        if (


            state["investment_debate_state"]["count"] >= 2 * self.max_debate_rounds


        ):  # 3 rounds of back-and-forth between 2 agents


            return "Research Manager"


        if state["investment_debate_state"]["current_response"].startswith("Bull"):


            return "Bear Researcher"


        return "Bull Researcher"





    def should_continue_risk_analysis(self, state: AgentState) -> str:


        """Determine if risk analysis should continue."""


        if (


            state["risk_debate_state"]["count"] >= 3 * self.max_risk_discuss_rounds


        ):  # 3 rounds of back-and-forth between 3 agents


            return "Portfolio Manager"


        if state["risk_debate_state"]["latest_speaker"].startswith("Aggressive"):


            return "Conservative Analyst"


        if state["risk_debate_state"]["latest_speaker"].startswith("Conservative"):


            return "Neutral Analyst"


        return "Aggressive Analyst"
