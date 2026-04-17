> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** MODULE
> **Position Chiastique :** D
> **Role du Fichier :** Transmission et interface
> **Centre Doctrinal Local :** canal local de diffusion et de synchronisation
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** portee de diffusion et memoisation utile
> - **β :** perte de fidelite et dispersion
> - **κ :** cout de packaging et de synchronisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
Ce dossier contient l'infrastructure nécessaire pour exposer l'AGI Ynor au monde extérieur.

## 📁 CONTENU
- **`ynor_api_server.py`** : Serveur FastAPI principal gérant les audits mu et les requêtes stratégiques.
- **`ynor_sdk/`** : Client Python pour intégrer Ynor dans d'autres applications.
- **`Dockerfile`** : Configuration pour l'isolation et le déploiement Cloud.

## LANCEMENT
```bash
uvicorn ynor_api_server:app --host 0.0.0.0 --port 8000
```

## 🔒 SÉCURITÉ
Le serveur utilise `python-dotenv`. Assurez-vous d'avoir configuré votre fichier `.env` à la racine du projet.
