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

# Import tools from separate utility files


from Formalisme Logique Smantique_engine.agents.utils.core_stock_tools import (


    get_stock_data


)


from Formalisme Logique Smantique_engine.agents.utils.technical_indicators_tools import (


    get_indicators


)


from Formalisme Logique Smantique_engine.agents.utils.fundamental_data_tools import (


    get_fundamentals,


    get_balance_sheet,


    get_cashflow,


    get_income_statement


)


from Formalisme Logique Smantique_engine.agents.utils.news_data_tools import (


    get_news,


    get_insider_transactions,


    get_global_news


)








def get_language_instruction() -> str:


    """Return a prompt instruction for the configured output language.





    Returns empty string when English (default), so no extra tokens are used.


    Only applied to user-facing agents (analysts, portfolio manager).


    Internal debate agents stay in English for reasoning quality.


    """


    from Formalisme Logique Smantique_engine.dataflows.config import get_config


    lang = get_config().get("output_language", "English")


    if lang.strip().lower() == "english":


        return ""


    return f" Write your entire response in {lang}."








def build_instrument_context(ticker: str) -> str:


    """Describe the exact instrument so agents preserve exchange-qualified tickers."""


    return (


        f"The instrument to analyze is `{ticker}`. "


        "Use this exact ticker in every tool call, report, and recommendation, "


        "preserving any exchange suffix (e.g. `.TO`, `.L`, `.HK`, `.T`)."


    )





def create_msg_delete():


    def delete_messages(state):


        """Clear messages and add placeholder for Anthropic compatibility"""


        messages = state["messages"]





        # Remove all messages


        removal_operations = [RemoveMessage(id=m.id) for m in messages]





        # Add a minimal placeholder message


        placeholder = HumanMessage(content="Continue")





        return {"messages": removal_operations + [placeholder]}





    return delete_messages








        
