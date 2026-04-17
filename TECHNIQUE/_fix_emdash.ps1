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

$corpusRoot = "c:\Users\ronyc\Desktop\Corpus\MDL Ynor"
$emdash = [string][char]0x2014
$count = 0

Get-ChildItem -Path $corpusRoot -Recurse -Include "*.md","*.py" -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\\.gemini\\' -and
    $_.FullName -notmatch '\\\.obsidian\\'
} | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    if ($content.Contains('u{2014}')) {
        $newContent = $content.Replace('u{2014}', $emdash)
        [System.IO.File]::WriteAllText($_.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
        $count++
    }
}
Write-Host "Fixed em-dash in $count files"
