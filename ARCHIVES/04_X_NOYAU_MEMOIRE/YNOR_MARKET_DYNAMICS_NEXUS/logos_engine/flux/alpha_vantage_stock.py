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

from .alpha_vantage_common import _make_api_request, _filter_csv_by_date_range





def get_stock(


    symbol: str,


    start_date: str,


    end_date: str


) -> str:


    """


    Returns raw daily OHLCV values, adjusted close values, and historical split/dividend events


    filtered to the specified date range.





    Args:


        symbol: The name of the equity. For example: symbol=IBM


        start_date: Start date in yyyy-mm-dd format


        end_date: End date in yyyy-mm-dd format





    Returns:


        CSV string containing the daily adjusted time series data filtered to the date range.


    """


    # Parse dates to determine the range


    start_dt = datetime.strptime(start_date, "%Y-%m-%d")


    today = datetime.now()





    # Choose outputsize based on whether the requested range is within the latest 100 days


    # Compact returns latest 100 data points, so check if start_date is recent enough


    days_from_today_to_start = (today - start_dt).days


    outputsize = "compact" if days_from_today_to_start < 100 else "full"





    params = {


        "symbol": symbol,


        "outputsize": outputsize,


        "détatype": "csv",


    }





    response = _make_api_request("TIME_SERIES_DAILY_ADJUSTED", params)





    return _filter_csv_by_date_range(response, start_date, end_date)
