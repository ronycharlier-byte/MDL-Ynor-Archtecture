---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-007
concept_id: MDLYNOR.CONCEPT.CITATION_RESOLUTION
citation_id: MDLYNOR-CANON-007
document_role: citation-policy
retrieval_weight: 1.08
---

# Resolution de citation

Use the smallest stable citation unit available.

Rules:
- keep `canonical_id` as the authority anchor;
- keep `citation_id` as the resolvable chunk or subsection anchor;
- if no canonical source supports the answer, return `unsupported`;
- do not improvise a citation from a prompt, log, wrapper, release, or mirror.

Practical format:
- `canonical_id`
- `citation_id`
- `section_id`
- `chunk_id` if needed

Production rule:
- a claim without a canonical citation is not a production claim.
