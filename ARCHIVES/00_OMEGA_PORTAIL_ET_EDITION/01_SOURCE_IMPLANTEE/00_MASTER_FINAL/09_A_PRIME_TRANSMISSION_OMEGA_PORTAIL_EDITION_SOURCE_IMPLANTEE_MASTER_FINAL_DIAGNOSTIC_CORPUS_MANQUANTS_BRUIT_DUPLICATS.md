> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** MODULE
> **Position Chiastique :** A'
> **Role du Fichier :** Dossier de diffusion
> **Centre Doctrinal Local :** canal local de diffusion et de synchronisation
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** portee de diffusion et memoisation utile
> - **β :** perte de fidelite et dispersion
> - **κ :** cout de packaging et de synchronisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** A / 00_OMEGA_PORTAIL_ET_EDITION
STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 



AUDIT: CERTIFIED 2026-04-06



---



# Diagnostic du corpus







## Statut Actuel



- Le corpus est maintenant indexe de maniere plus fiable, avec un suivi explicite des doublons, des couches derivees et des fichiers versionnes.



- Le noyau `04_X_NOYAU_MEMOIRE` dispose d'une entree lisible via `09_A_PRIME_ROOT_MDL_YNOR_ARCHITECTURE_UNIFIED_MASTER_FINAL_1373DA.md`.



- Les branches `03_C_MOTEURS_ET_DEPLOIEMENT` et `05_C_PRIME_validéTION_ET_TESTS` sont presentes et navigables, mais elles restent fortement surrepresentees par des miroirs et des artefacts generes.







## 1. Ce qui manquait vraiment



- Le probleme principal n'est plus l'absence materielle des branches, mais l'absence d'une lecture de qualite au niveau de l'index.



- Le corpus avait besoin d'un comptage clair des doublons logiques, des couches miroir et des variantes de version.



- Sans cette couche, le lecteur voyait un corpus volumineux mais ne pouvait pas distinguer proprement source, derive et archive.



- Les cartes et les points d'entree doivent donc etre compris comme une hierarchie de lecture, pas comme une simple liste de fichiers.







## 2. Bruit technique a isoler



- Les repertoires techniques `\.git`, `\.venv`, `\.pytest_cache`, `\.uv-cache`, `__pycache__` et `logs` doivent rester hors de la diffusion editoriale.



- Les caches, journaux, copies de build, exports temporaires et dossiers miroir ne doivent pas etre comptes comme du contenu canonique.



- Dans certaines branches, le bruit vient surtout des copies textuelles automatiques de fichiers binaires, des `../../02_MIROIR_TEXTUEL/01_TECHNICAL_CORE/01_A_MIROIR_OMEGA_PORTAIL_EDITION_MIROIR_TEXTUEL_TECHNICAL_CORE_04_06_MD.md`, des `../../../02_B_THEORIE_ET_PREUVES/09_PDF_CONSTITUTION_MATH_AUGMENTES/MDL_Ynor_Framework/03_C_CONSTITUTION_B_THEORIE_PREUVES_PDF_3_FRACTALE_E3672E.md`, des `../../02_MIROIR_TEXTUEL/00_CORPUS_AUDIT/01_A_AUDIT_OMEGA_PORTAIL_EDITION_MIROIR_TEXTUEL_CORPUS_AUDIT_CORPUS_AUDIT_JSON.md` et des `09_A_PRIME_ROOT_MDL_YNOR_ARCHITECTURE_UNIFIED_MASTER_FINAL_1373DA.md`.



- Ce bruit n'est pas forcement une erreur si le corpus sert d'archive de travail, mais il doit etre balise comme derive.







## 3. Doublons et variantes



- Le scan global actuel du depot montre `1 784` fichiers.



- `129` groupes de hachages sont dupliques, pour `367` entrees impliquees, soit `20,6 %` du corpus scanne.



- `23` fichiers sont redactes comme sensibles.



- `150` fichiers sont marques comme versionnes ou fortement historises.



- La vraie dette de maintenance est donc la consolidation des copies, la nomination canonique et la separation visible entre source, miroir et export.



- La valeur academique ne doit pas etre deduite de la seule masse documentaire: elle depend aussi de la verification externe, encore limitee a ce stade.







## 4. Ce qu'il faut normaliser



- Une seule source canonique par document.



- Une seule version miroir textuelle par source, avec alias si necessaire.



- Une separation stable entre diffusion publique, travail interne et archive.



- Une normalisation d'encodage et de typographie pour tous les points d'entree publics.







## Conclusion



- Le corpus est dense et exploitable.



- Les faiblesses restantes sont surtout la redondance, la surcharge de versions et le melange des couches.



- La correction utile n'est pas de supprimer l'historique, mais de le rendre lisible, mesurable et filtrable.



- La couche de preuve interne est solide; la validation externe reste a renforcer.







## Priorites recommandees



- Marquer explicitement les couches miroir et les exports comme derives.



- Stabiliser une source canonique par document.



- Exposer les doublons et les versions dans les tableaux de bord et les API.



- Continuer l'harmonisation typographique des fichiers publics.







## Remediation Appliquee



- La vue par defaut de l'API et de l'accueil utilise maintenant le corpus canonique dedoublonne.



- Les fichiers derives, les versions et les miroirs restent accessibles pour audit, mais ils ne polluent plus la lecture principale.



- Un endpoint de clusters de doublons permet de retrouver les repetitions du corpus brut sans les confondre avec la vue canonique.



- Les totaux visibles distinguent desormais le corpus source, le corpus canonique et la charge d'archive.
