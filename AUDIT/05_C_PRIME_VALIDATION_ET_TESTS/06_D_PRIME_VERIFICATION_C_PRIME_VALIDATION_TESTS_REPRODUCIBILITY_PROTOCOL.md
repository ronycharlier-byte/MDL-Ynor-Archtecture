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



# REPRODUCIBILITY PROTOCOL







## Objectif



Definir comment rejouer les audits du corpus avec un maximum de determinisme.







## Principes



- fixer les graines aleatoires quand le script le permet



- isoler les fichiers temporaires



- garder les entrees de test compactes



- rendre le chemin de travail explicite



- separer les validations deterministes des benchmarks stochastiques







## Protocoles Observes



### validation scientifique



- script: `hardcore_validation.py`



- graine par defaut: `42`



- comportement attendu: `mu` proche de `1.4`







### Experience de mutation



- script: `run_experiment.py`



- graine par defaut: `101`



- comportement attendu: passage d un etat instable a un etat plus stable







### Test d integration partageable



- script: `tests/test_shareable_mu_audit.py`



- stockage isole via `tmp_path`



- comportement attendu: lien public cree et evenements traces







## Point Sensible



Le benchmark global `mdl_ynor_ultimate_benchmark_v3.py` melange des mesures structurelles et des tirages aleatoires pour certaines composantes. Il est donc utile comme audit de tendance, mais pas comme reference numerique parfaitement deterministic sans ajustement supplementaire.







## Procedure Recommandee



1. Fixer `PYTHONHASHSEED` si besoin.



2. Fixer les graines numpy dans les scripts qui le permettent.



3. Isoler les fichiers JSON de runtime dans un repertoire temporaire.



4. Lancer les tests unitéires.



5. Lancer les audits de robustesse.



6. Comparer les resultats avec les sorties de reference.







## Sorties A Conserver



- rapport pytest



- JSON d audit si produit



- traces de benchmark



- journaux d erreur si un test echoue







## Regle D Or



Un test est reproductible seulement si ses donnees, ses graines et son espace d ecriture sont tous controles.









---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
