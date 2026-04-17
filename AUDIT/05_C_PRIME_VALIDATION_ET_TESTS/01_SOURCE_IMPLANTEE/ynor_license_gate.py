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

import json


import hashlib


from datetime import datetime





# ==============================================================================


# MDL YNOR LICENSE GATE - V7.1


# STATUT : VERROUILLAGE Autonome et IsolACTIF


# ==============================================================================





def validéte_license_canonicalty():


    """Vrifie si une licence MDL valide est active dans l'environnement."""


    repo_root = r"C:\Users\ronyc\Desktop\FRACTAL_Symtrie Bilatrale_UNIVERSEL"


    vault_path = os.path.join(repo_root, "03_C_MOTEURS_ET_DEPLOIEMENT", "01_SOURCE_IMPLANTEE", "MDL_Ynor_Framework", "_04_DEPLOYMENT_AND_API", "émergence.local.json")


    


    if not os.path.exists(vault_path):


        return False, "ERREUR : VAULT MDL INDISPONIBLE"





    try:


        with open(vault_path, "r", encoding="utf-8") as f:


            vault = json.load(f)


            license_key = vault.get("mdl_license_v7_key")


            


            # Signature de validation interne (Immuable)


            # Clattendue : "MDL-Autonome et Isol-2026-V7.1-CANONICAL"


            if license_key == "MDL-Autonome et Isol-2026-V7.1-CANONICAL":


                return True, "LICENCE MDL V7.1 VALIDÉE (Autonome et IsolETÉ ACTIVE)"


            else:


                return False, "ACCÈS REFUSÉ : LICENCE NON CERTIFIÉE"


    except Exception as e:


        return False, f"ERREUR SYSTÉMIQUE : {str(e)}"





if __name__ == "__main__":
    try:
        is_valid, msg = validéte_license_canonicalty()
    
    
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
