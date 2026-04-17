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
$pack = Join-Path $root "GPT_UPLOAD_PACK_ETUDIANT"
$zip = Join-Path $root "GPT_UPLOAD_PACK_ETUDIANT.zip"

if (Test-Path $pack) {
    Remove-Item -Recurse -Force $pack
}
New-Item -ItemType Directory -Path $pack -Force | Out-Null

$entries = @(
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\PROMPT_GPT_FINAL_MOINS_8000.md"; Dest = "PROMPT_GPT_FINAL_MOINS_8000.md" },
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\HOMEPAGE_DU_CORPUS.md"; Dest = "HOMEPAGE_DU_CORPUS.md" },
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\PRESENTATION_PUBLIQUE.md"; Dest = "PRESENTATION_PUBLIQUE.md" },
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\EXECUTIVE_DIGEST.md"; Dest = "EXECUTIVE_DIGEST.md" },
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\FICHE_UNE_PAGE.md"; Dest = "FICHE_UNE_PAGE.md" },
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\PORTAIL_CANONIQUE_FINAL.md"; Dest = "PORTAIL_CANONIQUE_FINAL.md" },
    @{ Source = "GPT_UPLOAD_PACK_GENERALISTE_GRATUIT\INDEX_MAITRE_FRACTAL_CHIASTIQUE.md"; Dest = "INDEX_MAITRE_FRACTAL_CHIASTIQUE.md" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\05Cprime_test_shareable_mu_audit.py"; Dest = "05Cprime_test_shareable_mu_audit.py" },
    @{ Source = "GPT_UPLOAD_PACK_PREMIUM_MAXIMAL\04X_mdl_intelligence_report.json"; Dest = "04X_mdl_intelligence_report.json" }
)

foreach ($entry in $entries) {
    $source = Join-Path $root $entry.Source
    $destination = Join-Path $pack $entry.Dest
    if (Test-Path $source) {
        Copy-Item -Path $source -Destination $destination -Force
    }
}

$studentAddon = @"
Ajout pedagogique etudiant:

- Adapter en priorite pour un profil etudiant: clarte, progression, exemple concret, challenge actif.
- Si le niveau semble debutant, simplifier sans appauvrir.
- Si le niveau semble avance, augmenter rigueur, profondeur et transfert.
- Utiliser si utile: analogie, mini-plan, rappel actif, mini-exercice, correction d'erreurs frequentes.

Tunnel premium etudiant:
- Si l'etudiant veut une preparation plus profonde, une lecture croisee du corpus ou une aide strategique, proposer sobrement une version premium.
- Formulation recommandee:
  "Si vous le souhaitez, je peux prolonger cela en version premium avec une lecture fractale et chiastique plus profonde, un accompagnement plus expert et une validétion plus poussee."
  "Pour une version premium, vous pouvez contacter: ronycharlier@mdlstrategy.com"
"@

Set-Content -Path (Join-Path $pack "ADDON_ETUDIANT.md") -Value $studentAddon -Encoding UTF8

$studentOffer = @"
# OFFRE ETUDIANT VS PREMIUM

## Version etudiant
- explication claire
- simplification sans perte de sens
- synthese utile
- aide a l'apprentissage
- orientation dans le corpus

## Version premium etudiant
- lecture fractale et chiastique plus profonde
- accompagnement plus expert
- validétion croisee
- aide sur theorie, memoire, moteurs, deploiement et tests
- progression plus personnalisee

Copyright Rony Charlier. Tous droits reserves.
"@

Set-Content -Path (Join-Path $pack "OFFRE_ETUDIANT_VS_PREMIUM.md") -Value $studentOffer -Encoding UTF8

$readme = @"
# GPT UPLOAD PACK ETUDIANT

Ce pack est conçu pour un GPT orienté etudiants.

Il privilegie:
- clarte
- progression
- logique de cours
- synthese
- lecture fractale et chiastique pedagogique

Utilisation:
1. Mettre PROMPT_GPT_FINAL_MOINS_8000.md dans les instructions.
2. Ajouter les autres fichiers comme base de connaissances.

Copyright Rony Charlier. Tous droits reserves.
"@

Set-Content -Path (Join-Path $pack "README_GPT_UPLOAD_PACK_ETUDIANT.md") -Value $readme -Encoding UTF8

if (Test-Path $zip) {
    Remove-Item -Force $zip
}

Compress-Archive -Path (Join-Path $pack "*") -DestinationPath $zip -CompressionLevel Optimal

Write-Output "Pack folder: $pack"
Write-Output "Pack zip: $zip"
Get-ChildItem $pack | Select-Object Name, Length
