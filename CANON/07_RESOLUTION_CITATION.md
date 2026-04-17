---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-007
concept_id: MDLYNOR.CONCEPT.CITATION_RESOLUTION
citation_id: MDLYNOR-CANON-007
document_role: answer_card
retrieval_weight: 1.08
---

# Resolution de citation

This sheet defines the stable citation target.

Query anchors:
- Comment resoudre un citation_id sans ambiguite ?
- Quelle citation dois-je utiliser pour mu ?
- Que faire si aucune source canonique ne soutient la reponse ?

Question:
- How do I resolve a citation without ambiguity?

Answer:
- Use the smallest stable citation unit available.
- Keep `canonical_id` as the authority anchor.
- Keep `citation_id` as the resolvable chunk or subsection anchor.
- If no canonical source supports the answer, return unsupported.

Rules:
- `canonical_id` names the authoritative source.
- `citation_id` names the resolvable citation unit.
- The retriever should cite the smallest stable unit available.
- If a document has no `citation_id`, it is not ready for production retrieval.

Practical format:
- `citation_id :: section_id :: Cxx`
- `canonical_id` remains the authority anchor.
- `section_id` keeps subsection citations stable.
- If no canonical source supports the response, mark it unsupported instead of improvising.
