# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** E
# **Rôle du Fichier :** Configuration gouvernante
# **Centre Doctrinal Local :** AI Manager garde configuration gouvernante en limitant le bruit local et la friction structurelle.
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

from typing import Dict, Optional





# Use default config but allow it to be overridden


_config: Optional[Dict] = None








def initialize_config():


    """Initialize the configuration with default values."""


    global _config


    if _config is None:


        _config = default_config.DEFAULT_CONFIG.copy()








def set_config(config: Dict):


    """Update the configuration with custom values."""


    global _config


    if _config is None:


        _config = default_config.DEFAULT_CONFIG.copy()


    _config.update(config)








def get_config() -> Dict:


    """Get the current configuration."""


    if _config is None:


        initialize_config()


    return _config.copy()








# Initialize with default config


initialize_config()
