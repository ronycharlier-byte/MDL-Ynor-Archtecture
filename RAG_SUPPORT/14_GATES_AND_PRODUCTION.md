---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-014
concept_id: MDLYNOR.SUPPORT.GATES_PRODUCTION
citation_id: MDLYNOR-RAGSUP-014
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 0.94
---

# Gates and production

Query anchors:
- Quel est le role des gates de validation ?
- Quelles conditions bloquent la production ?
- Pourquoi la production reste-t-elle bloquee ?
- Quel est le seuil minimal de pertinence production ?
- Quand la production est-elle autorisee ?

Question:
- When can the corpus be called production ready?

Answer:
- Only when the governing gates are all green.
- Citation must be stable and canonical.
- Archive and technical leakage must stay at zero.
- Top-5 pertinence must clear the production threshold.
- No answer is allowed without a valid canonical source.

Canonical citations:
- `MDLYNOR-CANON-007`
- `MDLYNOR-CANON-012`
- `MDLYNOR-CANON-013`
- `MDLYNOR-CANON-015`

Resolution rule:
- If one gate fails, production stays blocked.
