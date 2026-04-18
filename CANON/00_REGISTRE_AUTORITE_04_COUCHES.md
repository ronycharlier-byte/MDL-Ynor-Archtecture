---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-REGISTRY-LAYERS-001
concept_id: MDLYNOR.CONCEPT.REGISTRY_LAYERS
citation_id: MDLYNOR-CANON-REGISTRY-LAYERS-001
document_role: answer_card
retrieval_weight: 1.02
---

# Shard de couches du registre

Purpose:
- Enforce separation between doctrinal and non-doctrinal surfaces.
- Break the blur between canon, support, archives, technique, monitoring, audit and quarantine.

Question:
- Decris la structure du corpus.
- Quel est le role des gates de validation ?
- Quel est le statut des prompts, logs et wrappers ?

Answer:
- `CANON` is authority.
- `RAG_SUPPORT` is controlled support.
- `ARCHIVES` are historical and relayed outside the main path.
- `TECHNIQUE` is separate and never first-rank doctrine.
- `MONITORING` watches runtime state.
- `AUDIT` records validation evidence.
- `INBOX_QUARANTAINE` isolates ambiguity.
- Gates block production when a rule fails.

Layer order:
1. `CANON`
2. `RAG_SUPPORT`
3. `ARCHIVES`
4. `TECHNIQUE`
5. `MONITORING`
6. `AUDIT`
7. `INBOX_QUARANTAINE`

Primary retriever:
- sees only `CANON` and `RAG_SUPPORT`
- does not treat prompts, logs, wrappers, releases or mirrors as doctrine
- routes doctrinal questions to `CANON`
- routes support questions to `RAG_SUPPORT`
- leaves validation material to `AUDIT`
- leaves ambiguity to `INBOX_QUARANTAINE`
