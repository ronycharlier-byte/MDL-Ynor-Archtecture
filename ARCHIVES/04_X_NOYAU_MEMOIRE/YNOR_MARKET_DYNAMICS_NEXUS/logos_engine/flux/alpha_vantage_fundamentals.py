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

def _filter_reports_by_date(result, curr_date: str):


    """Filter annualReports/quarterlyReports to exclude entries after curr_date.





    Prevents look-ahead bias by removing fiscal periods that end after


    the simulation's current date.


    """


    if not curr_date or not isinstance(result, dict):


        return result


    for key in ("annualReports", "quarterlyReports"):


        if key in result:


            result[key] = [


                r for r in result[key]


                if r.get("fiscalDateEnding", "") <= curr_date


            ]


    return result








def get_fundamentals(ticker: str, curr_date: str = None) -> str:


    """


    Retrieve comprehensive fundamental data for a given ticker symbol using Alpha Vantage.





    Args:


        ticker (str): Ticker symbol of the company


        curr_date (str): Current date you are trading at, yyyy-mm-dd (not used for Alpha Vantage)





    Returns:


        str: Company overview data including financial ratios and key metrics


    """


    params = {


        "symbol": ticker,


    }





    return _make_api_request("OVERVIEW", params)








def get_balance_sheet(ticker: str, freq: str = "quarterly", curr_date: str = None):


    """Retrieve balance sheet data for a given ticker symbol using Alpha Vantage."""


    result = _make_api_request("BALANCE_SHEET", {"symbol": ticker})


    return _filter_reports_by_date(result, curr_date)








def get_cashflow(ticker: str, freq: str = "quarterly", curr_date: str = None):


    """Retrieve cash flow statement data for a given ticker symbol using Alpha Vantage."""


    result = _make_api_request("CASH_FLOW", {"symbol": ticker})


    return _filter_reports_by_date(result, curr_date)








def get_income_statement(ticker: str, freq: str = "quarterly", curr_date: str = None):


    """Retrieve income statement data for a given ticker symbol using Alpha Vantage."""


    result = _make_api_request("INCOME_STATEMENT", {"symbol": ticker})


    return _filter_reports_by_date(result, curr_date)
