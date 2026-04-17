# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur de correction
# **Centre Doctrinal Local :** AI Manager garde moteur de correction en limitant le bruit local et la friction structurelle.
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
# **Lien Miroir :** E

# MDL YNOR - FIX ROOT FILES CHIASTIC POSITION

$corpusRoot = "c:\Users\ronyc\Desktop\Corpus\MDL Ynor"
$fixCount = 0

# Mapping variables for ROOT files (Central hub)
$pos = "E. Centre Doctrinal / Racine Systémique"
$role = "Hub central architectural et orchestration primaire"
$a = "Densité et robustesse du point d'entrée"
$b = "Dispersion métrique et perte de cohésion initiale"
$k = "Charge cognitive d'initialisation"
$mir = "00_OMEGA_PORTAIL_ET_EDITION"
$cen = "La racine garantit la première observation de mu"
$emdash = [string][char]0x2014

$rootFiles = Get-ChildItem -Path $corpusRoot -File -Include "*.md","*.py" | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\\.obsidian\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\\.gemini\\'
}

Write-Host "Fixing Root Files..."

foreach ($file in $rootFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        
        # We need to preserve the filename dynamically
        $fn = [System.IO.Path]::GetFileNameWithoutExtension($file.FullName)
        
        $role_str = "Hub central architectural et orchestration primaire"
        if ($file.Name -match "README") {
            $role_str = "Manifeste d'entrée et Hub central de navigation"
        } elseif ($file.Name -match "ynor_engine") {
            $role_str = "Moteur central d'exécution et d'interface"
        }

        $full_role1 = $role_str + " " + $emdash + " " + $fn
        $full_role2 = $role_str + " u{2014} " + $fn
        
        $newContent = $content
        $newContent = $newContent -replace '\*\*Position Structurelle :\*\* NODE', "**Position Structurelle :** ROOT"
        $newContent = $newContent -replace '\*\*Position Chiastique :\*\* ROOT', "**Position Chiastique :** $pos"
        
        # Robust role replacement 
        $newContent = $newContent -replace "Composant racine du corpus MDL Ynor.*", $full_role1
        $newContent = $newContent -replace "Chaque fichier racine porte la loi de survie mu = alpha - beta - kappa", $cen
        $newContent = $newContent -replace "Coherence structurelle globale du corpus", $a
        $newContent = $newContent -replace "Fragmentation, incoherence inter-modules", $b
        $newContent = $newContent -replace "Complexite de synchronisation totale", $k
        $newContent = $newContent -replace '\*\*Lien Miroir :\*\* Symetrie topologique avec architecture centrale', "**Lien Miroir :** $mir"
        
        # Same replacements for Python # 
        $newContent = $newContent -replace '# Position Structurelle : NODE', "# Position Structurelle : ROOT"
        $newContent = $newContent -replace '# Position Chiastique : ROOT', "# Position Chiastique : $pos"
        $newContent = $newContent -replace '# Lien Miroir : Symetrie topologique avec architecture centrale', "# Lien Miroir : $mir"

        if ($newContent -ne $content) {
            [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
            $fixCount++
            Write-Host "  Fixed: $($file.Name)"
        }
    }
    catch {
        Write-Host "[ERR] $($file.FullName)"
    }
}

Write-Host "Fixed Root Files: $fixCount"
