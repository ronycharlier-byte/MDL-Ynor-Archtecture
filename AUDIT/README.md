---
layer: AUDIT
status: audit
canonical_id: MDLYNOR-AUDIT-ROOT-001
concept_id: MDLYNOR.AUDIT.LAYER
citation_id: MDLYNOR-AUDIT-ROOT-001
document_role: audit-root
retrieval_weight: 0.12
source_of_truth: MDLYNOR-CANON-015
---

# AUDIT

This layer holds global audits, rename journals, benchmark reports, validation reports, and phase reports.
It also hosts frozen execution artefacts for the external validation campaign.

AUDIT is not first-rank doctrine.
It records how the corpus was checked, benchmarked, and reorganized.

If a document is a report about the corpus, it belongs here or in MONITORING.
Audit documents are evidence, not doctrine.

## External Validation Campaign

- [AUDIT/99_Z_VALIDATION_PROTOCOL_EXTENDED.md](99_Z_VALIDATION_PROTOCOL_EXTENDED.md) fixes the frozen external validation protocol.
- [split_manifest.json](split_manifest.json) freezes the split membership, roles, inclusion rules, and placeholder item identifiers.
- [seed_log.json](seed_log.json) fixes the deterministic seeds, execution order, and replay constraints.
- Together, these three artefacts make the external campaign launchable, replayable, and auditable without reopening the doctrinal core.

## Execution Contracts

- [AUDIT/99_Z_SPLIT_INSTANTIATION_POLICY.json](99_Z_SPLIT_INSTANTIATION_POLICY.json) defines how real item ids are minted from the frozen snapshot.
- [AUDIT/99_Z_BLIND_ANNOTATION_PACKET_SCHEMA.json](99_Z_BLIND_ANNOTATION_PACKET_SCHEMA.json) defines the blind annotation packet envelope.
- [AUDIT/99_Z_RUN_OUTPUT_SCHEMA.json](99_Z_RUN_OUTPUT_SCHEMA.json) defines the run output contract.
- [AUDIT/99_Z_FINAL_VALIDATION_REPORT_TEMPLATE.md](99_Z_FINAL_VALIDATION_REPORT_TEMPLATE.md) defines the final report shell.
