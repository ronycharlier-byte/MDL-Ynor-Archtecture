# Cloud Upload

Ce dossier peut maintenant etre prepare pour un envoi cloud en deux versions :

- `MDL_Ynor_Architecture_cloud_full.zip` : archive complete du corpus.
- `MDL_Ynor_Architecture_cloud_safe.zip` : archive sans secrets locaux ni caches techniques.

Script de generation :

- `C:\\Users\\ronyc\\Desktop\\MDL Ynor Architecture\\build_cloud_package.ps1`

Sortie :

- `C:\\Users\\ronyc\\Desktop\\MDL Ynor Architecture\\_CLOUD_EXPORTS`

Commande PowerShell :

```powershell
powershell -ExecutionPolicy Bypass -File "C:\Users\ronyc\Desktop\MDL Ynor Architecture\build_cloud_package.ps1"
```

Contenu retire de la version `safe` :

- `.git`
- `.venv`
- `.uv-cache`
- `.pytest_cache`
- `__pycache__`
- `logs`
- `.env`
- `secrets.local.json`
- `*.pyc`

Si vous devez deposer le corpus sur un cloud public ou partage, utilisez la version `safe`.
Si vous devez cloner l'etat complet de travail dans un espace prive, utilisez la version `full`.
