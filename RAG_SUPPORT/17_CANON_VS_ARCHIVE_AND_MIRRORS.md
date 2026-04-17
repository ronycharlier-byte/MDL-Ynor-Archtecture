---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-017
concept_id: MDLYNOR.SUPPORT.CANON_VS_ARCHIVE
citation_id: MDLYNOR-RAGSUP-017
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 0.92
---

# Canon vs archive and mirrors

Query anchors:
- Quelle difference entre canon et archive ?
- Pourquoi les miroirs doivent-ils etre exclus du retrieval principal ?
- Quel est le comportement attendu des doublons non canoniques ?

Question:
- What is the difference between canon and archive?

Answer:
- CANON is authoritative.
- ARCHIVES preserve historical versions, releases and logs.
- Mirrors and duplicates are not first-rank doctrine.
- Non-canonical duplicates are relabeled as archive or derivative.

Canonical citations:
- `MDLYNOR-CANON-015`
- `MDLYNOR-CANON-REGISTRY-CITATION-001`
- `MDLYNOR-CANON-REGISTRY-LAYERS-001`

Resolution rule:
- If a source competes with canon, it leaves the primary retrieval path.
