# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** B'
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
# **Lien Miroir :** B

import numpy as np

import os



def optimize():

    # PATHS

    JSON_PATH = "corpus_index.json"

    META_PATH = "index_meta.json"

    VECT_PATH = "index_vectors.npy"



    if not os.path.exists(JSON_PATH):

        print(f"Erreur: {JSON_PATH} non trouv.")

        return



    print(f"Chargement de {JSON_PATH} (98MB)...")

    with open(JSON_PATH, "r", encoding="utf-8") as f:

        data = json.load(f)



    print(f"Extraction des mtadonnes ({len(data)} vecteurs)...")

    # On ne garde que le texte et le nom du fichier pour les mtadonnes

    meta = [{"text": item["text"], "file": item["file"]} for item in data]

    

    print(f"Formatage de la matrice d'embeddings...")

    # On convertit les listes de floats en un array numpy (Float32 pour conomiser 50% vs Float64)

    vectors = np.array([item["embedding"] for item in data], dtype=np.float32)



    print(f"Sauvegarde des mtadonnes dans {META_PATH}...")

    with open(META_PATH, "w", encoding="utf-8") as f:

        json.dump(meta, f, ensure_ascii=False)



    print(f"Sauvegarde des vecteurs dans {VECT_PATH}...")

    np.save(VECT_PATH, vectors)



    print("OPTIMISATION COMPLÉTÉE (Total Diamond Memory Optimization)")

    print(f"Taille finale Meta: {os.path.getsize(META_PATH)/1024/1024:.2f} MB")

    print(f"Taille finale Vect: {os.path.getsize(VECT_PATH)/1024/1024:.2f} MB")



if __name__ == "__main__":
    try:
        optimize()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
