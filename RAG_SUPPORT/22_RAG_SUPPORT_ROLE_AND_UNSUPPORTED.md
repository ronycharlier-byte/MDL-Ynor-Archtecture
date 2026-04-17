---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-022
concept_id: MDLYNOR.SUPPORT.RAG_SUPPORT_ROLE_AND_UNSUPPORTED
citation_id: MDLYNOR-RAGSUP-022
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 1.08
---

# RAG_SUPPORT role and unsupported answers

Query anchors:
- Quel est le role de RAG_SUPPORT ?
- Que faire si aucune source canonique ne soutient la reponse ?

Question:
- What is the role of RAG_SUPPORT?

Answer:
- RAG_SUPPORT helps retrieval and resolution.
- It offers chunkable summaries, reading guides, access maps and controlled examples.
- It never replaces CANON.
- If no canonical source supports the answer, return unsupported.

Canonical citations:
- `MDLYNOR-CANON-001`
- `MDLYNOR-CANON-007`
- `MDLYNOR-CANON-015`

Resolution rule:
- Support the answer, do not invent it.
