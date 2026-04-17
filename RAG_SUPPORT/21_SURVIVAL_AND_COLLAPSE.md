---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-021
concept_id: MDLYNOR.SUPPORT.SURVIVAL_AND_COLLAPSE
citation_id: MDLYNOR-RAGSUP-021
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 0.94
---

# Survival and collapse

Query anchors:
- Definis mu et la loi de survie documentaire.
- Quel est le seuil de survie documentaire ?
- Que dit le noyau memoire sur le collapse canonique ?
- Quels sont les regimes de stabilite et de cohesion ?

Question:
- What is the survival threshold?

Answer:
- `mu = alpha - beta - kappa`
- `mu <= 0` means collapse
- `0 < mu < 3` means fragile
- `3 <= mu < 5` means serious RAG
- `mu >= 5` means production window

Canonical citations:
- `MDLYNOR-CANON-008`
- `MDLYNOR-CANON-013`
- `MDLYNOR-CANON-005`
- `MDLYNOR-CANON-010`

Resolution rule:
- Lower `mu` amplifies small retrieval errors.
