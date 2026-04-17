# Phase 4 health report

- Alert level: `GREEN`
- Rollback required: `False`
- Production ready: `True`
- Benchmark path: `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\AUDIT\validation_long_duration_cycles\rag_validation_long_duration_cycle_4.json`
- Quarantine count: `0`

## Metric views
### canonical

| Metric | Value |
|---|---:|
| top5_pertinent_rate | 70.0 |
| citation_canonical_rate | 100.0 |
| citation_stable_rate | 100.0 |
| archive_leak_rate | 0.0 |
| tech_leak_rate | 0.0 |
| no_valid_source_rate | 0.0 |
| monopoly_violation_rate | 0.0 |
| support_rate | 70.0 |
| average_concentration | 0.2 |
| average_score | 8.95 |

### production

| Metric | Value |
|---|---:|
| top5_pertinent_rate | 72.0 |
| citation_canonical_rate | 100.0 |
| citation_stable_rate | 100.0 |
| archive_leak_rate | 0.0 |
| tech_leak_rate | 0.0 |
| no_valid_source_rate | 0.0 |
| monopoly_violation_rate | 0.0 |
| support_rate | 70.0 |
| average_concentration | 0.2 |
| average_score | 9.02 |

### combined

| Metric | Value |
|---|---:|
| top5_pertinent_rate | 71.0 |
| citation_canonical_rate | 100.0 |
| citation_stable_rate | 100.0 |
| archive_leak_rate | 0.0 |
| tech_leak_rate | 0.0 |
| no_valid_source_rate | 0.0 |
| monopoly_violation_rate | 0.0 |
| support_rate | 70.0 |
| average_concentration | 0.2 |
| average_score | 8.98 |

## Drift

```json
{
  "current": {
    "queries": 40,
    "top5_pertinent_rate": 71.0,
    "canonical_rate": 30.0,
    "support_rate": 70.0,
    "archive_leak_rate": 0.0,
    "tech_leak_rate": 0.0,
    "other_rate": 0.0,
    "duplicate_rate": 0.0,
    "citation_canonical_rate": 100.0,
    "citation_stable_rate": 100.0,
    "no_valid_source_rate": 0.0,
    "monopoly_violation_rate": 0.0,
    "average_concentration": 0.2,
    "average_score": 8.98
  },
  "previous": {
    "queries": 40,
    "top5_pertinent_rate": 71.0,
    "canonical_rate": 30.0,
    "support_rate": 70.0,
    "archive_leak_rate": 0.0,
    "tech_leak_rate": 0.0,
    "other_rate": 0.0,
    "duplicate_rate": 0.0,
    "citation_canonical_rate": 100.0,
    "citation_stable_rate": 100.0,
    "no_valid_source_rate": 0.0,
    "monopoly_violation_rate": 0.0,
    "average_concentration": 0.2,
    "average_score": 8.98
  },
  "reasons": [],
  "legacy_quarantine_status": "GREEN",
  "delta": {
    "top5_pertinent_rate": 0.0,
    "citation_stable_rate": 0.0,
    "citation_canonical_rate": 0.0,
    "support_rate": 0.0
  }
}
```

## Quarantine examples

- None

## Pivot watchlist

- layer:RAG_SUPPORT (0.7)
- layer:CANON (0.3)

## Decision

- maintenance remains green