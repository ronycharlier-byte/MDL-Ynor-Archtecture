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

from typing import Dict, Any, List, Optional


from Formalisme Logique Smantique_engine.agents.utils.agent_states import (


    AgentState,


    InvestDebateState,


    RiskDebateState,


)








class Propagator:


    """Handles state initialization and propagation through the graph."""





    def __init__(self, max_recur_limit=100):


        """Initialize with configuration parameters."""


        self.max_recur_limit = max_recur_limit





    def create_initial_state(


        self, company_name: str, trade_date: str


    ) -> Dict[str, Any]:


        """Create the initial state for the agent graph."""


        return {


            "messages": [("human", company_name)],


            "company_of_interest": company_name,


            "trade_date": str(trade_date),


            "investment_debate_state": InvestDebateState(


                {


                    "bull_history": "",


                    "bear_history": "",


                    "history": "",


                    "current_response": "",


                    "judge_decision": "",


                    "count": 0,


                }


            ),


            "risk_debate_state": RiskDebateState(


                {


                    "aggressive_history": "",


                    "conservative_history": "",


                    "neutral_history": "",


                    "history": "",


                    "latest_speaker": "",


                    "current_aggressive_response": "",


                    "current_conservative_response": "",


                    "current_neutral_response": "",


                    "judge_decision": "",


                    "count": 0,


                }


            ),


            "market_report": "",


            "fundamentals_report": "",


            "sentiment_report": "",


            "news_report": "",


        }





    def get_graph_args(self, callbacks: Optional[List] = None) -> Dict[str, Any]:


        """Get arguments for the graph invocation.





        Args:


            callbacks: Optional list of callback handlers for tool execution tracking.


                       Note: LLM callbacks are handled separately via LLM constructor.


        """


        config = {"recursion_limit": self.max_recur_limit}


        if callbacks:


            config["callbacks"] = callbacks


        return {


            "stream_mode": "values",


            "config": config,


        }
