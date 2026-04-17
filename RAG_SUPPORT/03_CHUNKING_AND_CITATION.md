---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-003
concept_id: MDLYNOR.SUPPORT.CHUNKING_CITATION
source_of_truth: CANON
citation_id: MDLYNOR-RAGSUP-003
document_role: policy
retrieval_weight: 0.8
---

# Chunking and citation

Query anchors:
- Quel est le principe 1 concept = 1 source canonique ?
- Comment eviter le monopole d un document pivot ?

Chunking rule:
- Prefer headings and paragraph boundaries.
- Keep chunks short and semantically atomic.
- Do not mix archive text with canonical text in the same chunk set.
- Do not let one pivot produce a monopoly of chunks.
- Split pivot documents before they dominate top-k.

Citation rule:
- Always cite `canonical_id` and `citation_id`.
- Include the chunk suffix when possible.
- If a source is not canonical, label it as archive or technical.

Production gate:
- No citation, no answer.
