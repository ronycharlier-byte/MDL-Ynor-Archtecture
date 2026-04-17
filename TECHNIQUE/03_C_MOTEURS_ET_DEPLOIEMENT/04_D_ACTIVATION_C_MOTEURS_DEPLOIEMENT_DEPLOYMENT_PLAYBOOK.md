> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** D
> **Role du Fichier :** Playbook de mise en service
> **Centre Doctrinal Local :** sequencement operationnel du deploiement
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** sequencement operationnel du deploiement
> - **β :** erreurs de sequence
> - **κ :** cout de sequence
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



# DEPLOYMENT PLAYBOOK







## Objectif



Deployer la branche `C` de facon reproductible, en gardant le controle sur l API, le dashboard et les logs.







## Prerequis



- Python et dependances du projet



04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_STRATEGY_PROFILE.json`



- cle `YNOR_API_KEY`



- cle optionnelle `YNOR_TEST_KEY`



- option de deploiement tunnelise si publication externe souhaitee







## Sequence Locale Recommandee



1. Verifier que le repertoire source est present.



2. Verifier les émergence locaux.



3. Lancer l API unifiee sur le port `8492`.



4. Ouvrir le dashboard Streamlit sur le port `8501`.



5. Valider `/api/corpus/status` et `/api/corpus/summary`.



6. Si besoin, ouvrir un tunnel `ngrok` ou `cloudflared`.







## Lancement Standard



### API



```bash



python -m uvicorn api_app:app --host 0.0.0.0 --port 8492



```







### Dashboard local



- `streamlit_dashboard.py` pour l exploration du corpus



- `app.py` pour l audit mu et la visualisation de viabilite



- `ynor_dashboard_v2.py` pour le monitor HTML/FastAPI







## Scripts De Travail



- `start_local_stack.ps1` lance l API et le dashboard Streamlit



- `stop_local_stack.ps1` arrete proprement les processus



- `start_mdl_servers.ps1` lance Uvicorn puis ngrok



- `start_mdl_servers_cf.ps1` lance Uvicorn puis Cloudflare Tunnel



- `start_mdl_ngrok.ps1` lance Uvicorn puis ngrok en mode secours



- `stop_mdl_servers.ps1` arrete proprement les processus







## Ports Observes



- API: `8492`



- Dashboard monitor: `8493`



- Tunnel externe: dependant du provider







## Strategie De Securite



- Ne jamais committer de émergence en clair.



- Garder le mode ecriture bloque sauf besoin explicite.



- Verifier les cles de revocation avant toute exposition externe.



- Preferer les usages locaux ou tunnelises avec acces limite.







## Checklist Avant Publication



- `/api/corpus/status` repond correctement.



- `/api/corpus/summary` charge sans erreur.



- Le dashboard Streamlit affiche les donnees du corpus.



- Les logs sont bien rediriges.



- Le fichier de PID est ecrit si un script de lancement le prevoit.



- Le tunnel public pointe bien vers le bon port.







## Incident Minimum



Si l API ne demarre pas:



- lire `uvicorn_errors_*.log`



- verifier la presence des variables d environnement



- confirmer que le port `8492` est libre



- relancer sans tunnel pour isoler le probleme





---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
