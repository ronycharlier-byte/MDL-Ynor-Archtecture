> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** D
> **Role du Fichier :** Manifeste d entree et hub de navigation
> **Centre Doctrinal Local :** point local d orientation et d acces
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** couverture de navigation et orientation
> - **β :** distraction et fragmentation
> - **κ :** cout d acces et de relecture
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
---



STATUS: CANONICAL | V11.13.0 | SOURCE: UNIFIED | 



AUDIT: CERTIFIED 2026-04-06



---



# 03 C MOTEURS ET DEPLOIEMENT







## Role



Branche operationnelle du corpus: moteurs actifs, API, dashboards, scripts de lancement et couche de distribution technique.







## Ce Que Cette Branche Contient



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_04_DEPLOYMENT_AND_API/ynor_api_server.py`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_04_DEPLOYMENT_AND_API/ynor_dashboard_ui.py`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/app.py`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/streamlit_dashboard.py`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/ynor_dashboard_v2.py`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/start_mdl_servers.ps1`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/start_mdl_servers_cf.ps1`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/start_mdl_ngrok.ps1`



- `01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_06_SCRIPTS_AND_DASHBOARDS/stop_mdl_servers.ps1`







## Fonction



Cette branche sert a transformer le corpus theoriquement complet en systeme utilisable:



- exposer une API



- fournir une interface de pilotage



- encadrer les émergence et les quotas



- instrumenter les logs et la telemetrie



- preparer les paquets de deploiement







## Entrypoints Principaux



- API locale: `uvicorn ynor_api_server:app --host 0.0.0.0 --port 8492`



- Dashboard de supervision: `http://localhost:8493`



- Dashboard API natif: `http://localhost:8492/dashboard`



- Status rapide: `http://localhost:8492/status`







## Documents De Reference



- [04_D_TRANSMISSION_C_MOTEURS_DEPLOIEMENT_API_CONTRACT.md](04_D_TRANSMISSION_C_MOTEURS_DEPLOIEMENT_API_CONTRACT.md)



- [04_D_ACTIVATION_C_MOTEURS_DEPLOIEMENT_DEPLOYMENT_PLAYBOOK.md](04_D_ACTIVATION_C_MOTEURS_DEPLOIEMENT_DEPLOYMENT_PLAYBOOK.md)



- [04_D_VERIFICATION_C_MOTEURS_DEPLOIEMENT_DASHBOARD_SPEC.md](04_D_VERIFICATION_C_MOTEURS_DEPLOIEMENT_DASHBOARD_SPEC.md)



- [04_D_VERIFICATION_C_MOTEURS_DEPLOIEMENT_OBSERVABILITY_LOGS.md](04_D_VERIFICATION_C_MOTEURS_DEPLOIEMENT_OBSERVABILITY_LOGS.md)



- [97_Z_ARCHIVES_C_MOTEURS_DEPLOIEMENT_RELEASE_PIPELINE.md](97_Z_ARCHIVES_C_MOTEURS_DEPLOIEMENT_RELEASE_PIPELINE.md)







## Principe De Lecture



Lire d abord la couche d exposition, puis la couche de controle, puis les scripts de lancement. La branche doit rester lisible comme un systeme, pas comme un tas de fichiers de service.





---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
