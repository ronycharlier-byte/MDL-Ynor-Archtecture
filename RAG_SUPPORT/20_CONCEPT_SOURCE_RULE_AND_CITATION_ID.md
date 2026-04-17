---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-020
concept_id: MDLYNOR.SUPPORT.CONCEPT_SOURCE_RULE_AND_CITATION_ID
citation_id: MDLYNOR-RAGSUP-020
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 0.94
---

# Concept source rule and citation id

Query anchors:
- Explique le principe 1 concept = 1 source canonique.
- Que signifie canonical_id ?
- Comment resoudre un citation_id sans ambiguite ?

Question:
- What does one concept = one canonical source mean?

Answer:
- Each concept has one authoritative source.
- `canonical_id` identifies that source.
- `citation_id` identifies the stable citation target.
- `section_id` and `chunk` make the citation resolvable at a fine level.

Canonical citations:
- `MDLYNOR-CANON-014`
- `MDLYNOR-CANON-007`
- `MDLYNOR-CANON-REGISTRY-CITATION-001`

Resolution rule:
- If a duplicate competes with the canonical source, it becomes archive or derivative.
