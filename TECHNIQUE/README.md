---
layer: TECHNIQUE
status: technical
canonical_id: MDLYNOR-TECH-ROOT-001
concept_id: MDLYNOR.TECHNOLOGY.LAYER
citation_id: MDLYNOR-TECH-ROOT-001
document_role: technical-root
retrieval_weight: 0.10
source_of_truth: MDLYNOR-CANON-015
---

# TECHNIQUE

This layer holds code, scripts, notebooks, deployment, tests, dashboards, configs, binaries, and generated artefacts.

TECHNIQUE is separate from doctrine.
It may be indexed separately, but it must never compete with CANON.
It is the correct home for operational packs, gate specs, and runtime tooling.

Storage notes:
- `00_PACK_INJECTION_CANONIQUE.md` is an operational pack, not doctrine.
- `00_POLICY.md` defines technical policy.
- `01_GATE_SPEC.md` defines hard technical gates.
- `vector_memory.json` is the live runtime vector store.
- `vector_memory_governed.json` is the governed snapshot used by production retrieval.
- `vector_memory_governed_phase3.json` has been archived under `ARCHIVES/07_A_PRIME_ARCHIVES_ET_RELEASES/`.
- `data/90_Z_BASE_CONNAISSANCE_TECHNIQUE.json` is technical data and not doctrinal source material.
