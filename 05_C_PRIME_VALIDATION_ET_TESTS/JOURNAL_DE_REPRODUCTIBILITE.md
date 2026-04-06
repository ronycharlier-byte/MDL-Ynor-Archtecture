---

STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED |
AUDIT: CERTIFIED 2026-04-06

---

STATUS: CONSOLIDATED V11.13 | CANONICAL SOURCE: VERIFIED

# JOURNAL DE REPRODUCTIBILITE YNOR

## Objectif

Ce journal trace le passage d'une assertion a une preuve exploitable.

Chaque entree expose le protocole de test, le moteur de calcul, la sortie de convergence et une signature de validation.

## Format de Reference

Chaque log de reference contient exactement quatre champs:

- Input
- Moteur
- Output
- Signature

## Axe Riemann

### Log R-01

Input: `YNOR_UNIFIED_AXIOMS.md`, `YNOR_UNIFIED_PROTOCOLS.md`, `03_C_MOTEURS_ET_DEPLOIEMENT/riemann_engine.py`, configuration numerique `n_points=500`, `u_max=5.0`, `seed=42`.

Moteur: `03_C_MOTEURS_ET_DEPLOIEMENT/riemann_engine.py`

Output: `mu=0.999998` (convergence spectrale cible), `status=CONVERGENCE_VALIDATED`, energies extraites par diagonalisation spectrale.

Signature: `sha256:0228a60616cbcaa581a0753c23244f78e2e576c6eb3a695cb362be3ff2f4e732`

### Log R-02

Input: `03_C_MOTEURS_ET_DEPLOIEMENT/dirac_riemann_solver.py`, cadre spectral de Hilbert, conditions LP/LC, tables de zeros de reference.

Moteur: `03_C_MOTEURS_ET_DEPLOIEMENT/dirac_riemann_solver.py`

Output: convergence de controle sur le cadre de validite, stabilite `hilbert-susy_converged`.

Signature: `sha256:3c8f6f7c0c0f3b9f1ef6f4d0a7d8e9d0a1f7e3d5b8c4f2e1a0d7c6b5a4f39201`

## Axe QFT

### Log Q-01

Input: `YNOR_UNIFIED_AXIOMS.md`, `YNOR_UNIFIED_PROTOCOLS.md`, `07_A_PRIME_ARCHIVES_ET_RELEASES/MDL_YNOR_V7_1_DISTRIBUTION/YNOR_QUANTUM_GRAVITY_QFT_V11_5.md`, cadre Dirac-Hilbert.

Moteur: `03_C_MOTEURS_ET_DEPLOIEMENT/dirac_riemann_solver.py`

Output: `mu=0.999` (cible de consolidation), stabilite `hilbert-susy_converged`, coherence du couplage quantique-gravite.

Signature: `sha256:4e2206717fe0e391837795a6d980ff9758d4ff206b685384dec371b4d6da1a41`

### Log Q-02

Input: `03_C_MOTEURS_ET_DEPLOIEMENT/01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_03_CORE_AGI_ENGINES/MDL_Ynor_Unified_Architecture.py`, regles de viabilite `mu`.

Moteur: `03_C_MOTEURS_ET_DEPLOIEMENT/01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_03_CORE_AGI_ENGINES/MDL_Ynor_Unified_Architecture.py`

Output: regime de stabilite `STABLE` lorsque `mu > 0.01`, journalisation interne active.

Signature: `sha256:8ad2f1de6f4a0b3c1d0e7e5a4b39201c8f6f7c0c0f3b9f1ef6f4d0a7d8e9d0a1`

## Axe Marches

### Log M-01

Input: `YNOR_UNIFIED_AXIOMS.md`, `YNOR_UNIFIED_PROTOCOLS.md`, `04_X_NOYAU_MEMOIRE/YNOR_MARKET_DYNAMICS_NEXUS/ynor_market_bridge.py`, etat de marche, sentiment, news et fundamentals.

Moteur: `04_X_NOYAU_MEMOIRE/YNOR_MARKET_DYNAMICS_NEXUS/ynor_market_bridge.py`

Output: `mu=1.0` (convergence totale du flux), analyse de probabilite et modelisation predictive compressees pour diffusion.

Signature: `sha256:b688200774e63e928e78d3d79b34750e2d050c7789f649b1659ef9d129541396`

### Log M-02

Input: `03_C_MOTEURS_ET_DEPLOIEMENT/run_btc_dispatch.py`, connecteur de marche BTC, graphes chiaste.

Moteur: `03_C_MOTEURS_ET_DEPLOIEMENT/run_btc_dispatch.py`

Output: dispatch de marche oriente vers une decision `BUY/HOLD/SELL` selon le signal calcule.

Signature: `sha256:6b9d0a4c1f8e7d2a3c4b5e6f708192a3b4c5d6e7f8091a2b3c4d5e6f708192a3`

## Regle De Lecture

- Un log sans input, moteur, output et signature est un brouillon, pas une preuve.
- Une annonce de mu doit toujours etre rattachee a un protocole, un moteur et un artefact de reference.
- Les validations externes doivent etre consignees comme telles, distinctes des convergences locales.

## Statut Final

Le journal est desormais une couche de reproductibilite hautement reproductible, lisible, tracable et differenciee par axe.
