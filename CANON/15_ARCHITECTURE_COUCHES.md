---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-015
concept_id: MDLYNOR.CONCEPT.LAYER_ARCHITECTURE
citation_id: MDLYNOR-CANON-015
document_role: answer_card
retrieval_weight: 1.08
---

# Layer architecture

Query anchors:
- Decris la structure CANON, RAG_SUPPORT, ARCHIVES, TECHNIQUE.
- Quelle difference entre canon et archive ?
- Quel est le role des gates de validation ?
- Pourquoi les miroirs doivent-ils etre exclus du retrieval principal ?
- Quelle couche repond a une question doctrinale ?
- Quel est le comportement attendu des doublons non canoniques ?
- Quel est le role de RAG_SUPPORT ?
- Quel est le statut des prompts, logs et wrappers ?

Question:
- What is the four-layer architecture and how does it govern retrieval?

Answer:
- `CANON` is the authority layer.
- `RAG_SUPPORT` is controlled support, not first-rank doctrine.
- `ARCHIVES` preserve historical material outside the main path.
- `TECHNIQUE` holds code, scripts, configs and deployment artefacts.
- The primary retriever sees only `CANON` and `RAG_SUPPORT`.
- Prompts, logs, wrappers, releases and mirrors are not first-rank doctrine.

The corpus has four coercive layers:
1. `CANON`
2. `RAG_SUPPORT`
3. `ARCHIVES`
4. `TECHNIQUE`

Retrieval rule:
- the primary retriever sees only `CANON` and `RAG_SUPPORT`
- `ARCHIVES` are relayed outside the main path
- `TECHNIQUE` is indexed separately
- prompts, logs, wrappers, releases and mirrors are not first-rank doctrine
