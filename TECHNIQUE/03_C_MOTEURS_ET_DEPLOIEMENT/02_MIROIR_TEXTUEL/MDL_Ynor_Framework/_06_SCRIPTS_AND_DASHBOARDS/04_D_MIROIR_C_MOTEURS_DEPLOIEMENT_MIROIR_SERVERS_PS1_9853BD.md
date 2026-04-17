> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D
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
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
# MIROIR TEXTUEL - stop_mdl_servers.ps1

Source : MDL_Ynor_Framework\_06_SCRIPTS_AND_DASHBOARDS\stop_mdl_servers.ps1
Taille : 1366 octets
SHA256 : 6e6970b959d84e220137fe443335886301fe41fae80568d183b8f65072c13248

```text
# =============================================================================
# COPYRIGHT (c) 2026 CHARLIER RONY - TOUS DROITS RESERVES
# Script d'arret des serveurs MDL Ynor
# =============================================================================

$workDir = "C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework"
$pidFile = "$../../../../02_B_THEORIE_ET_PREUVES/07_REECRITURE_JSON_CHIASTIQUE/MDL_Ynor_Framework/_PREUVES_ET_RAPPORTS/03_C_FORMALISME_B_THEORIE_PREUVES_REECRITURE_JSON_FRACTALE_5B4F61.md"

if (Test-Path $pidFile) {
 $pids = Get-Content $pidFile | ConvertFrom-Json
 
 Write-Host "Arret du serveur Uvicorn (PID: $($pids.uvicorn_pid))..." -ForegroundColor Yellow
 Stop-Process -Id $pids.uvicorn_pid -Force -ErrorAction SilentlyContinue
 
 Write-Host "Arret de ngrok (PID: $($pids.ngrok_pid))..." -ForegroundColor Yellow
 Stop-Process -Id $pids.ngrok_pid -Force -ErrorAction SilentlyContinue
 
 Remove-Item $pidFile -Force
 Write-Host "Tous les serveurs ont ete arretes." -ForegroundColor Green
} else {
 Write-Host "Aucun serveur actif trouve (pas de ../../../../02_B_THEORIE_ET_PREUVES/07_REECRITURE_JSON_CHIASTIQUE/MDL_Ynor_Framework/_PREUVES_ET_RAPPORTS/03_C_FORMALISME_B_THEORIE_PREUVES_REECRITURE_JSON_FRACTALE_5B4F61.md)." -ForegroundColor Red
 
 # Fallback : tuer par nom de processus
 Write-Host "Tentative d'arret par nom de processus..." -ForegroundColor Yellow
 Get-Process -Name "uvicorn" -ErrorAction SilentlyContinue | Stop-Process -Force
 Get-Process -Name "ngrok" -ErrorAction SilentlyContinue | Stop-Process -Force
 Write-Host "Processus arretes." -ForegroundColor Green
}

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
