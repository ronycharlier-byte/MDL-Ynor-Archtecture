# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** C
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
# **Lien Miroir :** C'

# Root directory of the framework
BASE_DIR = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework"

# Files to synchronize (Source -> Targets)
# We choose the best/most complete version as source
SYNC_PLAN = [
    {
        "src": os.path.join(BASE_DIR, "_01_THEORY_AND_PAPERS", "MDL_YNOR_TECHNICAL_SPECIFICATIONS.md"),
        "targets": [
            os.path.join(BASE_DIR, "_10_YNOR_AI_KNOWLEDGE_BASE_SOURCES", "MDL_YNOR_TECHNICAL_SPECIFICATIONS.md"),
            os.path.join(BASE_DIR, "MDL_YNOR_GPT_KNOWLEDGE", "MDL_YNOR_TECHNICAL_SPECIFICATIONS.md")
        ]
    },
    {
        "src": os.path.join(BASE_DIR, "_01_THEORY_AND_PAPERS", "MDL_YNOR_SCIENTIFIC_WHITE_PAPER.md"),
        "targets": [
            os.path.join(BASE_DIR, "_10_YNOR_AI_KNOWLEDGE_BASE_SOURCES", "MDL_YNOR_SCIENTIFIC_WHITE_PAPER.md"),
            os.path.join(BASE_DIR, "MDL_GPT_KNOWLEDGE_PRODUCTION", "MDL_YNOR_SCIENTIFIC_WHITE_PAPER.md")
        ]
    },
    {
        "src": os.path.join(BASE_DIR, "_PREUVES_ET_RAPPORTS", "BENCHMARK_ULTRA_HARDCORE_ULTIMATE_10_10.md"),
        "targets": [
            os.path.join(BASE_DIR, "_01_THEORY_AND_PAPERS", "BENCHMARK_ULTRA_HARDCORE_ULTIMATE_10_10.md"),
            os.path.join(BASE_DIR, "_10_YNOR_AI_KNOWLEDGE_BASE_SOURCES", "BENCHMARK_ULTRA_HARDCORE_ULTIMATE_10_10.md")
        ]
    }
]

def deep_sync():
    print("--- LANCEMENT DE LA SYNCHRONISATION PROFONDE DU CORPUS ---")
    for task in SYNC_PLAN:
        src = task["src"]
        if not os.path.exists(src):
            print(f"⚠️ Source manquante : {src}")
            continue
            
        for target in task["targets"]:
            os.makedirs(os.path.dirname(target), exist_ok=True)
            shutil.copy2(src, target)
            print(f"✅ Synchronisé : {os.path.relpath(target, BASE_DIR)}")

    print("\n--- SYNCHRONISATION TERMINÉE ---")

if __name__ == "__main__":
    try:
        deep_sync()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
