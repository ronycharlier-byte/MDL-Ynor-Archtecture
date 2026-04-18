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

import time


import json





from Formalisme Logique Smantique_engine.agents.utils.agent_utils import build_instrument_context








def create_trader(llm, memory):


    def trader_node(state, name):


        company_name = state["company_of_interest"]


        instrument_context = build_instrument_context(company_name)


        investment_plan = state["investment_plan"]


        market_research_report = state["market_report"]


        sentiment_report = state["sentiment_report"]


        news_report = state["news_report"]


        fundamentals_report = state["fundamentals_report"]





        curr_situation = f"{market_research_report}\n\n{sentiment_report}\n\n{news_report}\n\n{fundamentals_report}"


        past_memories = memory.get_memories(curr_situation, n_matches=2)





        past_memory_str = ""


        if past_memories:


            for i, rec in enumerate(past_memories, 1):


                past_memory_str += rec["recommendation"] + "\n\n"


        else:


            past_memory_str = "No past memories found."





        context = {


            "role": "user",


            "content": f"Based on a comprehensive analysis by a team of analysts, here is an investment plan tailored for {company_name}. {instrument_context} This plan incorporates insights from current technical market trends, macroeconomic indicators, and social media sentiment. Use this plan as a foundation for evaluating your next trading decision.\n\nProposed Investment Plan: {investment_plan}\n\nLeverage these insights to make an informed and strategic decision.",


        }





        messages = [


            {


                "role": "system",


                "content": f"""You are a trading agent analyzing market data to make investment decisions. Based on your analysis, provide a specific recommendation to buy, sell, or hold. End with a firm decision and always conclude your response with 'FINAL TRANSACTION PROPOSAL: **BUY/HOLD/SELL**' to confirm your recommendation. Apply lessons from past decisions to strengthen your analysis. Here are reflections from similar situations you traded in and the lessons learned: {past_memory_str}""",


            },


            context,


        ]





        result = llm.invoke(messages)





        return {


            "messages": [result],


            "trader_investment_plan": result.content,


            "sender": name,


        }





    return functools.partial(trader_node, name="Trader")
