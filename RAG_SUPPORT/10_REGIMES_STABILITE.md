---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-010
concept_id: MDLYNOR.SUPPORT.STABILITY_REGIMES
citation_id: MDLYNOR-RAGSUP-010
source_of_truth: CANON
document_role: support
retrieval_weight: 0.78
---

# Fiche des regimes de stabilite

Query anchors:
- Quels sont les regimes de stabilite et de cohesion ?
- Quel est le seuil de survie documentaire ?
- Quelle est la condition de stabilité exponentielle ou de convergence vers un invariant ?

- `mu <= 0` -> collapse
- `0 < mu < 3` -> fragile
- `3 <= mu < 5` -> serious RAG
- `mu >= 5` -> production window

Question:
- What are the stability regimes and the survival threshold?

Answer:
- `mu <= 0` -> collapse
- `0 < mu < 3` -> fragile
- `3 <= mu < 5` -> serious RAG
- `mu >= 5` -> production window

Canonical citations:
- `MDLYNOR-CANON-013`
- `MDLYNOR-CANON-008`

This card should steer retrieval toward the canonical regime sheet.
It should never monopolize queries about reading order.
