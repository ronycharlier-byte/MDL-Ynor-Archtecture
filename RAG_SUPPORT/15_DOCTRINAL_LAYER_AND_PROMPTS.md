---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-015
concept_id: MDLYNOR.SUPPORT.DOCTRINAL_LAYER_PROMPTS
citation_id: MDLYNOR-RAGSUP-015
source_of_truth: CANON
document_role: answer_card
retrieval_weight: 0.92
---

# Doctrinal layer and prompts

Query anchors:
- Quelle couche repond a une question doctrinale ?
- Quel est le statut des prompts, logs et wrappers ?
- Les prompts, logs et wrappers ont-ils une autorite doctrinale ?
- Quelle couche ne doit pas servir de source de verite de premier rang ?

Question:
- Which layer answers a doctrinal question?

Answer:
- The canonical layer answers doctrine.
- RAG_SUPPORT may help with retrieval and resolution.
- Prompts, logs, wrappers and audits are not first-rank doctrine.
- Technical artifacts stay outside the primary retrieval path.

Canonical citations:
- `MDLYNOR-CANON-015`
- `MDLYNOR-CANON-REGISTRY-DOCTRINE-001`
- `MDLYNOR-CANON-REGISTRY-LAYERS-001`

Resolution rule:
- If the query is doctrinal, route to CANON first.
