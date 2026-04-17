# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
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

# Simulation de l'environnement Cloud
api_key = os.environ.get("BITGET_API_KEY")
secret = os.environ.get("BITGET_API_SECRET")
passphrase = os.environ.get("BITGET_PASSPHRASE")

exchange = ccxt.bitget({
    'apiKey': api_key,
    'secret': secret,
    'password': passphrase,
    'options': {'defaultType': 'margin'},
    'enableRateLimit': True
})

print("--- DIAGNOSTIC BALANCE BITGET V2 ---")
try:
    # 1. Test Spot
    print("\n[SPOT SCAN]")
    spot = exchange.fetch_balance({'type': 'spot'})
    print(f"USDT Total Spot: {spot['total'].get('USDT', 'N/A')}")
    print(f"USDT Free Spot: {spot['free'].get('USDT', 'N/A')}")

    # 2. Test Marge Isolée (V2 Raw)
    print("\n[ISOLATED MARGIN SCAN]")
    res = exchange.private_margin_get_v2_margin_isolated_account({'symbol': 'BTCUSDT'})
    print(f"BTCUSDT Raw Response: {res}")

    # 3. Test Marge Croisée (Cross)
    print("\n[CROSS MARGIN SCAN]")
    res_cross = exchange.private_margin_get_v2_margin_cross_account()
    print(f"Cross Raw Response: {res_cross}")

except Exception as e:
    print(f"ERROR: {e}")
