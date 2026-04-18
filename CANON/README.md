---
layer: CANON
status: navigation
canonical_id: MDLYNOR-CANON-ROOT-001
concept_id: MDLYNOR.CONCEPT.CANON_LAYER
citation_id: MDLYNOR-CANON-ROOT-001
document_role: navigation
retrieval_weight: 0.26
source_of_truth: MDLYNOR-CANON-015
---

# CANON

This is the authoritative layer for first-rank doctrine.
It defines the canonical source of truth and the admissible reading order.

Rules:
- One concept = one canonical source.
- Only `CANON` and `RAG_SUPPORT` may enter the primary retriever.
- Every canonical document must expose a stable `canonical_id`.
- Every canonical document used in production must expose a stable `citation_id`.
- Prompts, logs, wrappers, releases, mirrors, and audits are not first-rank doctrine.
- If a document is only operational, it belongs in `TECHNIQUE`.

Canonical retrieval order:
1. Registry shards
2. Portal
3. Constitution
4. Theory
5. Memory nucleus
6. Citation resolution
7. Alpha / beta / kappa and `mu`
8. Risk law and operator D
9. Goodhart and stability regimes
10. Identifiers, layers, and governance relation
11. Scientific validation
12. Empirical measurement
13. Predictive piloting
14. Cognitive extensions

Primary files:
- `00_REGISTRE_AUTORITE.md`
- `00_REGISTRE_AUTORITE_01_PORTAIL.md`
- `00_REGISTRE_AUTORITE_02_DOCTRINE.md`
- `00_REGISTRE_AUTORITE_03_CITATION.md`
- `00_REGISTRE_AUTORITE_04_COUCHES.md`
- `01_PORTAIL_CANONIQUE_FINAL.md`
- `02_CONSTITUTION_STRUCTURANTE.md`
- `03_THEORIE_STRUCTURELLE.md`
- `04_NOYAU_MEMOIRE.md`
- `05_GLOSSAIRE.md`
- `06_INDEX_CANONIQUE.md`
- `07_RESOLUTION_CITATION.md`
- `08_MU_SURVIE.md`
- `09_ALPHA_BETA_KAPPA.md`
- `10_E_INFINI.md`
- `11_OPERATEUR_D.md`
- `12_GOODHART.md`
- `13_REGIMES_STABILITE.md`
- `14_IDENTIFIANTS_CANONIQUES.md`
- `15_ARCHITECTURE_COUCHES.md`
- `16_THEORIE_CONSTITUTION_GOUVERNANCE.md`
- `17_SCIENTIFIC_VALIDATION.md`
- `18_MATHEMATICAL_TOPOLOGY.md`
- `19_EMPIRICAL_MEASUREMENT.md`
- `20_PREDICTIVE_PILOTING.md`
- `21_COGNITIVE_EXTENSIONS.md`
