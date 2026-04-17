---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-012
concept_id: MDLYNOR.SUPPORT.LAYER_ARCHITECTURE
citation_id: MDLYNOR-RAGSUP-012
source_of_truth: CANON
document_role: support
retrieval_weight: 0.45
---

# Fiche d architecture des couches

Query anchors:
- Decris la structure CANON, RAG_SUPPORT, ARCHIVES, TECHNIQUE.
- Quelle difference entre canon et archive ?
- Quel est le role des gates de validation ?
- Pourquoi les miroirs doivent-ils etre exclus du retrieval principal ?
- Quel est le comportement attendu des doublons non canoniques ?

Layers:
1. `CANON`
2. `RAG_SUPPORT`
3. `ARCHIVES`
4. `TECHNIQUE`

Primary retrieval sees only `CANON` and `RAG_SUPPORT`.

Question:
- Which layers belong in the primary retriever and which ones stay out?

Answer:
- Primary retrieval sees only `CANON` and `RAG_SUPPORT`.
- `ARCHIVES` stay out of the primary path.
- `TECHNIQUE` is indexed separately.
- Prompts, logs, wrappers, releases and mirrors are not first-rank doctrine.

Canonical citations:
- `MDLYNOR-CANON-015`
- `MDLYNOR-CANON-REGISTRY-LAYERS-001`
