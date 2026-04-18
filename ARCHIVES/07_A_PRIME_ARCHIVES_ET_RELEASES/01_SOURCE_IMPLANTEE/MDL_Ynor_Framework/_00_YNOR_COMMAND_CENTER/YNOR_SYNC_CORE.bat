@echo off

REM **[◬] MATRICE FRACTALE MDL YNOR V2.0**
REM **Corpus :** MDL YNOR
REM **Position Structurelle :** NODE
REM **Position Chiastique :** B'
REM **Rôle du Fichier :** Module YNOR_SYNC_CORE
REM **Centre Doctrinal Local :** AI Manager garde module ynor_sync_core en limitant le bruit local et la friction structurelle.
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

setlocal
title YNOR CORE BRAIN SYNC

echo ========================================================
echo        🛡️ YNOR CORE - MISE À JOUR DU CERVEAU AGI
echo ========================================================
echo.
echo [1] - AJOUTER UNE EXPÉRIENCE / CHAT LOG (Ouvrir le Journal)
echo [2] - SYNCHRONISER LA CONNAISSANCE (Lancer l'Indexeur)
echo [3] - VOIR LES PROTOCOLES DE SÉCURITÉ
echo [4] - QUITTER
echo.

set /p choice="Action (1-4) : "

if "%choice%"=="1" (
    echo.
    echo [*] Ouverture du journal d'expérience...
    start notepad "c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_10_YNOR_AI_KNOWLEDGE_BASE_SOURCES\MDL_YNOR_CUSTOMER_EXPERIENCE_LOGS.md"
    echo [!] Une fois vos logs collés et enregistrés, relancez ce script et faites [2].
    pause
    goto end
)

if "%choice%"=="2" (
    echo.
    echo [*] Lancement de l'indexation globale (mu-scaling)...
    cd /d "c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_YNOR_GPT_KNOWLEDGE"
    python update_knowledge.py
    echo.
    echo [OK] Cerveau AGI à jour et synchronisé.
    pause
    goto end
)

if "%choice%"=="3" (
    echo.
    echo [*] Affichage des protocoles de sécurité actuels...
    type "c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_00_YNOR_COMMAND_CENTER\mdl_ynor_manifesto_governance.json"
    pause
    goto end
)

if "%choice%"=="4" exit

:end
exit
