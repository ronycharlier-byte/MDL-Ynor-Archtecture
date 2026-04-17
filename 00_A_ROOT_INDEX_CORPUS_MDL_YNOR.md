# MDL YNOR Root Index

- Corpus: MDL YNOR
- Role: root entry point and navigation hub
- Primary retrieval: `CANON` and `RAG_SUPPORT` only
- Non-primary layers: `ARCHIVES`, `TECHNIQUE`, `MONITORING`, `AUDIT`, `INBOX_QUARANTAINE`

## Root Files
- `00_A_ROOT_INDEX_CORPUS_MDL_YNOR.md`
- `corpus_layers.json`

## Root Layers
- `CANON`
- `RAG_SUPPORT`
- `ARCHIVES`
- `TECHNIQUE`
- `MONITORING`
- `AUDIT`
- `INBOX_QUARANTAINE`

## Layer Guides
- `CANON/README.md`
- `RAG_SUPPORT/README.md`
- `ARCHIVES/README.md`
- `TECHNIQUE/README.md`
- `MONITORING/README.md`
- `AUDIT/README.md`
- `INBOX_QUARANTAINE/README.md`

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
