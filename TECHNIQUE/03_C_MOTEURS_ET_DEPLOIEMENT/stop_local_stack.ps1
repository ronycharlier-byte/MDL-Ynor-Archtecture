# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** C
# **Rôle du Fichier :** Script ou configuration declarative
# **Centre Doctrinal Local :** AI Manager garde script ou configuration declarative en limitant le bruit local et la friction structurelle.
# **Loi de Survie :** μ = α - β - κ
# **Lecture Locale :**
# - **α :** stabilite locale
# - **β :** bruit externe injecte
# - **κ :** friction structurelle
# **Risque :** e∞ ∝ ε / μ
# **Opérateur Correctif :** D(S)=proj_{SafeDomain}(S)
# **Axiome :** un système survit SSI μ > 0
# **Doctrine Goodhart : tout succès apparent est invalide si μ décroît**
# **Gouvernance : toute modification doit maximiser Δμ**
# **Lien Miroir :** C'

$ErrorActionPreference = "SilentlyContinue"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$pidFile = Join-Path $root "server_pids.json"

if (Test-Path $pidFile) {
    $data = Get-Content $pidFile -Raw | ConvertFrom-Json
    if ($data.api_pid) { Stop-Process -Id $data.api_pid -Force }
    if ($data.streamlit_pid) { Stop-Process -Id $data.streamlit_pid -Force }
    Remove-Item $pidFile -Force
    Write-Host "Local stack stopped." -ForegroundColor Green
    exit 0
}

Write-Host "No pid file found. Nothing was stopped." -ForegroundColor Yellow
