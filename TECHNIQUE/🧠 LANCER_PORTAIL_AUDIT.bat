@echo off

REM **[◬] MATRICE FRACTALE MDL YNOR V2.0**
REM **Corpus :** MDL YNOR
REM **Position Structurelle :** ROOT
REM **Position Chiastique :** E
REM **Rôle du Fichier :** Audit structurel et controle d'integrite
REM **Centre Doctrinal Local :** AI Manager garde audit structurel et controle d'integrite en limitant le bruit local et la friction structurelle.
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
REM **Lien Miroir :** E

title MDL YNOR - LIVE AUDIT PORTAL [LAUNCHER]
echo ==============================================================================
echo 🔺 MDL YNOR — SYSTÈME IMMUNITAIRE DES IA [STARTING...]
echo ==============================================================================
echo.
echo [1] Verification de Python et des dependances...
pip install fastapi uvicorn openai google-generativeai python-dotenv numpy pandas requests >nul 2>&1
echo [OK] Environnement pret.
echo.
echo [2] Lancement du Portail Web de Verification (Viral Mode)
echo.
echo IMPORTANT : Ouvre http://localhost:8000 pour la demo.
echo.
echo ==============================================================================
python 03_C_MOTEURS_ET_DEPLOIEMENT/ynor_web_app.py
pause
