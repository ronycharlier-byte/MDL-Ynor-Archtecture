---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-020
concept_id: MDLYNOR.CONCEPT.PREDICTIVE_PILOTING
citation_id: MDLYNOR-CANON-020
document_role: predictive-piloting
retrieval_weight: 1.08
---

# Predictive Piloting

Early warning:
- weak signals are detected by tracking `dot mu(t) < 0` on a pre-registered window.

Loop:
- `S(t) -> O(t) -> I(t) -> A(t) -> S(t + Delta t)`

Meaning:
- `O` = observe;
- `I` = interpret;
- `A` = act;
- `S` = state update.

Rule:
- trigger `D` before saturation occurs.
- pilot the margin `mu`, not the signal surface.

Validation note:
- separate calibration from validation and do not reuse the same window for both.
- keep a final untouched test set for the final claim.
- if the trigger threshold is tuned after observing outcomes, the trigger is not a validated rule.

Failure criteria:
- `mu` improves only in-sample but not out-of-sample;
- `dot mu` predicts nothing beyond random drift;
- the operator `D` reduces risk in one setting while increasing leakage or brittleness elsewhere.
