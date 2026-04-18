> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** E
> **Role du Fichier :** Noyau de connaissance
> **Centre Doctrinal Local :** noyau local de memoire et de conservation
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** densite de connaissance exploitable
> - **β :** redondance et entropie injectee
> - **κ :** cout de maintenance et de reconciliation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** E / 04_X_NOYAU_MEMOIRE
---


STATUS: CANONICAL | V11.13.0 | AUDIT: CERTIFIED | FINAL CONSOLIDATED REVIEW / V11.13.0


---


# LLM Clients - Consistency Improvements











## Issues to Fix











### 1. `validéte_model()` is never called





- Add validation call in `get_llm()` with warning (not error) for unknown models











### 2. ~~Inconsistent parameter handling~~ (Fixed)





- GoogleClient now accepts unified `api_key` and maps it to `google_api_key`











### 3. ~~`base_url` accepted but ignored~~ (Fixed)





- All clients now pass `base_url` to their respective LLM constructors











### 4. ~~Update validétors.py with models from CLI~~ (Fixed)





- Synced in v0.2.2







---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
