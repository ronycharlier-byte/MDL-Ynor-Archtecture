# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** B'
# **Rôle du Fichier :** Collecte et ingestion
# **Centre Doctrinal Local :** AI Manager garde collecte et ingestion en limitant le bruit local et la friction structurelle.
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

import json





from Formalisme Logique Smantique_engine.agents.utils.agent_utils import build_instrument_context








def create_research_manager(llm, memory):


    def research_manager_node(state) -> dict:


        instrument_context = build_instrument_context(state["company_of_interest"])


        history = state["investment_debate_state"].get("history", "")


        market_research_report = state["market_report"]


        sentiment_report = state["sentiment_report"]


        news_report = state["news_report"]


        fundamentals_report = state["fundamentals_report"]





        investment_debate_state = state["investment_debate_state"]





        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"


        past_memories = memory.get_memories(curr_situation, n_matches=2)





        past_memory_str = ""


        for i, rec in enumerate(past_memories, 1):


            past_memory_str += rec["recommendation"] + "\n\n"





        prompt = f"""As the portfolio manager and debate facilitator, your role is to critically evaluate this round of debate and make a definitive decision: align with the bear analyst, the bull analyst, or choose Hold only if it is strongly justified based on the arguments presented.





Summarize the key points from both sides concisely, focusing on the most compelling evidence or reasoning. Your recommendation—Buy, Sell, or Hold—must be clear and actionable. Avoid defaulting to Hold simply because both sides have valid points; commit to a stance grounded in the debate's strongest arguments.





Additionally, develop a detailed investment plan for the trader. This should include:





Your Recommendation: A decisive stance supported by the most convincing arguments.


Rationale: An explanation of why these arguments lead to your conclusion.


Strategic Actions: Concrete steps for implementing the recommendation.


Take into account your past mistakes on similar situations. Use these insights to refine your decision-making and ensure you are learning and improving. Present your analysis conversationally, as if speaking naturally, without special formatting. 





Here are your past reflections on mistakes:


\"{past_memory_str}\"





{instrument_context}





Here is the debate:


Debate History:


{history}"""


        response = llm.invoke(prompt)





        new_investment_debate_state = {


            "judge_decision": response.content,


            "history": investment_debate_state.get("history", ""),


            "bear_history": investment_debate_state.get("bear_history", ""),


            "bull_history": investment_debate_state.get("bull_history", ""),


            "current_response": response.content,


            "count": investment_debate_state["count"],


        }





        return {


            "investment_debate_state": new_investment_debate_state,


            "investment_plan": response.content,


        }





    return research_manager_node
