---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-REGISTRY-CITATION-001
concept_id: MDLYNOR.CONCEPT.REGISTRY_CITATION
citation_id: MDLYNOR-CANON-REGISTRY-CITATION-001
document_role: answer_card
retrieval_weight: 1.02
---

# Shard de citation du registre

Purpose:
- Definir comment le retriever resout l autorite.
- Stabiliser la citation sans melanger plusieurs sources.

Question:
- Comment resoudre un citation_id sans ambiguite ?
- Explique le principe 1 concept = 1 source canonique.

Answer:
- `canonical_id` identifies the authoritative source.
- `citation_id` identifies the chunk or subsection to cite.
- One concept has one canonical source.
- If no canonical source supports the answer, mark it unsupported.

Query anchors:
- Explique le principe 1 concept = 1 source canonique.
- Comment resoudre un citation_id sans ambiguite ?
- Quelle citation dois-je utiliser pour mu ?
- Quel est le comportement attendu des doublons non canoniques ?

Rules:
- `canonical_id` identifies the authoritative source.
- `citation_id` identifies the chunk or subsection to cite.
- One concept has one canonical source.
- One answer has one or more citations, never a blurred source mass.
- Tout doublon non canonique devient archive ou derive.

The registry shard points to the citation manifest and the canonical identifier sheet.
