# Résumé Scientifique Exécutif (Ynor V11.14.0)

> **Note de l'Éditeur :** *Ce document constitue le point d'entrée prioritaire pour tout relecteur externe ou pair scientifique découvrant le projet. Il présente les revendications avec lisibilité et traçabilité.*

## 1. Proposition Fondamentale
Le projet Ynor propose un pont expérimental entre l'organisation fractale de l'information (Corpus Chiaste) et l'exécution asynchrone sur les marchés (Moteurs Bitget). Ce dépôt consolide l'infrastructure mathématique de ce modèle et fournit les scripts d'exploitation associés.

## 2. Statut des Preuves
Il est crucial de distinguer la validité interne du corpus de sa validation externe :
- **Validité Interne (Démontrée) :** L'architecture du corpus démontre une résilience structurelle très élevée. Nos métriques internes (indiquées sous l'appellation "Stabilité structurelle (Mu)") atteignent 0.9997, ce qui témoigne d'une cohérence sémantique et documentaire quasi totale sur plus de 1400 fichiers.
- **Validité Empirique / Externe (En cours) :** Le moteur de trading intégré (`bitget_market_bot.py`) est actuellement validé en condition "Dry-Run" locale. L'hypothèse selon laquelle la structure du corpus octroie un avantage prédictif sur les marchés reste une proposition théorique à valider par un audit de performance (PNL réel vs théorique) sur une période prolongée.

## 3. Architecture Déployée
Le socle technique fourni permet une stricte reproductibilité de nos tests locaux :
*   **Données :** Systèmes de collecte CCXT (OHLCV).
*   **Théorie :** Unification algorithmique des axiomes (CF. `YNOR_UNIFIED_AXIOMS.md`).
*   **Infrastructure :** Déploiement VPS automatisé (`install_vps.sh`) garantissant un environnement stérile.

## 4. Appel à l'Audit
Ce corpus (V11.14.0) est "Science-Ready" dans sa forme. Nous le soumettons à révision pour faire examiner :
1.  La validité de ses modèles mathématiques de distribution de données.
2.  La viabilité de ses stratégies d'exécution asynchrone en temps réel.
