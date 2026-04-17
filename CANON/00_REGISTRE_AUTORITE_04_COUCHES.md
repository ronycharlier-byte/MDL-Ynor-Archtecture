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
- Enforcer la separation entre surfaces doctrinales et non doctrinales.
- Casser le flou entre canon, support, archives et technique.

Question:
- Decris la structure CANON, RAG_SUPPORT, ARCHIVES, TECHNIQUE.
- Quel est le role des gates de validation ?
- Quel est le statut des prompts, logs et wrappers ?

Answer:
- `CANON` is authority.
- `RAG_SUPPORT` is controlled support.
- `ARCHIVES` are historical and relayed outside the main path.
- `TECHNIQUE` is separate and never first-rank doctrine.
- Gates block production when a rule fails.

Query anchors:
- Decris la structure CANON, RAG_SUPPORT, ARCHIVES, TECHNIQUE.
- Quel est le role des gates de validation ?
- Pourquoi les miroirs doivent-ils etre exclus du retrieval principal ?
- Quel est le comportement attendu des doublons non canoniques ?

Layer order:
1. `CANON`
2. `RAG_SUPPORT`
3. `ARCHIVES`
4. `TECHNIQUE`

Primary retriever:
- sees only `CANON` and `RAG_SUPPORT`
- does not treat prompts, logs, wrappers, releases or mirrors as doctrine
- routes doctrinal questions to `CANON`
- routes support questions to `RAG_SUPPORT`
