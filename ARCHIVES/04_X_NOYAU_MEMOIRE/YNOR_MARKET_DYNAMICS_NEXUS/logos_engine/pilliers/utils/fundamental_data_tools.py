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


def get_fundamentals(


    ticker: Annotated[str, "ticker symbol"],


    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"],


) -> str:


    """


    Retrieve comprehensive fundamental data for a given ticker symbol.


    Uses the configured fundamental_data vendor.


    Args:


        ticker (str): Ticker symbol of the company


        curr_date (str): Current date you are trading at, yyyy-mm-dd


    Returns:


        str: A formatted report containing comprehensive fundamental data


    """


    return route_to_vendor("get_fundamentals", ticker, curr_date)








@tool


def get_balance_sheet(


    ticker: Annotated[str, "ticker symbol"],


    freq: Annotated[str, "reporting frequency: annual/quarterly"] = "quarterly",


    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"] = None,


) -> str:


    """


    Retrieve balance sheet data for a given ticker symbol.


    Uses the configured fundamental_data vendor.


    Args:


        ticker (str): Ticker symbol of the company


        freq (str): Reporting frequency: annual/quarterly (default quarterly)


        curr_date (str): Current date you are trading at, yyyy-mm-dd


    Returns:


        str: A formatted report containing balance sheet data


    """


    return route_to_vendor("get_balance_sheet", ticker, freq, curr_date)








@tool


def get_cashflow(


    ticker: Annotated[str, "ticker symbol"],


    freq: Annotated[str, "reporting frequency: annual/quarterly"] = "quarterly",


    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"] = None,


) -> str:


    """


    Retrieve cash flow statement data for a given ticker symbol.


    Uses the configured fundamental_data vendor.


    Args:


        ticker (str): Ticker symbol of the company


        freq (str): Reporting frequency: annual/quarterly (default quarterly)


        curr_date (str): Current date you are trading at, yyyy-mm-dd


    Returns:


        str: A formatted report containing cash flow statement data


    """


    return route_to_vendor("get_cashflow", ticker, freq, curr_date)








@tool


def get_income_statement(


    ticker: Annotated[str, "ticker symbol"],


    freq: Annotated[str, "reporting frequency: annual/quarterly"] = "quarterly",


    curr_date: Annotated[str, "current date you are trading at, yyyy-mm-dd"] = None,


) -> str:


    """


    Retrieve income statement data for a given ticker symbol.


    Uses the configured fundamental_data vendor.


    Args:


        ticker (str): Ticker symbol of the company


        freq (str): Reporting frequency: annual/quarterly (default quarterly)


        curr_date (str): Current date you are trading at, yyyy-mm-dd


    Returns:


        str: A formatted report containing income statement data


    """


    return route_to_vendor("get_income_statement", ticker, freq, curr_date)
