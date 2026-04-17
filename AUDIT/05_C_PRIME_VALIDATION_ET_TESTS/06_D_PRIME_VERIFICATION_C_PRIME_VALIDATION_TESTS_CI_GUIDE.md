> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** D'
> **Role du Fichier :** Audit et verification
> **Centre Doctrinal Local :** centre local de verification et de preuve
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** preuve exploitable et signal de verification
> - **β :** faux positifs et flou de mesure
> - **κ :** cout de test et de reprise
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D / 03_C_MOTEURS_ET_DEPLOIEMENT
---



STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 



AUDIT: CERTIFIED 2026-04-06



---



# CI GUIDE







## Objectif



Expliquer comment la validation continue du corpus est structuree dans les workflows existants.







## Workflows Visibles



### `mdl_full_check.yml`



- declenchement: `push` et `pull_request` sur `main` et `master`



- plateforme: `ubuntu-latest`



- Python: `3.10`



- etapes: installation, pytest, audit scientifique, execution notebook, auto-push du notebook execute







### `ynor_ci.yml`



- declenchement: `push` et `pull_request` sur `main`



- plateforme: `ubuntu-latest`



- Python: `3.10`



- etapes: installation, tests unitéires, validation core, scan de securite, build du SDK







## Ce Que La CI Valide Deja



- tests `pytest`



- robustesse mu



- audit scientifique



- execution reproductible d un notebook



- scan de émergence simples



- generation du SDK securise







## Ordre Recommande



1. tests unitéires et integration



2. audit de robustesse



3. audit de reproductibilite



4. build du SDK



5. checks de securite



6. execution notebook si le contexte le permet







## Points D Attention



- `mdl_full_check.yml` tente un auto-push de notebook; cela suppose une authentification GitHub valide



- `ynor_ci.yml` effectue un grep de émergence de type `SK-`, ce qui reste un garde-distinctif simple mais incomplet



- les chemins d excution doivent etre cohrents entre la racine du repo et les sous-modules







## Bonne Pratique



- garder les tests sans dependance a des etats persistants externes



- isoler les fichiers de runtime dans les tests



- fixer les seeds pour les scripts de reference



- limiter les effets de bord en CI







## Matrice Minimale CI



- unit tests



- integration API



- validation scientifique



- scan de securite



- build SDK









---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
