---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-016
concept_id: MDLYNOR.SUPPORT.INDEX_AND_READING_ORDER
citation_id: MDLYNOR-RAGSUP-016
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 0.92
---

# Index and reading order

Query anchors:
- Quelle est la fonction de l index canonique ?
- Quelle fiche donne l ordre de lecture canonique ?
- Quel est l ordre de lecture canonique recommande ?

Question:
- What does the canonical index do?

Answer:
- It gives the canonical reading order.
- It routes the reader toward the right sheet.
- It should not monopolize retrieval when a more specific sheet exists.

Canonical citations:
- `MDLYNOR-CANON-INDEX-001`
- `MDLYNOR-CANON-001`
- `MDLYNOR-CANON-006`

Resolution rule:
- Use the index for routing, then jump to the specific concept sheet.
