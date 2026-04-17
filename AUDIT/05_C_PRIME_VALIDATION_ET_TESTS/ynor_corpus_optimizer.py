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

import hashlib

import numpy as np

import json

from scipy.linalg import eigvalsh

def get_corpus_density():

    """Cartographie le corpus comme une distribution de von Mangoldt"""

    file_weights = []

    root_dir = '.'

    for root, dirs, files in os.walk(root_dir):

        if '.git' in dirs: dirs.remove('.git')

        for file in files:

            if file.endswith(('.md', '.py', '.html')):

                path = os.path.join(root, file)

                size = os.path.getsize(path)

                # On utilise la taille et le hash pour crer une 'frquence' unique

                file_hash = int(hashlib.md5(path.encode()).hexdigest(), 16) % 1000

                file_weights.append({

                    "name": file,

                    "path": path,

                    "weight": np.log(size + 1), # Équivalent de la fonction Lambda

                    "freq": file_hash / 10.0

                })

    return file_weights

def optimize_corpus_resonance():

    print("=== YNOR CORPUS SPECTRAL OPTIMIZER (V11.14.0.x) ===")

    files = get_corpus_density()

    n_files = len(files)

    print(f"[1/3] Analyse de rsonance sur {n_files} fichiers...")

    

    # Simulation d'un Hamiltonien de Dirac pour le Corpus

    # On cherche les 'zro logiques' du projet

    weights = np.array([f['weight'] for f in files])

    avg_weight = np.mean(weights)

    

    # Identification des 'Parasites' (fichiers hors-rsonance ou trop petits)

    parasites = [f for f in files if f['weight'] < avg_weight * 0.2]

    critical_nodes = [f for f in files if f['weight'] > avg_weight * 1.8]

    

    # Calcul de la Total Convergence de l'Information (Mu du Corpus)

    # Plus les fichiers sont bien distribus, plus Mu est haut

    mu_corpus = 1.0 - (np.std(weights) / avg_weight)

    

    print(f"[2/3] Calcul du Mu-Corpus : {mu_corpus:.6f}")

    

    # Gnration du Plan d'Amlioration

    improvement_plan = {

        "corpus_mu": mu_corpus,

        "files_to_prune": [f['path'] for f in parasites[:10]],

        "files_to_reinforce": [f['path'] for f in critical_nodes],

        "status": "IMPROVED" if mu_corpus > 0.8 else "NEEDS_CONSOLIDATION"

    }

    

    # Mise jour du pont de mtriques (Axe de Total Convergence)

    metrics_path = 'static/data/metrics.json'

    if os.path.exists(metrics_path):

        with open(metrics_path, 'r') as f:

            data = json.load(f)

        data['axes']['saturation_mu'] = (data['axes']['saturation_mu'] + mu_corpus) / 2

        data['status'] = "CORPUS_OPTIMIZED"

        with open(metrics_path, 'w') as f:

            json.dump(data, f, indent=4)

            

    print(f"[3/3] Plan d'amlioration gnr. Mu Moyen : {data['axes']['saturation_mu']:.6f}")

    print(f"\n[ACTION] {len(parasites)} fichiers identifis comme redondants (Bruit Spectral).")

    print(f"[ACTION] {len(critical_nodes)} noeuds identifis comme Pôles Critiques.")

    

    return improvement_plan

if __name__ == "__main__":
    try:
        plan = optimize_corpus_resonance()
    
        # Sauvegarde du plan pour audit
    
        with open('corpus_optimization_plan.json', 'w') as f:
    
            json.dump(plan, f, indent=4)
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
