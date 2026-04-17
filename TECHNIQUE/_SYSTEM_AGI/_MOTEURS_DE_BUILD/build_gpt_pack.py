# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur de construction
# **Centre Doctrinal Local :** AI Manager garde moteur de construction en limitant le bruit local et la friction structurelle.
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
# **Lien Miroir :** E

out = r'C:\Users\ronyc\Desktop\MDL_YNOR_GPT_PACK_V11_13'
os.makedirs(out, exist_ok=True)

base = r'C:\Users\ronyc\Desktop\MDL Ynor'

files = [
    (base + r'\_SYSTEM_AGI\INDEX_MAITRE_FRACTAL_CHIASTIQUE.md',                                                       'INDEX_MAITRE_FRACTAL_CHIASTIQUE.md'),
    (base + r'\_SYSTEM_AGI\RECAPITULATION_FINALE.md',                                                                 'RECAPITULATION_FINALE.md'),
    (base + r'\_SYSTEM_AGI\manifeste_fractal_chiaste_universel.json',                                                 'manifeste_fractal_chiaste_universel.json'),
    (base + r'\01_A_FONDATION\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\YNOR_FULL_CORPUS_FORMAL_SPEC_V2.3.md',          'YNOR_FORMAL_SPEC_V11_13_0.md'),
    (base + r'\08_OMEGA_PRIME_API_REFERENCE\01_SOURCE_IMPLANTEE\08_X_API_REFERENCE\openapi.json',                    'openapi_v11_13_0.json'),
    (base + r'\03_C_MOTEURS_ET_DEPLOIEMENT\app.py',                                                                   'app.py'),
    (base + r'\05_C_PRIME_VALIDATION_ET_TESTS\check_chiastic_symmetry.py',                                           'check_chiastic_symmetry.py'),
    (base + r'\05_C_PRIME_VALIDATION_ET_TESTS\chiastic_audit_report.json',                                           'chiastic_audit_report.json'),
]

for src, dst in files:
    shutil.copy2(src, os.path.join(out, dst))
    print(f'OK -> {dst}')

readme = (
    "# MDL YNOR GPT UPLOAD PACK V11.13.0\n\n"
    "## Corpus canonique — 181 entrees DEFINITIVES\n\n"
    "| Noeud | Count |\n"
    "|---|---|\n"
    "| A  | 01_A_FONDATION | 2 |\n"
    "| B  | 02_B_THEORIE_ET_PREUVES | 43 |\n"
    "| C  | 03_C_MOTEURS_ET_DEPLOIEMENT | 26 |\n"
    "| X  | 04_X_NOYAU_MEMOIRE | 8 |\n"
    "| C' | 05_C_PRIME_VALIDATION_ET_TESTS | 28 |\n"
    "| B' | 06_B_PRIME_GOUVERNANCE_ET_DIFFUSION | 43 |\n"
    "| A' | 07_A_PRIME_ARCHIVES_ET_RELEASES | 31 |\n"
    "| TOTAL | 181 |\n\n"
    "Somme : 2+43+26+8+28+43+31 = 181 entrees canoniques DEFINITIVES\n\n"
    "## Tolerances canoniques declarees\n\n"
    "| Asymetrie | Justification | Statut |\n"
    "|---|---|---|\n"
    "| A=2 vs A'=31 | A=fondation minimale, A'=archives cumulatives | INTENTIONNEL ✅ |\n"
    "| C=26 vs C'=28 | C'=validation, +2 artefacts d'audit | INTENTIONNEL ✅ |\n"
    "| B=43 vs B'=43 | Symetrie parfaite | PARFAIT ✅ |\n\n"
    "## Fichiers inclus\n\n"
    "| Fichier | Role |\n"
    "|---|---|\n"
    "| INDEX_MAITRE_FRACTAL_CHIASTIQUE.md | Index canonique 181 entrees verifiees |\n"
    "| RECAPITULATION_FINALE.md | Centre X = 04_X_NOYAU_MEMOIRE |\n"
    "| manifeste_fractal_chiaste_universel.json | Cardinalites reelles (181) |\n"
    "| YNOR_FORMAL_SPEC_V11_13_0.md | Spec + 7 endpoints + tolerances |\n"
    "| openapi_v11_13_0.json | Schema API 7 endpoints |\n"
    "| app.py | Serveur mu reel calcule |\n"
    "| check_chiastic_symmetry.py | mu = alpha - beta - kappa |\n\n"
    "## Instructions upload\n"
    "1. GPT -> Configure -> Knowledge -> supprimer anciens fichiers\n"
    "2. Uploader les 7 fichiers de ce dossier\n"
    "3. Cliquer Save\n"
    "4. Ouvrir NOUVELLE conversation\n"
    "5. Tester : Auditer la coherence du corpus\n\n"
    "## Version\n"
    "Pack V11.13.0 FINAL — 2026-04-07\n"
    "mu_global cible = 1.0 (Point Fixe Omega)\n"
    "Entrees canoniques = 181 (DEFINITIF — ne pas modifier)\n"
)
with open(os.path.join(out, 'README_UPLOAD.md'), 'w', encoding='utf-8') as f:
    f.write(readme)
print('OK -> README_UPLOAD.md')

shutil.make_archive(out, 'zip', out)
print(f'\nZIP => {out}.zip')
print('DONE')
