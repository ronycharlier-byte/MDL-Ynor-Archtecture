---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-015
concept_id: MDLYNOR.CONCEPT.LAYER_ARCHITECTURE
citation_id: MDLYNOR-CANON-015
document_role: layer-architecture
retrieval_weight: 1.08
---

# Layer architecture

The corpus has seven layers:
1. `CANON`
2. `RAG_SUPPORT`
3. `ARCHIVES`
4. `TECHNIQUE`
5. `MONITORING`
6. `AUDIT`
7. `INBOX_QUARANTAINE`

Retrieval rule:
- the primary retriever sees only `CANON` and `RAG_SUPPORT`.

Operational rule:
- `TECHNIQUE` holds code, scripts, configs and artefacts.
- `MONITORING` watches drift and runtime state.
- `AUDIT` records validation and benchmarks.
- `INBOX_QUARANTAINE` isolates ambiguity.

Admissibility rule:
- prompts, logs, wrappers, releases and mirrors are not first-rank doctrine.
