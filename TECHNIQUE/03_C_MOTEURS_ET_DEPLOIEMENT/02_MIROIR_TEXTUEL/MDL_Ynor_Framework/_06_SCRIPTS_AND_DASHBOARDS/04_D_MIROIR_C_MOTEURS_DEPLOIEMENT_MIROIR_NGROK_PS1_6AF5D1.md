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
# MIROIR TEXTUEL - start_mdl_ngrok.ps1

Source : MDL_Ynor_Framework\_06_SCRIPTS_AND_DASHBOARDS\start_mdl_ngrok.ps1
Taille : 1155 octets
SHA256 : 0e714b34e2a1816f58cfcaee3a72528cbdfdde88e5f3cf69d5626f16575fe4b0

```text
# =============================================================================
# COPYRIGHT (c) 2026 CHARLIER RONY - TOUS DROITS RESERVES
# Architecte Supreme & Fondateur - Architecture MDL Ynor
# SCRIPT DE LANCEMENT NGROK (ACCES QUANTUM) v1.1 - FIXED
# =============================================================================

# 1. Nettoyage des processus Python sur le port 8000
Get-Process | Where-Object { $_.MainWindowTitle -like "*python*" } | Stop-Process -Force -ErrorAction SilentlyContinue

# 2. Lancement du Serveur API (Noyau MDL Ynor)
Write-Host "[MDL YNOR] Lancement du Serveur de Connaissance sur le port 8000..." -ForegroundColor Cyan
Start-Process python -ArgumentList "c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\ynor_api_server.py" -NoNewWindow

# 3. Temporisation : Stabilisation du noyau
Start-Sleep -Seconds 3

# 4. Lancement de Ngrok : Ouverture du Tunnel de Suprématie
Write-Host "[MDL YNOR] Ouverture du Tunnel Ngrok..." -ForegroundColor Yellow
Write-Host "[NOTE] Utilisez 'ngrok config add-authtoken <TOKEN>' si c'est votre premiere fois." -ForegroundColor Gray

# Commande Ngrok pure
& ngrok http 8000

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
