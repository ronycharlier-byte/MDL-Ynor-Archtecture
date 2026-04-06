﻿---
STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 
AUDIT: CERTIFIED 2026-04-06
---
# 📡 PÔLE DÉPLOIEMENT & API
**MDL YNOR FRAMEWORK**

Ce dossier contient l'infrastructure ncessaire pour exposer l'AGI Ynor au monde extrieur.

## 📁 CONTENU
- **`ynor_api_server.py`** : Serveur FastAPI principal grant les audits mu et les requêtes stratgiques.
- **`ynor_sdk/`** : Client Python pour intgrer Ynor dans d'autres applications.
- **`Dockerfile`** : Configuration pour l'isolation et le dploiement Cloud.

## 🚀 LANCEMENT
```bash
uvicorn ynor_api_server:app --host 0.0.0.0 --port 8000
```

## 🔒 SÉCURITÉ
Le serveur utilise `python-dotenv`. Assurez-vous d'avoir configurvotre fichier `.env` la racine du projet.
