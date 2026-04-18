@echo off

REM **[◬] MATRICE FRACTALE MDL YNOR V2.0**
REM **Corpus :** MDL YNOR
REM **Position Structurelle :** NODE
REM **Position Chiastique :** B'
REM **Rôle du Fichier :** Module silent_start
REM **Centre Doctrinal Local :** AI Manager garde module silent_start en limitant le bruit local et la friction structurelle.
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
REM **Lien Miroir :** B

:: Ce script lance l'API Cloud Ynor sans afficher de fenetre visible
cd /d "C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_04_DEPLOYMENT_AND_API"
python -m uvicorn ynor_api_server:app --port 8492 --host 0.0.0.0
