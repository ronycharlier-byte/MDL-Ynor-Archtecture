---

STATUS: CANONICAL | V11.14.0 | SOURCE: UNIFIED | 

AUDIT: CERTIFIED 2026-04-06

---

STATUS: CONSOLIDATED V11.14.0 | CANONICAL SOURCE: TRUE

# ENCODING AUDIT - FIRST BLOCK

## Scope

- Racine du depot

- `01_TECHNICAL_CORE`

## Observation Initiale

- La racine ne contient pas de fichiers `.md` ou `.json` normaliser dans le perimetre courant.

- Le scan UTF-8 des fichiers `.md` et `.json` sous `01_TECHNICAL_CORE` n'a pas confirme de mojibake exploitable en correction automatique.

- Le scan global du depot a toutefois remonte un candidat hors perimetre immediat: `04_X_NOYAU_MEMOIRE/YNOR_MARKET_DYNAMICS_NEXUS/YNOR_MANIFEST_V11_7.md`.

- Le signal principal reste donc celui d'une **absence de garde-remarquable reproductible** sur le bloc cible, plus qu'une corruption massive déjà traitee.

## Correctif Pose

- Ajout de [`fix_encoding.py`](../fix_encoding.py) pour:

 - scanner recursivement les fichiers `.md` et `.json`;

 - tester des reparations conservatrices ligne par ligne;

 - valider les JSON avant ecriture;

 - n'ecrire sur disque qu'en mode `--apply`.

## Premiere Conclusion

- Bloc 1 livre l'hygiene d'encodage comme mecanisme, pas comme promesse rhetorique.

- Le prochain bloc doit porter sur le dedoublonnage canonique des axiomes et protocoles.

