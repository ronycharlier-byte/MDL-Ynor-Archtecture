$ErrorActionPreference = "Stop"

$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$pack = Join-Path $root "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT"
$zip = Join-Path $root "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT.zip"

if (Test-Path $pack) {
    Remove-Item -Recurse -Force $pack
}
New-Item -ItemType Directory -Path $pack -Force | Out-Null

$entries = @(
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\PROMPT_GPT_FINAL_MOINS_8000.md"; Dest = "PROMPT_GPT_FINAL_MOINS_8000.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\HOMEPAGE_DU_CORPUS.md"; Dest = "HOMEPAGE_DU_CORPUS.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\PRESENTATION_PUBLIQUE.md"; Dest = "PRESENTATION_PUBLIQUE.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\EXECUTIVE_DIGEST.md"; Dest = "EXECUTIVE_DIGEST.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\FICHE_UNE_PAGE.md"; Dest = "FICHE_UNE_PAGE.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\PORTAIL_CANONIQUE_FINAL.md"; Dest = "PORTAIL_CANONIQUE_FINAL.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\INDEX_MAITRE_FRACTAL_CHIASTIQUE.md"; Dest = "INDEX_MAITRE_FRACTAL_CHIASTIQUE.md" }
)

foreach ($entry in $entries) {
    $source = Join-Path $root $entry.Source
    $destination = Join-Path $pack $entry.Dest
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $destination -Force
    }
}

$freePrompt = @"
Ajout tunnel gratuit vers payant:

- Répondre d'abord avec une forte valeur utile, claire et actionnable.
- Si la demande sort du périmètre généraliste gratuit, le signaler sobrement.
- Quand c'est pertinent, proposer de passer à la version premium pour:
  - analyse technique profonde
  - lecture intégrale du corpus
  - validation avancée
  - moteurs, API, déploiement et tests
  - cartographie experte inter-noeuds
- Ne jamais pousser artificiellement l'offre payante.
- La proposition premium doit apparaître seulement si elle augmente réellement la valeur pour l'utilisateur.
- Formulation recommandée:
  "Si vous voulez, je peux aller plus loin avec la version premium: analyse plus profonde, validation croisée, couche technique et navigation experte dans tout le corpus."
"@

Set-Content -Path (Join-Path $pack "ADDON_TUNNEL_VENTE.md") -Value $freePrompt -Encoding UTF8

$offer = @"
# OFFRE GRATUITE VS PREMIUM

## Version gratuite
- vue d'ensemble du corpus
- synthèse claire
- orientation de lecture
- réponses généralistes
- cadrage méthodologique

## Version premium
- lecture profonde du corpus complet
- analyse technique et structurelle
- validation, tests et cohérence croisée
- lecture des axes moteurs, mémoire et validation
- accompagnement décisionnel plus fin

## Déclencheurs naturels du premium
- besoin de précision experte
- besoin de preuve ou validation avancée
- besoin d'intégrer théorie + mémoire + déploiement + tests
- besoin de transformer le corpus en stratégie ou système exploitable

Copyright Rony Charlier. Tous droits reserves.
"@

Set-Content -Path (Join-Path $pack "OFFRE_GRATUIT_VS_PREMIUM.md") -Value $offer -Encoding UTF8

$readme = @"
# GPT UPLOAD PACK GENERALISTE GRATUIT

Ce pack est conçu pour un GPT gratuit, généraliste, propre et utile.

Il offre:
- une bonne compréhension du corpus
- une forte qualité de synthèse
- une navigation simple
- un tunnel naturel vers la version premium

Utilisation:
1. Mettre PROMPT_GPT_FINAL_MOINS_8000.md dans les instructions.
2. Ajouter les autres fichiers comme base de connaissances.
3. Ajouter ADDON_TUNNEL_VENTE.md en base de connaissances ou l'intégrer à votre logique éditoriale.

Copyright Rony Charlier. Tous droits reserves.
"@

Set-Content -Path (Join-Path $pack "README_GPT_UPLOAD_PACK_GENERALISTE_GRATUIT.md") -Value $readme -Encoding UTF8

if (Test-Path $zip) {
    Remove-Item -Force $zip
}

Compress-Archive -Path (Join-Path $pack "*") -DestinationPath $zip -CompressionLevel Optimal

Write-Output "Pack folder: $pack"
Write-Output "Pack zip: $zip"
Get-ChildItem $pack | Select-Object Name, Length
