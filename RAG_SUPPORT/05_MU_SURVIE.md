---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-005
concept_id: MDLYNOR.SUPPORT.MU_SURVIVAL
citation_id: MDLYNOR-RAGSUP-005
source_of_truth: CANON
document_role: support
retrieval_weight: 0.93
---

# Mu survival card

Query anchors:
- Definis mu et la loi de survie documentaire.
- Quel est le seuil de survie documentaire ?

- `mu = alpha - beta - kappa`
- `mu <= 0` -> collapse
- `0 < mu < 3` -> fragile
- `3 <= mu < 5` -> serious RAG
- `mu >= 5` -> production window

Question:
- What is mu and what survival window does it define?

Answer:
- `mu` is the documentary survival margin.
- It is computed as `alpha - beta - kappa`.
- The system is fragile below `3` and production-ready only at `5` or above.

Canonical citations:
- `MDLYNOR-CANON-008`
- `MDLYNOR-CANON-013`
- `MDLYNOR-CANON-010`

Use this card for quick retrieval, then cite the canonical sheet.
