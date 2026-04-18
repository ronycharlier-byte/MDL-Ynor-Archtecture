> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** MODULE
> **Position Chiastique :** B
> **Role du Fichier :** Surface miroir et symetrie locale
> **Centre Doctrinal Local :** boucle locale de reflet et de coherence
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence reflexive et effet miroir
> - **β :** derive de boucle et bruit de reflet
> - **κ :** cout de cycle et de stabilisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** B' / 07_A_PRIME_ARCHIVES_ET_RELEASES
# MIROIR TEXTUEL - docker-compose.yml

Source : MDL_Ynor_Framework\docker-compose.yml
Taille : 925 octets
SHA256 : 3e5182839e4f8efb5e84a712fa391f513997d19f5000c49bf8eeb7f7b27ed0be

```text
version: "3.8"

services:
 ynor-api:
 build: .
 image: ynor-agi-server:2.0
 container_name: ynor_api_server
 ports:
 - "8492:8492"
 environment:
 - YNOR_API_KEY=${YNOR_API_KEY}
 - MDL_PROD_WRITE_ENABLED=FALSE
 - DEFCON=1
 volumes:
 - ./.env:/app/.env
 - ./logs:/app/logs
 - ../../../03_C_MOTEURS_ET_DEPLOIEMENT/01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_03_CORE_AGI_ENGINES/MDL_YNOR_GPT_KNOWLEDGE/04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_SOURCE_CONTRAT_LICENCE_CC231A.md:/../../../03_C_MOTEURS_ET_DEPLOIEMENT/01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_03_CORE_AGI_ENGINES/MDL_YNOR_GPT_KNOWLEDGE/04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_SOURCE_CONTRAT_LICENCE_CC231A.md
 restart: unless-stopped
 healthcheck:
 test: ["CMD", "curl", "-f", "http://localhost:8492/status"]
 interval: 30s
 timeout: 10s
 retries: 3

 ynor-dashboard:
 image: ynor-agi-server:2.0
 container_name: ynor_dashboard
 command: streamlit run _06_SCRIPTS_AND_DASHBOARDS/streamlit_dashboard.py --server.port 8493 --server.address 0.0.0.0
 ports:
 - "8493:8493"
 depends_on:
 - ynor-api
 environment:
 - YNOR_API_KEY=${YNOR_API_KEY}
 restart: always

networks:
 default:
 name: ynor_network

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
