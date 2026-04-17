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

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$logDir = Join-Path $root "logs"

if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir | Out-Null
}

$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$apiLog = Join-Path $logDir "api_$timestamp.log"
$apiErr = Join-Path $logDir "api_errors_$timestamp.log"
$uiLog = Join-Path $logDir "streamlit_$timestamp.log"
$uiErr = Join-Path $logDir "streamlit_errors_$timestamp.log"

Write-Host "Launching MDL Ynor local stack..." -ForegroundColor Cyan

$apiProcess = Start-Process -FilePath "python" `
    -ArgumentList @("-m", "uvicorn", "api_app:app", "--host", "0.0.0.0", "--port", "8492") `
    -WorkingDirectory $root `
    -WindowStyle Hidden `
    -RedirectStandardOutput $apiLog `
    -RedirectStandardError $apiErr `
    -PassThru

Start-Sleep -Seconds 3

$dashboardPath = Join-Path $root "03_C_MOTEURS_ET_DEPLOIEMENT\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\_06_SCRIPTS_AND_DASHBOARDS\streamlit_dashboard.py"
$uiProcess = Start-Process -FilePath "python" `
    -ArgumentList @("-m", "streamlit", "run", $dashboardPath, "--server.port", "8501", "--server.address", "0.0.0.0") `
    -WorkingDirectory $root `
    -WindowStyle Hidden `
    -RedirectStandardOutput $uiLog `
    -RedirectStandardError $uiErr `
    -PassThru

@{
    api_pid = $apiProcess.Id
    streamlit_pid = $uiProcess.Id
    started_at = (Get-Date).ToString("o")
    api_url = "http://localhost:8492"
    dashboard_url = "http://localhost:8501"
    logs = $logDir
} | ConvertTo-Json -Depth 4 | Out-File (Join-Path $root "server_pids.json") -Encoding UTF8

Write-Host "API: http://localhost:8492" -ForegroundColor Green
Write-Host "Dashboard: http://localhost:8501" -ForegroundColor Green
Write-Host "Logs: $logDir" -ForegroundColor Gray
