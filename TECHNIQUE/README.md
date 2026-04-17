---
layer: TECHNIQUE
status: technical
canonical_id: MDLYNOR-TECH-ROOT-001
concept_id: MDLYNOR.TECHNOLOGY.LAYER
---

# TECHNIQUE

This layer holds code, scripts, notebooks, deployment, tests, dashboards, configs, binaries, and generated artefacts.

TECHNIQUE is separate from doctrine.
It may be indexed separately, but it must never compete with CANON.

Storage notes:
- `vector_memory.json` is the live runtime vector store.
- `vector_memory_governed.json` is the governed snapshot used by production retrieval.
- `vector_memory_governed_phase3.json` has been archived under `ARCHIVES/07_A_PRIME_ARCHIVES_ET_RELEASES/`.
- `data/90_Z_BASE_CONNAISSANCE_TECHNIQUE.json` is technical data and not doctrinal source material.
