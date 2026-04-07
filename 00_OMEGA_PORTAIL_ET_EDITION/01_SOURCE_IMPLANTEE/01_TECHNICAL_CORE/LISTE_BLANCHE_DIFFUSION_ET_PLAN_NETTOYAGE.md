---

STATUS: CANONICAL | V11.14.0 | SOURCE: UNIFIED | 

AUDIT: CERTIFIED 2026-04-06

---

# LISTE BLANCHE DE DIFFUSION ET PLAN DE NETTOYAGE

## Objet

Ce document fixe deux choses:

1. ce qui peut sortir dans une diffusion propre

2. ce qui doit rester interne, technique ou archive

Il sert de garde-fou pour eviter de melanger corpus editorial, artefacts de travail et caches d'execution.

## Liste Blanche De Diffusion

### Niveau Public

- `02_PUBLIC_LITERATURE/README.md`

- `02_PUBLIC_LITERATURE/REFERENCE_PUBLIQUE.md`

- `00_HOMEPAGE/HOMEPAGE_DU_CORPUS.md`

- `00_HOMEPAGE/SITE_MAP.md`

- `02_PUBLIC_LITERATURE/PUBLIC_BRIEF.md`

- `02_PUBLIC_LITERATURE/PRESENTATION_PUBLIQUE.md`

### Niveau Executive

- `00_EXECUTIVE_DIGEST/EXECUTIVE_DIGEST.md`

- `00_EXECUTIVE_DIGEST/FICHE_UNE_PAGE.md`

### Niveau Canonique

- `00_EDITION_CANONIQUE_FINALE/PORTAIL_CANONIQUE_FINAL.md`

- `00_EDITION_CANONIQUE_FINALE/01_DOCUMENTS_CENTRAUX/INDEX_MAITRE_YNOR.md`

- `00_EDITION_CANONIQUE_FINALE/01_DOCUMENTS_CENTRAUX/CARTE_VISUELLE_YNOR.md`

### Niveau Master

- `01_TECHNICAL_CORE/README.md`

- `INDEX_MAITRE_YNOR.md`

- `CARTE_VISUELLE_YNOR.md`

- `RECAPITULATION_FINALE.md`

- `MANIFESTE_YNOR.md`

- `NETTOYAGE_TECHNIQUE.md`

- `NORMALISATION_CANONIQUE.md`

### Niveau Soumission

- `00_ACADEMIC_SUBMISSION/MANUSCRIT_FINAL.md`

- `00_ACADEMIC_SUBMISSION/MANUSCRIT_FINAL_FOUNDATIONS_OF_PHYSICS.md`

- `00_ACADEMIC_SUBMISSION/LETTRE_DE_COUVERTURE.md`

- `00_ACADEMIC_SUBMISSION/JOURNAL_TARGETING.md`

- `00_ACADEMIC_SUBMISSION/METADONNEES_SOUMISSION.md`

- `00_ACADEMIC_SUBMISSION/RESUME_DE_SOUMISSION.md`

- `00_ACADEMIC_SUBMISSION/STRUCTURE_DE_LIVRAISON.md`

### Branches Documentaires A Garder Dans La Diffusion

- `01_A_FONDATION`

- `02_B_THEORIE_ET_PREUVES`

- `03_C_MOTEURS_ET_DEPLOIEMENT`

- `04_X_NOYAU_MEMOIRE`

- `05_C_PRIME_VALIDATION_ET_TESTS`

- `06_B_PRIME_GOUVERNANCE_ET_DIFFUSION`

- `07_A_PRIME_ARCHIVES_ET_RELEASES`

## Hors Diffusion

### Artefacts Techniques

- `.git`

- `.venv`

- `.pytest_cache`

- `.uv-cache`

- `__pycache__`

- `*.pyc`

- `*.log`

- `*.tmp`

### Journaux Et Traces

- `logs`

- tout fichier de trace ou de runtime non editorial

### Miroirs Techniques

- les copies textuelles de caches, logs et artefacts de build

- les exports derives (`*.md.md`, `*.pdf.md`, `*.json.md`, `*.fractale.md`) quand ils ne sont pas destines a la diffusion publique

## Plan De Nettoyage

### Étape 1 - Isolation

- Marquer explicitement les repertoires techniques comme hors diffusion.

- Eviter de les compter dans les statistiques documentaires.

- Les conserver seulement dans les zones d'archive ou de travail interne.

### Étape 2 - Separation

- Distinguer corpus editorial et outillage.

- Ne pas melanger sources, caches, logs et environnements d'execution dans les inventaires publics.

- Conserver une frontiere nette entre texte publie et texte de travail.

### Étape 3 - Normalisation

- Garder une seule source canonique par document.

- Harmoniser les noms visibles et les encodages.

- Marquer explicitement les variantes versionnees, historisees et canonique comme derives.

### Étape 4 - Filtrage

- Exclure les caches Python, les environnements virtuels et les journaux des packages de diffusion.

- Retirer les fichiers temporaires et les reliquats de build des dossiers publics.

- Verifier que les manifests ne comptent que le contenu editorial utile.

### Étape 5 - Verification

- Refaire un scan des couches visibles apres nettoyage.

- Verifier qu'aucun `__pycache__`, `.venv`, `.pytest_cache`, `.uv-cache`, `.git` ou `logs` ne remonte dans la diffusion.

- Confirmer que les points d'entrée publics restent lisibles et coherents.

## Regle Pratique

Si un fichier sert a executer, tester, compiler, journaliser ou mettre au point le corpus, il reste interne.

Si un fichier sert a lire, comprendre, diffuser ou remettre le corpus, il peut entrer dans la liste blanche.

## Synthese

- Diffusion: documents de lecture, d'index, de navigation, de synthese et de soumission.

- Interne: caches, logs, environnements virtuels, depots embarques, fichiers temporaires et artefacts techniques.

