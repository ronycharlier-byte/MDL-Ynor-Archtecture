# Validation longue duree MDL YNOR

## Protocole
- Cycles: 4
- Runs consecutifs: oui
- Extension du corpus: interdite pendant la validation
- Gates: inchanges

## Synthese par cycle

| Cycle | Alert | Top-5 | Top-1 utile | Citation canonique | Citation stable | Archive | Technique | No valid source | Duplicates | RAG_SUPPORT | Pivot max | Quarantaine | Drift global | Score |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | GREEN | 71.0% | 100.0% | 100.0% | 100.0% | 0.0% | 0.0% | 0.0% | 0.0% | 70.0% | 0.7 | 0 | 1.5 | 8.98 |
| 2 | GREEN | 71.0% | 100.0% | 100.0% | 100.0% | 0.0% | 0.0% | 0.0% | 0.0% | 70.0% | 0.7 | 0 | 0.0 | 8.98 |
| 3 | GREEN | 71.0% | 100.0% | 100.0% | 100.0% | 0.0% | 0.0% | 0.0% | 0.0% | 70.0% | 0.7 | 0 | 0.0 | 8.98 |
| 4 | GREEN | 71.0% | 100.0% | 100.0% | 100.0% | 0.0% | 0.0% | 0.0% | 0.0% | 70.0% | 0.7 | 0 | 0.0 | 8.98 |

## Agregats

| Metrique | Min | Mean | Max |
|---|---:|---:|---:|
| Top-5 pertinent | 71.0 | 71.0 | 71.0 |
| Top-1 utile | 100.0 | 100.0 | 100.0 |
| Citation canonique correcte | 100.0 | 100.0 | 100.0 |
| Citation stable | 100.0 | 100.0 | 100.0 |
| Fuite archive | 0.0 | 0.0 | 0.0 |
| Fuite technique | 0.0 | 0.0 | 0.0 |
| Reponses sans source valable | 0.0 | 0.0 | 0.0 |
| Doublons top-k | 0.0 | 0.0 | 0.0 |
| Part RAG_SUPPORT | 70.0 | 70.0 | 70.0 |
| Part pivots dominants | 0.7 | 0.7 | 0.7 |
| Nouveaux fichiers en quarantaine | 0 | 0.0 | 0 |
| Drift global | 0.0 | 0.38 | 1.5 |
| Score moyen | 8.98 | 8.98 | 8.98 |

## Conditions de succes
- top5_pertinent_min: `True`
- top1_useful_min: `True`
- citation_canonical_min: `True`
- citation_stable_min: `True`
- archive_leak_zero: `True`
- tech_leak_zero: `True`
- no_valid_source_zero: `True`
- duplicate_topk_zero: `True`
- pivot_dominance_controlled: `False`
- quarantine_zero: `True`
- no_drift: `False`

## Verdict
- Success: `True`
- Rollback required: `False`