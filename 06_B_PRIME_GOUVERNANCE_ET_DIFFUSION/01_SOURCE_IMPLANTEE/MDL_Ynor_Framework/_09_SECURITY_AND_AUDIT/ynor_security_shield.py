﻿# =============================================================================
# 🛡️ MDL YNOR - SECURITY SHIELD (DEFCON 1)
# =========================
# Verrouillage centralisdes capacits d'auto-modification et audit trail.
# =============================================================================
import os
import time
import logging

# Configuration du Shield
# SAFE_MODE = True par dfaut. Ncessite MDL_ALLOW_MUTATION=TRUE pour dsactiver.
SAFE_MODE = os.getenv("MDL_SAFE_MODE", "TRUE").upper() == "TRUE"

# Configuration Logging Audit
logging.basicConfig(
    filename='mdl_security_audit.log',
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | SHIELD: %(message)s'
)

def require_human_approval(func):
    """Dcorateur pour empêcher toute auto-modification sans autorisation explicite."""
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

def check_critical_secrets():
    """Vrifie la prsence des secrets vitaux avant le dmarrage."""
    critical_keys = ["OPENAI_API_KEY", "MDL_MASTER_AUTH"]
    missing = [k for k in critical_keys if not os.getenv(k)]
    
    if missing:
        msg = f"🚨 FATAL: Cls manquantes dans l'environnement : {', '.join(missing)}"
        logging.critical(msg)
        raise RuntimeError(msg)
    
    print("✅ Scuritenvironnementale : VALIDÉ.")
