# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** C
# **Rôle du Fichier :** Moteur operatoire
# **Centre Doctrinal Local :** AI Manager garde moteur operatoire en limitant le bruit local et la friction structurelle.
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
# **Lien Miroir :** C'

from typing import Dict

import pandas as pd


def compute_market_features(df: pd.DataFrame) -> Dict[str, float | bool]:
    if df.empty or len(df) < 25:
        return {}

    close = df["close"].astype(float)
    high = df["high"].astype(float)
    low = df["low"].astype(float)
    volume = df["volume"].astype(float)

    current_price = float(close.iloc[-1])
    previous_high_20 = float(high.iloc[-21:-1].max())
    previous_low_20 = float(low.iloc[-21:-1].min())
    ema_fast = float(close.ewm(span=9, adjust=False).mean().iloc[-1])
    ema_slow = float(close.ewm(span=21, adjust=False).mean().iloc[-1])

    momentum_5 = float(close.iloc[-1] / close.iloc[-6] - 1.0) if len(close) >= 6 else 0.0
    momentum_20 = float(close.iloc[-1] / close.iloc[-21] - 1.0) if len(close) >= 21 else 0.0

    volume_mean_20 = float(volume.iloc[-21:-1].mean())
    volume_ratio_20 = float(volume.iloc[-1] / volume_mean_20) if volume_mean_20 > 0 else 0.0

    returns = close.pct_change().dropna()
    volatility_20 = float(returns.tail(20).std() * (20 ** 0.5)) if len(returns) >= 5 else 0.0

    breakout_20 = current_price > previous_high_20
    sweep_reversal = float(low.iloc[-1]) < previous_low_20 and current_price > previous_low_20

    return {
        "current_price": current_price,
        "previous_high_20": previous_high_20,
        "previous_low_20": previous_low_20,
        "ema_fast": ema_fast,
        "ema_slow": ema_slow,
        "momentum_5": momentum_5,
        "momentum_20": momentum_20,
        "volume_ratio_20": volume_ratio_20,
        "volatility_20": volatility_20,
        "breakout_20": breakout_20,
        "sweep_reversal": sweep_reversal,
    }
