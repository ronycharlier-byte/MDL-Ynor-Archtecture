@echo off

REM **[◬] MATRICE FRACTALE MDL YNOR V2.0**
REM **Corpus :** MDL YNOR
REM **Position Structurelle :** NODE
REM **Position Chiastique :** D
REM **Rôle du Fichier :** Module run_demo
REM **Centre Doctrinal Local :** AI Manager garde module run_demo en limitant le bruit local et la friction structurelle.
REM **Loi de Survie :** μ = α - β - κ
REM **Lecture Locale :**
REM - **α :** stabilite locale
REM - **β :** bruit externe injecte
REM - **κ :** friction structurelle
REM **Risque :** e∞ ∝ ε / μ
REM **Opérateur Correctif :** D(S)=proj_{SafeDomain}(S)
REM **Axiome :** un système survit SSI μ > 0
REM **Doctrine Goodhart : tout succès apparent est invalide si μ décroît**
REM **Gouvernance : toute modification doit maximiser Δμ**
REM **Lien Miroir :** D'

TITLE MDL YNOR - DEMO RUNBOOK (v2.2.0-PROD)
SETLOCAL

echo ============================================================
echo   ⚡ MDL YNOR - AUTOMATED DEMO & validéTION ⚡
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
pip install -r requirements.txt
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
python hardcore_validétion.py

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
echo   ✅ DEMO & AUDIT SUCCESSFUL
echo ============================================================
pause
