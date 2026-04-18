---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-011
concept_id: MDLYNOR.CONCEPT.OPERATOR_D
citation_id: MDLYNOR-CANON-011
document_role: operator
retrieval_weight: 1.08
---

# Operator D

Definition:
- `D(S) = proj_{SafeDomain}(S)`

Role:
- remove unsafe or non-resolvable states from the working set;
- keep the system inside the safe domain;
- correct, not invent.

Validation requirement:
- the safe domain must be defined by independent admissibility criteria, not by the output of `D` itself.
- `D` is valid only if it preserves those criteria under test.

Operational rule:
- D is a corrective operator.
- D is not a generative operator.
- D should be used whenever a state threatens admissibility or production safety.
