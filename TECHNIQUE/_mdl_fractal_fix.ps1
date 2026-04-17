# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
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
# **Lien Miroir :** E

# MDL YNOR FRACTAL MATRIX - UNICODE FIX PASS
# Replaces literal u{XXXX} sequences with actual Unicode characters

$corpusRoot = "c:\Users\ronyc\Desktop\Corpus\MDL Ynor"
$fixCount = 0

# Unicode character map
$umap = @{
    'u{25EC}' = [char]0x25EC   # ◬
    'u{00F4}' = [char]0x00F4   # ô
    'u{2014}' = [char]0x2014   # —
    'u{03BC}' = [char]0x03BC   # μ
    'u{03B1}' = [char]0x03B1   # α
    'u{03B2}' = [char]0x03B2   # β
    'u{03BA}' = [char]0x03BA   # κ
    'u{221E}' = [char]0x221E   # ∞
    'u{221D}' = [char]0x221D   # ∝
    'u{03B5}' = [char]0x03B5   # ε
    'u{00E9}' = [char]0x00E9   # é
    'u{00E8}' = [char]0x00E8   # è
    'u{00EE}' = [char]0x00EE   # î
    'u{0394}' = [char]0x0394   # Δ
}

# Collect files
$allFiles = @()
$allFiles += Get-ChildItem -Path $corpusRoot -Recurse -Include "*.md","*.py" -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\\.obsidian\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\\.gemini\\'
}

Write-Host "=== UNICODE FIX PASS ==="
Write-Host "Files to scan: $($allFiles.Count)"

foreach ($file in $allFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        
        # Check if file has any u{XXXX} literals
        if ($content -match 'u\{[0-9A-Fa-f]{4}\}') {
            $newContent = $content
            foreach ($key in $umap.Keys) {
                $newContent = $newContent.Replace($key, [string]$umap[$key])
            }
            
            if ($newContent -ne $content) {
                [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
                $fixCount++
                Write-Host "[FIX] $($file.FullName)"
            }
        }
    }
    catch {
        Write-Host "[ERR] $($file.FullName) - $($_.Exception.Message)"
    }
}

Write-Host ""
Write-Host "=== FIX COMPLETE ==="
Write-Host "Files fixed: $fixCount"
