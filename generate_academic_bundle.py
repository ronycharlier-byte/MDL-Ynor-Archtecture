import os
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
                print(f" [+] Fichier ajouté : {t}")
            elif os.path.isdir(t):
                for root, dirs, files in os.walk(t):
                    # Skip git and cache
                    if '.git' in root or '__pycache__' in root:
                        continue
                    for file in files:
                        filepath = os.path.join(root, file)
                        zipf.write(filepath)
                print(f" [V] Dossier consolidé : {t}")

    print(f"\n[SUCCÈS] Pack de soumission généré : {bundle_name}")
    print("Le fichier est prêt pour l'envoi aux comités de lecture (Nature, Science, etc.).")

if __name__ == "__main__":
    create_bundle()
