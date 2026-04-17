---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-004
concept_id: MDLYNOR.SUPPORT.CITATION_MANIFEST
citation_id: MDLYNOR-RAGSUP-004
source_of_truth: CANON
document_role: support
retrieval_weight: 0.82
---

# Manifeste de citation

Query anchors:
- Comment resoudre un citation_id sans ambiguite ?
- Quelle citation dois-je utiliser pour mu ?
- Que faire si aucune source canonique ne soutient la reponse ?

Use:
- resoudre une citation vers une source canonique unique
- garder la citation au niveau chunk quand c est possible
- preferer l unite stable la plus petite

Format:
- `canonical_id`
- `citation_id`
- `section_id`
- `chunk`

If a source cannot be resolved, do not promote it to doctrine.
If no canonical source supports the answer, return unsupported instead of improvising.
