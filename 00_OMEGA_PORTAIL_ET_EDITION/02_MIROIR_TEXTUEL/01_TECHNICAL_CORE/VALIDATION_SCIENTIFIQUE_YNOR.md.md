# MIROIR TEXTUEL - VALIDATION_SCIENTIFIQUE_YNOR.md

```text
---

STATUS: CANONICAL | V11.14.0 | SOURCE: UNIFIED | 

AUDIT: CERTIFIED 2026-04-06

---

STATUS: CONSOLIDATED V11.14.0 | CANONICAL SOURCE: TRUE

# VALIDATION SCIENTIFIQUE YNOR

## Rôle

Ce document définit le statut de preuve attendu pour toute affirmation du corpus.
Il référence le journal de reproductibilité comme registre canonique des validations.

## Canonical Evidence Register

- [JOURNAL_DE_REPRODUCTIBILITE.md](../05_C_PRIME_VALIDATION_ET_TESTS/JOURNAL_DE_REPRODUCTIBILITE.md)

## Échelle de Preuve (Proof Ladder)

- Hypothèse: proposition de travail clairement formulée.
- Preuve interne: dérivation, calcul ou test reproductible dans le dépôt.
- Reproduction locale: exécution indépendante avec mêmes entrées et mêmes sorties attendues.
- Vérification externe: reproduction par un tiers hors dépôt.
- Validation forte: reproduction externe accompagnée d'une lecture critique.

## Contrat de Reproductibilité (Log Contract)

Tout registre de validation doit contenir les quatre éléments suivants:
- Input: données sources, axiomes, hypothèses ou artefacts utilisés.
- Moteur: script Python ou moteur opérationnel responsable.
- Output: valeur de convergence, statut de stabilité, ou effet observé.
- Signature: hash symbolique ou signature déterministe du protocole.

## Précision Requise

- Les valeurs de `mu` doivent être reliées à un moteur, une configuration et un périmètre de test.
- Les stabilités spectrales doivent être rattachées à un protocole de calcul ou à un script.
- Les affirmations de type `mu = 1.0` ne sont recevables que si le journal donne la chaîne de validation complète.

## Règles de Reproductibilité

- Fixer les seeds pour les calculs numériques.
- Documenter les entrées, les sorties et les conditions d'arrêt.
- Conserver les artefacts minimaux permettant la réexécution.
- Distinguer la reproductibilité locale de la vérification externe.
- Marquer explicitement tout bloc déjà reproductible localement.

## Seuils d'Acceptation Scientifiques

- Bloc formalisé: structure logique définie et contrôle interne établi.
- Bloc reproductible localement: protocole exécutable, entrées fixées, sortie stabilisée.
- Bloc scientifiquement consolidé: revue ou reproduction externe disponible.

## Règle d'Usage

Une affirmation scientifique ne doit plus circuler sans sa ligne de journal certifiée.
La validation n'est pas une simple revendication : elle est un contrat de traçabilité.


```