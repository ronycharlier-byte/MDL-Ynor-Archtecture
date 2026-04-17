---
layer: CANON
status: canonical
canonical_id: MDLYNOR-CANON-REGISTRY-001
concept_id: MDLYNOR.CONCEPT.REGISTRY_HUB
citation_id: MDLYNOR-CANON-REGISTRY-001
document_role: registry
retrieval_weight: 0.30
---

# Registre d autorite

Role:
- Le registre d autorite route les questions vers la bonne feuille canonique.
- Il ne doit jamais servir de preuve doctrinale de premier rang.
- Il existe pour decompacter le pivot et forcer la lecture des unites fines.

Query anchors:
- Quel est le role du registre d autorite ?
- Quelle couche repond a une question doctrinale ?
- Quel est le comportement attendu des doublons non canoniques ?

Rules:
- One concept = one canonical source.
- One citation_id = one resolvable target.
- Competing authority views are archives or derivatives.
- Do not answer doctrine from the registry hub when a dedicated sheet exists.

Shards:
- `00_REGISTRE_AUTORITE_01_PORTAIL.md`
- `00_REGISTRE_AUTORITE_02_DOCTRINE.md`
- `00_REGISTRE_AUTORITE_03_CITATION.md`
- `00_REGISTRE_AUTORITE_04_COUCHES.md`

Canonical anchors:
- Portal -> `MDLYNOR-CANON-001`
- Constitution -> `MDLYNOR-CANON-003`
- Theory -> `MDLYNOR-CANON-004`
- Memory -> `MDLYNOR-CANON-005`
- Citation policy -> `MDLYNOR-CANON-007`
- Mu and survival -> `MDLYNOR-CANON-008`
- Alpha / beta / kappa -> `MDLYNOR-CANON-009`
- Risk law -> `MDLYNOR-CANON-010`
- Operator D -> `MDLYNOR-CANON-011`
- Goodhart -> `MDLYNOR-CANON-012`
- Regimes -> `MDLYNOR-CANON-013`
- Canonical ids -> `MDLYNOR-CANON-014`
- Layers -> `MDLYNOR-CANON-015`
- Theory / constitution / governance -> `MDLYNOR-CANON-016`
