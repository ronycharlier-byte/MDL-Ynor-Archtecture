> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D'
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
> **Lien Miroir :** D / 03_C_MOTEURS_ET_DEPLOIEMENT
# MIROIR TEXTUEL - run_demo.bat

Source : MDL_Ynor_Framework\_08_EXPERIMENTS_AND_DEMOS\run_demo.bat
Taille : 1307 octets
SHA256 : 3dcd933bb99a83e00ec2df7d3f8fefae13b87031a76de7fa8c565df9f251689a

```text
@echo off
TITLE MDL YNOR - DEMO RUNBOOK (v2.2.0-PROD)
SETLOCAL

echo ============================================================
echo ⚡ MDL YNOR - AUTOMATED DEMO & validéTION ⚡
echo ============================================================

:: 1. CHECK VIRTUAL ENV
IF NOT EXIST venv (
 echo [INFO] Creating virtual environment...
 python -m venv venv
)

echo [INFO] Activating environment...
CALL venv\Scripts\activate

:: 2. INSTALL DEPS
echo [INFO] Installing required dependencies...
06_D_PRIME_MIROIR_C_PRIME_VALIDATION_TESTS_DEMONSTRATION_IPYNB_161208.md
pip install -e .

:: 3. ENVIRONMENT CHECK
IF NOT EXIST .env (
 echo [WARNING] No .env file found. Copying template...
 copy .env.template .env
 echo [ACTION] Please edit your .env file and add your API keys!
)

:: 4. RUN validéTION
echo.
echo [1/3] RUNNING HARDCORE validéTION (MU MARGIN)...
python hardcore_validation.py

:: 5. RUN EXPERIMENT
echo.
echo [2/3] RUNNING AGI MUTATION EXPERIMENT...
python run_experiment.py

:: 6. NOTEBOOK LAUNCH (INFO)
echo.
echo [3/3] DEMO COMPLETE. 
echo [INFO] To view the Jupyter Notebook, run:
echo jupyter notebook ynor_core_demonstration.ipynb
echo.

echo ============================================================
echo ✅ DEMO & AUDIT SUCCESSFUL
echo ============================================================
pause

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
