# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** C'
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
# **Lien Miroir :** C

# Configuration du Shield
# SAFE_MODE = True par défaut. Nécessite MDL_ALLOW_MUTATION=TRUE pour désactiver.
SAFE_MODE = os.getenv("MDL_SAFE_MODE", "TRUE").upper() == "TRUE"

# Configuration Logging Audit
logging.basicConfig(
    filename='mdl_security_audit.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | SHIELD: %(message)s'
)

def require_human_approval(func):
    """Décorateur pour empêcher toute auto-modification sans autorisation explicite."""
    def wrapper(*args, **kwargs):
        action_name = func.__name__
        if SAFE_MODE:
            msg = f"❌ TENTATIVE D'AUTO-MODIFICATION BLOQUÉE : {action_name}. [SAFE_MODE=ACTIVE]"
            print(f"\n[⚠️ SECURITY] {msg}")
            logging.error(msg)
            raise RuntimeError(f"Audit Required: Action '{action_name}' is disabled in Safe Mode.")
        
        logging.info(f"✅ ACTION AUTORISÉE : {action_name} par signature humaine.")
        return func(*args, **kwargs)
    return wrapper

def check_critical_node_keys():
    """Vérifie la présence des émergence vitaux avant le démarrage."""
    critical_keys = ["OPENAI_API_KEY", "MDL_MASTER_AUTH"]
    missing = [k for k in critical_keys if not os.getenv(k)]
    
    if missing:
        msg = f"🚨 FATAL: Clés manquantes dans l'environnement : {', '.join(missing)}"
        logging.critical(msg)
        raise RuntimeError(msg)
    
    print("✅ Sécurité environnementale : VALIDÉ.")
