---
layer: RAG_SUPPORT
status: navigation
canonical_id: MDLYNOR-RAGSUP-ROOT-001
concept_id: MDLYNOR.SUPPORT.RAG_LAYER
source_of_truth: CANON
citation_id: MDLYNOR-RAGSUP-ROOT-001
document_role: navigation
retrieval_weight: 0.12
---

# RAG_SUPPORT

Role:
- RAG_SUPPORT helps retrieval but never replaces CANON.
- It provides controlled support, not first-rank doctrine.
- It exists to reduce ambiguity and keep answers chunkable.

Query anchors:
- Quel est le role de RAG_SUPPORT ?

Allowed content:
- chunkable summaries
- reading guides
- access maps
- controlled examples
- crosswalks to canonical sources

The primary retriever may use:
- CANON
- RAG_SUPPORT

The primary retriever may not use:
- ARCHIVES
- TECHNIQUE
- prompts, logs, wrappers, releases, mirrors as doctrine
