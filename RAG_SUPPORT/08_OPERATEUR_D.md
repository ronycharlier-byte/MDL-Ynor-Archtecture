---
layer: RAG_SUPPORT
status: support
canonical_id: MDLYNOR-RAGSUP-008
concept_id: MDLYNOR.SUPPORT.OPERATOR_D
citation_id: MDLYNOR-RAGSUP-008
source_of_truth: CANON
document_role: support
retrieval_weight: 0.93
---

# Operator D card

Query anchors:
- Quel est l operateur D et son role ?

Corrective operator:
- `D(S) = proj_{SafeDomain}(S)`

Question:
- What is operator D and what does it do?

Answer:
- `D(S) = proj_{SafeDomain}(S)`
- It removes unsafe or non-resolvable state.
- It keeps the system inside the safe domain.
- It never uses archives as doctrine.

Canonical citations:
- `MDLYNOR-CANON-011`
- `MDLYNOR-CANON-015`

Role:
- remove unsafe or non-resolvable state
- keep the system inside the safe domain
- never use archives as doctrine
