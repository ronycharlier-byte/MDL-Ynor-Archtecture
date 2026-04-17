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

import os



def execute_purge():

    # 1. Purge des Doublons (via report)

    data = {}

    if os.path.exists('collapse_report.json'):

        with open('collapse_report.json', 'r') as f:

            data = json.load(f)

    

    duplicates = data.get('duplicate_list', [])

    purged_count = 0

    

    print(f"=== DÉBUT DE LA PURGE DE DENSIFICATION (V11.13.x) ===")

    

    # Suppression des doublons lists

    for item in duplicates:

        path = os.path.normpath(item['duplicate'])

        try:

            if os.path.exists(path):

                os.remove(path)

                print(f"[PURGE] Doublon : {path} -> EFFACÉ")

                purged_count += 1

        except Exception as e:

            print(f"[ERREUR] Impossible de supprimer {path}: {e}")



    # 2. Nettoyage Chirurgical des Rsidus (Untitled / Sans titre)

    print(f"\n--- NETTOYAGE DES RÉSIDUS (ROOT) ---")

    residue_patterns = ["Sans titre", "Untitled"]

    

    for filename in os.listdir('.'):

        if any(pattern in filename for pattern in residue_patterns):

            if os.path.isfile(filename):

                try:

                    os.remove(filename)

                    print(f"[CLEANUP] Rsidu : {filename} -> ÉLIMINÉ")

                    purged_count += 1

                except Exception as e:

                    print(f"[ERREUR] Impossible d'liminer {filename}: {e}")

            

    print(f"\n=== OPÉRATION TERMINÉE : {purged_count} ÉLÉMENTS PURGÉS ===")

    print(f"STATUT : CORPUS DENSISIÉ ET PURIFIÉ.")

    return purged_count





if __name__ == "__main__":
    try:
        execute_purge()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
