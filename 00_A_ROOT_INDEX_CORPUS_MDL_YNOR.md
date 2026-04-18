# MDL YNOR Root Index

- Corpus: MDL YNOR
- Role: root entry point, governance hub and routing map
- Primary retrieval: `CANON` and `RAG_SUPPORT` only
- Secondary reading: `ARCHIVES`, `TECHNIQUE`
- Operational layers: `MONITORING`, `AUDIT`
- Quarantine layer: `INBOX_QUARANTAINE`

## Root Files

- `00_A_ROOT_INDEX_CORPUS_MDL_YNOR.md`
- `README.md`
- `corpus_layers.json`
- `AUDIT/98_Z_CORPUS_RESTRUCTURATION_CANONIQUE.md`

## External Validation Campaign

- Snapshot: `MDLYNOR_EXTVAL_SNAPSHOT_2026-04-18`
- Protocol: `AUDIT/99_Z_VALIDATION_PROTOCOL_EXTENDED.md`
- Split manifest: `AUDIT/split_manifest.json`
- Seed log: `AUDIT/seed_log.json`
- The protocol defines the campaign, the split manifest freezes group membership, and the seed log fixes deterministic execution and replay order.
- Execution contracts: `AUDIT/99_Z_SPLIT_INSTANTIATION_POLICY.json`, `AUDIT/99_Z_BLIND_ANNOTATION_PACKET_SCHEMA.json`, `AUDIT/99_Z_RUN_OUTPUT_SCHEMA.json`, `AUDIT/99_Z_FINAL_VALIDATION_REPORT_TEMPLATE.md`

## Layer Order

1. `CANON`
2. `RAG_SUPPORT`
3. `ARCHIVES`
4. `TECHNIQUE`
5. `MONITORING`
6. `AUDIT`
7. `INBOX_QUARANTAINE`

## Reading Order

1. Portal and registry
2. Constitution and theory
3. Glossary and identifiers
4. Variable definitions and regime sheets
5. Validation and empirical measurement
6. Support crosswalks
7. Archives only when historical context is needed

## Retrieval Order

1. Dedicated canonical sheet
2. Canonical registry shard
3. Support crosswalk
4. Archive only when explicitly requested
5. Technical artefact only for implementation or debugging

## Operational Order

1. `TECHNIQUE` for code, scripts, configs and generated artefacts
2. `MONITORING` for health, drift and runtime state
3. `AUDIT` for benchmarks, validation runs and reproducibility
4. `INBOX_QUARANTAINE` for ambiguous or unclassified items

## Validation Order

1. Canonical citation check
2. Layer admissibility check
3. Archive leakage check
4. UTF-8 and encoding check
5. Duplicate concept and duplicate canonical source check
6. Empirical calibration or replication, when applicable

## Validation Launchers

- `python AUDIT/05_C_PRIME_VALIDATION_ET_TESTS/YNOR_Q_ISOMORPHISM_CHALLENGE.py`
- `python AUDIT/05_C_PRIME_VALIDATION_ET_TESTS/ynor_hallucination_challenge.py`

## Notes

- Canonical doctrine stays in `CANON`.
- Chunkable retrieval support stays in `RAG_SUPPORT`.
- Historical material stays in `ARCHIVES`.
- Code, scripts, configs, dashboards and runtime artifacts stay in `TECHNIQUE`.
- Monitoring, audit and quarantine stay out of the primary retriever.
- Ambiguous material goes to `INBOX_QUARANTAINE`.
