> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** D
> **Role du Fichier :** Observabilite et journalisation
> **Centre Doctrinal Local :** tracabilite des signaux, journaux et derives
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** tracabilite des signaux, journaux et derives
> - **β :** trous de logs
> - **κ :** cout de capture
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



# OBSERVABILITY AND LOGS







## Objectif



Definir ce qui doit etre observe, journalise et relu pour que `C` reste diagnostiable.







## Sources De Telemetrie



04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_STRATEGY_PROFILE.json`



04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_STRATEGY_PROFILE.json`



04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_STRATEGY_PROFILE.json`



04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_STRATEGY_PROFILE.json`



04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_STRATEGY_PROFILE.json`



- logs `uvicorn_*.log`



- logs `uvicorn_errors_*.log`



- logs `ngrok_*.log`



- logs `cloudflare_errors_*.log`



- `mdl_security_audit.log`







## Signaux Importants



- nombre d appels API



- erreurs de validation



- cles revoquees



- taux de partage public



- historique des scores mu



- presence de divergences



- statut du tunnel externe







## Endpoints Utiles



- `GET /status`



- `GET /v1/mu/check`



- `GET /v1/mu/history`



- `GET /v1/growth/events`



- `GET /share/mu/{share_id}`







## Ce Qu On Doit Pouvoir Diagnostiquer



- un moteur qui ne demarre pas



- une cle API refusee



- un quota atteint



- un partage public absent



- un dashboard qui ne se rafraichit plus



- un tunnel coupe







## Regles De Journalisation



- horodater chaque evenement important



- masquer les cles partiellement



- tronquer les journaux volumineux



- conserver des fichiers lisibles par session







## Bonnes Pratiques



- separer logs applicatifs et logs d erreur



- surveiller le fichier de PID si un script le produit



- utiliser des traces courtes mais exploitables



- preferer des indicateurs de sante simples et stables







## Inference



La structure exacte des journaux derives peut varier selon le script de lancement utilise. Cette page decrit le socle commun observable dans les fichiers de la branche.





---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
