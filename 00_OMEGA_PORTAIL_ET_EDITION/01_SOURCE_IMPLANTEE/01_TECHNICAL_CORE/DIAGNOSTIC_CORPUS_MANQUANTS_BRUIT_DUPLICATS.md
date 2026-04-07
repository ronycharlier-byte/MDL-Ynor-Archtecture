---

STATUS: CANONICAL | V11.14.1 | SOURCE: UNIFIED

AUDIT: CERTIFIED 2026-04-06

---

# Diagnostic du corpus

## Statut actuel

- Le corpus visible est maintenant indexe de maniere plus fiable.
- La derniere passe de scan sur l'arborescence visible ne trouve plus de doublons exacts.
- La distinction entre source, derive et archive reste utile pour la lecture, mais elle ne signale plus de duplication binaire identique dans le corpus courant.

## 1. Ce qui etait le vrai probleme

- Le probleme principal n'etait pas l'absence de contenu, mais l'absence d'une lecture claire de la hierarchie documentaire.
- Sans cette couche, le lecteur voyait un corpus volumineux sans pouvoir distinguer proprement source, derive et archive.
- Les cartes et les points d'entree doivent donc etre compris comme une hierarchie de lecture, pas comme une simple liste de fichiers.

## 2. Bruit technique a isoler

- Les repertoires techniques `.git`, `.venv`, `.pytest_cache`, `.uv-cache`, `__pycache__` et `logs` doivent rester hors de la diffusion editoriale.
- Le corpus comporte encore des exports derives, des fichiers de travail et des artefacts de build, mais ils ne constituent plus des doublons exacts dans le scan courant.
- Ces artefacts doivent etre balises comme derives.

## 3. Etat des doublons

- Le scan complet actuel sur l'arborescence visible montre `1106` fichiers et `1106` hachages uniques.
- Le nombre de groupes de doublons exacts est donc `0`.
- Les duplications historiques les plus structurantes etaient les familles d'axiomes, de protocoles, de miroirs de release, d'exports JSON/TEX synchronises et de certains index de rediffusion.
- Ces familles ont ete consolidees ou reliees par la carte canonique.

## 4. Triage prioritaire

- Conserver un seul representant canonique par famille.
- Archiver les miroirs, variantes de release et exports synchrones comme derives, pas comme points d'entree.
- Familles historiquement prioritaires a dedoublonner logiquement:
  - `PROTOCOLES_YNOR.md` comme source unique pour la famille `PROTOCOLES_*`.
  - `AXIOMES_YNOR.md` comme source unique pour la famille `AXIOMES_*`.
  - `Procfile`, `index_meta.json`, `mdl_global_knowledge.json`, `MDL_Ynor_Dynamic_Systems_Paper.tex`, `MDL_Ynor_NeurIPS_Submission.tex` et `Sovereign_Global_Knowledge.json` comme couples ou miroirs a maintenir en archive uniquement.
  - Les exports `*.fractale.md`, `*.fractale_augmente.tex`, `*.json.fractale.md` et `*.md.md` comme artefacts derives, jamais comme lecture principale.

## 5. Ce qu'il faut normaliser

- Une seule source canonique par document.
- Une separation stable entre diffusion publique, travail interne et archive.
- Une normalisation d'encodage et de typographie pour tous les points d'entree publics.

## Conclusion

- Le corpus est dense et exploitable.
- Les faiblesses restantes sont surtout la surcharge de versions et le melange des couches, pas la duplication exacte.
- La correction utile n'est plus de supprimer l'historique, mais de le rendre lisible, mesurable et filtrable.
- La couche de preuve interne est solide; la validation externe reste a renforcer.

## Priorites recommandees

- Stabiliser une source canonique par document.
- Exposer les derives et les archives dans les tableaux de bord et les API.
- Continuer l'harmonisation typographique des fichiers publics.

## Remediation appliquee

- La vue par defaut de l'API et de l'accueil utilise maintenant le corpus canonique.
- Un endpoint de clusters de derives permet de retrouver les repetitions historiques du corpus brut sans les confondre avec la vue canonique.
- Les totaux visibles distinguent desormais le corpus source, le corpus canonique et la charge d'archive.
- La carte canonique des doublons est disponible dans [CANONICAL_DUPLICATES_MAP.md](../00_EDITION_CANONIQUE_FINALE/CANONICAL_DUPLICATES_MAP.md).

