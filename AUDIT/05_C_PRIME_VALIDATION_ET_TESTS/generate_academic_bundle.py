# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** D
# **Rôle du Fichier :** Moteur de generation
# **Centre Doctrinal Local :** AI Manager garde moteur de generation en limitant le bruit local et la friction structurelle.
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

import zipfile

from datetime import datetime



# MDL YNOR ACADEMIC - AUTOMATED SUBMISSION BUNDLER

# V11.13.0 (Ω Phase)



def create_bundle():

    print("--- YNOR ACADEMIC : GÉNÉRATION DU PACK DE SOUMISSION ---")

    

    timestamp = datetime.now().strftime("%Y%m%d_%H%M")

    bundle_name = f"YNOR_ACADEMIC_SUBMISSION_{timestamp}.zip"

    

    # Paths to include

    targets = [

        "00_EDITION_CANONIQUE_FINALE",

        "02_B_THEORIE_ET_PREUVES",

        "03_C_MOTEURS_ET_DEPLOIEMENT",

        "MDL_YNOR_V7_1_DISTRIBUTION",

        "README.md",

        "LICENSE",

        "PORTAIL_CANONIQUE_FINAL.md"

    ]

    

    with zipfile.ZipFile(bundle_name, 'w', zipfile.ZIP_DEFLATED) as zipf:

        for t in targets:

            if os.path.isfile(t):

                zipf.write(t)

                print(f" [+] Fichier ajout: {t}")

            elif os.path.isdir(t):

                for root, dirs, files in os.walk(t):

                    # Skip git and cache

                    if '.git' in root or '__pycache__' in root:

                        continue

                    for file in files:

                        filepath = os.path.join(root, file)

                        zipf.write(filepath)

                print(f" [V] Dossier consolid: {t}")



    print(f"\n[SUCCÈS] Pack de soumission gnr: {bundle_name}")

    print("Le fichier est prêt pour l'envoi aux comits de lecture (Nature, Science, etc.).")



if __name__ == "__main__":
    try:
        create_bundle()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
