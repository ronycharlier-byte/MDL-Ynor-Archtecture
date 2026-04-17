# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur de construction
# **Centre Doctrinal Local :** AI Manager garde moteur de construction en limitant le bruit local et la friction structurelle.
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

$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$pack = Join-Path $root "GPT_UPLOAD_PACK"
$zip = Join-Path $root "GPT_UPLOAD_PACK.zip"

New-Item -ItemType Directory -Path $pack -Force | Out-Null

$files = @(
    "FRACTAL_CHIASTE_UNIVERSEL\\00_MASTER_FINAL\\PROMPT_GPT_FINAL_MOINS_8000.md",
    "FRACTAL_CHIASTE_UNIVERSEL\\00_MASTER_FINAL\\PROMPT_CORPUS_SECURISE_RIGOUREUX.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_HOMEPAGE\\HOMEPAGE_DU_CORPUS.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_PUBLIC_BRIEF\\PRESENTATION_PUBLIQUE.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_EXECUTIVE_DIGEST\\EXECUTIVE_DIGEST.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_EXECUTIVE_DIGEST\\FICHE_UNE_PAGE.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_EDITION_CANONIQUE_FINALE\\PORTAIL_CANONIQUE_FINAL.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_EDITION_CANONIQUE_FINALE\\01_DOCUMENTS_CENTRAUX\\INDEX_MAITRE_FRACTAL_CHIASTIQUE.md",
    "_CLOUD_EXPORTS\\full_staging\\FRACTAL_CHIASTE_UNIVERSEL\\00_EDITION_CANONIQUE_FINALE\\01_DOCUMENTS_CENTRAUX\\CARTE_VISUELLE_FRACTALE_CHIASTIQUE.md",
    "GPT_UPLOAD_PACK\\README_GPT_UPLOAD_PACK.md"
)

foreach ($relativePath in $files) {
    $source = Join-Path $root $relativePath
    if (Test-Path $source) {
        $destination = Join-Path $pack (Split-Path $source -Leaf)
        $resolvedSource = (Resolve-Path $source).Path
        $resolvedDestination = $destination
        if (Test-Path $destination) {
            $resolvedDestination = (Resolve-Path $destination).Path
        }
        if ($resolvedSource -ne $resolvedDestination) {
            Copy-Item -Path $source -Destination $destination -Force
        }
    }
}

if (Test-Path $zip) {
    Remove-Item -Force $zip
}

Compress-Archive -Path (Join-Path $pack "*") -DestinationPath $zip -CompressionLevel Optimal

Write-Output "Pack folder: $pack"
Write-Output "Pack zip: $zip"
Get-ChildItem $pack | Select-Object Name, Length
