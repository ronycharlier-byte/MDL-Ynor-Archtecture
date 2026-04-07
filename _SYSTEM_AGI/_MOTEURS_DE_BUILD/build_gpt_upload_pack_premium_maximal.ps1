$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$pack = Join-Path $root "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL"
$zip = Join-Path $root "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL.zip"

if (Test-Path $pack) {
    Remove-Item -Recurse -Force $pack
}
New-Item -ItemType Directory -Path $pack -Force | Out-Null

$entries = @(
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_MASTER_FINAL\PROMPT_GPT_FINAL_MOINS_8000.md"; Dest = "PROMPT_GPT_FINAL_MOINS_8000.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_MASTER_FINAL\PROMPT_CORPUS_SECURISE_RIGOUREUX.md"; Dest = "PROMPT_CORPUS_SECURISE_RIGOUREUX.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_MASTER_FINAL\PROMPT_CORPUS_SECURISE_RIGOUREUX_PREMIUM.md"; Dest = "PROMPT_CORPUS_SECURISE_RIGOUREUX_PREMIUM.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_MASTER_FINAL\MASTER_FINAL.md"; Dest = "MASTER_FINAL.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_HOMEPAGE\HOMEPAGE_DU_CORPUS.md"; Dest = "HOMEPAGE_DU_CORPUS.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_HOMEPAGE\SITE_MAP.md"; Dest = "SITE_MAP.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_PUBLIC_BRIEF\PRESENTATION_PUBLIQUE.md"; Dest = "PRESENTATION_PUBLIQUE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_PUBLIC_BRIEF\PUBLIC_BRIEF.md"; Dest = "PUBLIC_BRIEF.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_EXECUTIVE_DIGEST\EXECUTIVE_DIGEST.md"; Dest = "EXECUTIVE_DIGEST.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_EXECUTIVE_DIGEST\FICHE_UNE_PAGE.md"; Dest = "FICHE_UNE_PAGE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_EDITION_CANONIQUE_FINALE\PORTAIL_CANONIQUE_FINAL.md"; Dest = "PORTAIL_CANONIQUE_FINAL.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_EDITION_CANONIQUE_FINALE\01_DOCUMENTS_CENTRAUX\INDEX_MAITRE_FRACTAL_CHIASTIQUE.md"; Dest = "INDEX_MAITRE_FRACTAL_CHIASTIQUE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_EDITION_CANONIQUE_FINALE\01_DOCUMENTS_CENTRAUX\CARTE_VISUELLE_FRACTALE_CHIASTIQUE.md"; Dest = "CARTE_VISUELLE_FRACTALE_CHIASTIQUE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\00_EDITION_CANONIQUE_FINALE\01_DOCUMENTS_CENTRAUX\MANIFESTE_FRACTAL_CHIASTE_UNIVERSEL.md"; Dest = "MANIFESTE_FRACTAL_CHIASTE_UNIVERSEL.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\00_NODE.md"; Dest = "03C_NODE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\04_INDEX\index.json"; Dest = "03C_index.json" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\_03_CORE_AGI_ENGINES\README.md"; Dest = "03C_CORE_ENGINES_README.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\_04_DEPLOYMENT_AND_API\README.md"; Dest = "03C_DEPLOYMENT_API_README.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\_04_DEPLOYMENT_AND_API\ynor_api_server.py"; Dest = "03C_ynor_api_server.py" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\_04_DEPLOYMENT_AND_API\requirements.txt"; Dest = "03C_requirements.txt" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\03_C_MOTEURS_ET_DEPLOIEMENT\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\_04_DEPLOYMENT_AND_API\Dockerfile"; Dest = "03C_Dockerfile" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\04_X_NOYAU_MEMOIRE\00_NODE.md"; Dest = "04X_NODE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\04_X_NOYAU_MEMOIRE\04_INDEX\index.json"; Dest = "04X_index.json" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\04_X_NOYAU_MEMOIRE\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\mdl_intelligence_report.json"; Dest = "04X_mdl_intelligence_report.json" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\05_C_PRIME_VALIDATION_ET_TESTS\00_NODE.md"; Dest = "05Cprime_NODE.md" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\05_C_PRIME_VALIDATION_ET_TESTS\04_INDEX\index.json"; Dest = "05Cprime_index.json" },
    @{ Source = "FRACTAL_CHIASTE_UNIVERSEL\05_C_PRIME_VALIDATION_ET_TESTS\01_SOURCE_IMPLANTEE\MDL_Ynor_Framework\tests\test_shareable_mu_audit.py"; Dest = "05Cprime_test_shareable_mu_audit.py" }
)

foreach ($entry in $entries) {
    $source = Join-Path $root $entry.Source
    $destination = Join-Path $pack $entry.Dest
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $destination -Force
    }
}

$readme = @"
# GPT UPLOAD PACK PREMIUM MAXIMAL

Ce pack est la version premium maximale recommandee pour un GPT Ynor tres solide.

Il combine:
- instructions compactes
- navigation strategique du corpus
- couches publique, executive et canonique
- axe moteur et deploiement
- axe validation et tests
- noeud memoire

Usage recommande:
1. Mettre PROMPT_GPT_FINAL_MOINS_8000.md dans les instructions du GPT.
2. Ajouter ensuite les autres fichiers comme base de connaissances.

Copyright Rony Charlier. Tous droits reserves.
"@

Set-Content -Path (Join-Path $pack "README_GPT_UPLOAD_PACK_PREMIUM_MAXIMAL.md") -Value $readme -Encoding UTF8

if (Test-Path $zip) {
    Remove-Item -Force $zip
}

Compress-Archive -Path (Join-Path $pack "*") -DestinationPath $zip -CompressionLevel Optimal

Write-Output "Pack folder: $pack"
Write-Output "Pack zip: $zip"
Get-ChildItem $pack | Select-Object Name, Length
