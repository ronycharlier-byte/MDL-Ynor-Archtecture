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

from datetime import datetime



JOURNAL_PATH = "05_C_PRIME_validéTION_ET_TESTS/JOURNAL_DE_REPRODUCTIBILITE.md"

SIGNATURE_PATH = "05_C_PRIME_validéTION_ET_TESTS/JOURNAL_SIGNATURE.json"



def sign_journal():

    if not os.path.exists(JOURNAL_PATH):

        print(f"Erreur : {JOURNAL_PATH} introuvable.")

        return



    with open(JOURNAL_PATH, "rb") as f:

        file_data = f.read()

        file_hash = hashlib.sha256(file_data).hexdigest()



    signature = {

        "timestamp": str(datetime.now()),

        "file": JOURNAL_PATH,

        "sha256": file_hash,

        "status": "IMMUTABLE_CLAIM_SIGNED",

        "signer": "MDL YNOR ENGINE V11.13"

    }



    with open(SIGNATURE_PATH, "w") as f:

        json.dump(signature, f, indent=4)



    print(f"Journal signavec succs : {file_hash}")



import os

if __name__ == "__main__":
    try:
        sign_journal()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
