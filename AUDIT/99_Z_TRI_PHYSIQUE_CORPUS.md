# Tri physique corpus MDL YNOR

- Files moved: 66
- Folders reorganized: 24
- Total moved items: 90
- Root files kept: 2
- Root layer dirs kept: 7
- Hidden infra dirs kept: 3

## Root layers
- `CANON`
- `RAG_SUPPORT`
- `ARCHIVES`
- `TECHNIQUE`
- `MONITORING`
- `AUDIT`
- `INBOX_QUARANTAINE`

## Root files kept
- `00_A_ROOT_INDEX_CORPUS_MDL_YNOR.md`
- `corpus_layers.json`

## Hidden infra dirs kept
- `.git`
- `.github`
- `.obsidian`

## Quarantine
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\supreme_temp` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\INBOX_QUARANTAINE\supreme_temp`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\AUDIT\90_Z_CARNET_AUTO_RECHERCHE.txt` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\INBOX_QUARANTAINE\90_Z_CARNET_AUTO_RECHERCHE.txt`
- No additional quarantine files were created in this phase.

## Sample moves
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\monitoring` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\MONITORING`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\dashboard` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\MONITORING\dashboard`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\ingest.py` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\ingest.py`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\rag_engine.py` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\rag_engine.py`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\vector_memory.py` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\vector_memory.py`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\supreme_temp` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\INBOX_QUARANTAINE\supreme_temp`
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\AUDIT\90_Z_CARNET_AUTO_RECHERCHE.txt` -> `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\INBOX_QUARANTAINE\90_Z_CARNET_AUTO_RECHERCHE.txt`

## Verification
- `python -m py_compile` passed on the moved and patched modules.
- `MONITORING/dashboard/server.py` remains in the monitoring layer and is imported by `TECHNIQUE/main.py` through the repo root.
- Validation launchers now point to `AUDIT/05_C_PRIME_VALIDATION_ET_TESTS`.
- The root contains only the index, the corpus map, and the seven governed roots.

## Exceptions
- `C:\Users\ronyc\Desktop\Corpus\MDL Ynor\README.md` was not found at the source path when the archive move ran, so no relocation was performed.
