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

from typing import Annotated


from Formalisme Logique Smantique_engine.dataflows.interface import route_to_vendor





@tool


def get_news(


    ticker: Annotated[str, "Ticker symbol"],


    start_date: Annotated[str, "Start date in yyyy-mm-dd format"],


    end_date: Annotated[str, "End date in yyyy-mm-dd format"],


) -> str:


    """


    Retrieve news data for a given ticker symbol.


    Uses the configured news_data vendor.


    Args:


        ticker (str): Ticker symbol


        start_date (str): Start date in yyyy-mm-dd format


        end_date (str): End date in yyyy-mm-dd format


    Returns:


        str: A formatted string containing news data


    """


    return route_to_vendor("get_news", ticker, start_date, end_date)





@tool


def get_global_news(


    curr_date: Annotated[str, "Current date in yyyy-mm-dd format"],


    look_back_days: Annotated[int, "Number of days to look back"] = 7,


    limit: Annotated[int, "Maximum number of articles to return"] = 5,


) -> str:


    """


    Retrieve global news data.


    Uses the configured news_data vendor.


    Args:


        curr_date (str): Current date in yyyy-mm-dd format


        look_back_days (int): Number of days to look back (default 7)


        limit (int): Maximum number of articles to return (default 5)


    Returns:


        str: A formatted string containing global news data


    """


    return route_to_vendor("get_global_news", curr_date, look_back_days, limit)





@tool


def get_insider_transactions(


    ticker: Annotated[str, "ticker symbol"],


) -> str:


    """


    Retrieve insider transaction information about a company.


    Uses the configured news_data vendor.


    Args:


        ticker (str): Ticker symbol of the company


    Returns:


        str: A report of insider transaction data


    """


    return route_to_vendor("get_insider_transactions", ticker)
