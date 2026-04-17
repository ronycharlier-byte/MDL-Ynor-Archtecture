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

import shutil



def reorganize_corpus():

    print("=== YNOR CORPUS REORGANIZER (V12.1) ===")

    

    # Configuration du mapping

    mapping = {

        # 00 - Executive & Final

        '00_MASTER_FINAL': ['README.md', 'LICENSE.md', 'YNOR_ACADEMIC_SUBMISSION_20260405_1013.zip', '2026-04-06.md'],

        

        # 01 - Fondation & Seeds

        '01_A_FONDATION': ['core', 'static', 'templates', 'YNOR_KNOWLEDGE_SEED', 'YNOR_KNOWLEDGE_SEED_V11_10_12', 'YNOR_KNOWLEDGE_SEED_V11_13_5', 'YNOR_KNOWLEDGE_SEED_V11_9_3', 'YNOR_KNOWLEDGE_VAULT_V10_8'],

        

        # 02 - Thorie

        '02_B_THEORIE_ET_PREUVES': ['millennium_proof_of_concepts.py'],

        

        # 03 - Moteurs & Dploiement

        '03_C_MOTEURS_ET_DEPLOIEMENT': ['app.py', 'riemann_engine.py', 'run_btc_dispatch.py', 'ynor_geopolitical_tipping_point.py', 'Dockerfile', 'Procfile', 'render.yaml', 'requirements.txt', 'ynor_corpus_optimizer.py', 'ynor_world_critical_audit.py', 'ynor_mega_stress_500k.py', 'ynor_stress_test_50k.py'],

        

        # 04 - Noyau Mmoire

        '04_X_NOYAU_MEMOIRE': ['corpus_index.py', 'mdl_metrics_bridge.py', 'collapse_report.json', 'corpus_optimization_plan.json', 'YNOR_MARKET_DYNAMICS_NEXUS'],

        

        # 05 - validation & Tests

        '05_C_PRIME_validéTION_ET_TESTS': ['tests', 'check_axes_convergence.py', 'check_chiastic_symmetry.py', 'ynor_master_audit.py', 'ynor_fractal_expander.py', 'ynor_execute_purge.py', 'ynor_hyper_stress_5M.py', 'generate_academic_bundle.py', 'ynor_collapse_maximizer.py', 'logs', '__pycache__'],

        

        # 07 - Archives

        '07_A_PRIME_ARCHIVES_ET_RELEASES': ['MDL_YNOR_V7_1_DISTRIBUTION', 'YNOR_MASTER_SHOWCASE', 'YNOR_MAX_EXPLOITATION']

    }

    

    moved_count = 0

    

    # On ajoute le script lui-même la liste de validation

    mapping['05_C_PRIME_validéTION_ET_TESTS'].append('ynor_corpus_reorganizer.py')



    for target_dir_prefix, items in mapping.items():

        # Trouver le vrai nom du dossier (car il peut varier lgrement)

        target_dir = next((d for d in os.listdir('.') if os.path.isdir(d) and d.startswith(target_dir_prefix)), None)

        

        if not target_dir:

            print(f"[ERROR] Dossier cible non trouvpour le prfixe : {target_dir_prefix}")

            continue

            

        print(f"\nMoving to {target_dir}...")

        for item in items:

            if os.path.exists(item):

                try:

                    # Gestion spciale pour ne pas se dplacer soi-même pendant l'excution (si possible)

                    if item == 'ynor_corpus_reorganizer.py':

                        continue 

                        

                    shutil.move(item, os.path.join(target_dir, item))

                    print(f"  [MOVED] {item}")

                    moved_count += 1

                except Exception as e:

                    print(f"  [ERROR] {item} -> {e}")



    print(f"\n=== RÉORGANISATION TERMINÉE : {moved_count} ÉLÉMENTS CLASSÉS ===")

    print("STATUT : RACINE PURIFIÉE.")



if __name__ == "__main__":
    try:
        reorganize_corpus()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
