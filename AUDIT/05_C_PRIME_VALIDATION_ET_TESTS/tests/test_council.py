# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** D
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
# **Lien Miroir :** D'

from core.h_alpha_projection import calculate_h_alpha_stability, apply_kl_projection



def test_h_alpha_clamping():

    """

    Vrifie que le thorme H_alpha tronque correctement une entropie excessive.

    """

    # logprobs mock gnrant une forte entropie

    mock_logprobs = np.array([-0.69, -0.69]) # Distribution uniforme sur 2 tokens ~ ln(2)

    

    stability = calculate_h_alpha_stability(mock_logprobs, alpha_threshold=0.5)

    

    # Assert que ça clamp bien au threshold

    assert stability <= 0.5



def test_kl_divergence_logic():

    """

    Vrifie la divergence KL entre deux distributions.

    """

    p = np.array([0.9, 0.1])

    q = np.array([0.8, 0.2])

    

    kl_div = apply_kl_projection(p, q)

    assert kl_div > 0 # La divergence entre P et Q n'est pas nulle

    assert kl_div < 0.1 # La divergence reste basse
