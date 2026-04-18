---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-017
concept_id: MDLYNOR.CONCEPT.SCIENTIFIC_VALIDATION
citation_id: MDLYNOR-CANON-017
document_role: validation-framework
retrieval_weight: 1.08
---

# Scientific Validation

Scientific status is layered:
- description: what the corpus does;
- explanation: why a relation is proposed;
- prediction: what should happen next under the model;
- norm: what the corpus prescribes for itself;
- speculation: any claim beyond the supported domain.

Evidence ladder:
- mock: a test double or placeholder, not evidence;
- simulation: model-generated behavior, useful but not direct proof;
- benchmark internal: controlled test on the same corpus family;
- validation internal: consistency and invariants inside the corpus;
- benchmark external: evaluation on independent material;
- validation external: performance on unseen material with pre-registered criteria;
- replication independent: repeated evaluation by a separate run, separate sampler, or separate annotator;
- proof scientific strong: convergent evidence from independent validation, replication, uncertainty bounds, and explicit failure criteria.

Rules:
- demonstration is not proof;
- internal validation is not external validation;
- benchmark performance is not scientific proof;
- a cited result is still only a result if the protocol is weak;
- a theory without external validation remains a hypothesis class.

Circularity guard:
- if the same corpus both defines the metric and certifies the metric, the result is auto-confirming;
- if calibration data are reused for final claims, the claim is not independent;
- if the evaluation set influences threshold selection after the fact, the claim is post-hoc.
