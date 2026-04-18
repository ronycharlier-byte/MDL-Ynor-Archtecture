> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** MODULE
> **Position Chiastique :** B
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
> **Lien Miroir :** B' / 07_A_PRIME_ARCHIVES_ET_RELEASES
# MIROIR TEXTUEL - build_fractal_chiasm.ps1

Source : MDL Ynor Constitution\build_fractal_chiasm.ps1
Taille : 6807 octets
SHA256 : 02cfa9abba6e9b1032302c6f84d6da4772c662de965ab06841ffe1bc696fd8e6

```text
$ErrorActionPreference = "Stop"

$constitutionRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$outputRoot = Join-Path $constitutionRoot "FRACTAL_CHIASME_MDL_YNOR"

$nodes = @(
 @{
 Order = "01"
 Key = "A"
 Title = "AXIOMATIQUE_MINIMALE"
 Role = "Ouverture fondatrice"
 Mirror = "A_PRIME"
 Summary = "Le point d'entree du systeme. Les axiomes minimaux ouvrent la forme fractale."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor MATH\Chapitre I — Formalisation axiomatique minimale.pdf")
 )
 },
 @{
 Order = "02"
 Key = "B"
 Title = "THEOREMES_DE_LA_MARGE"
 Role = "Premier arc de dissipation"
 Mirror = "B_PRIME"
 Summary = "Le premier developpement porte la marge dissipative comme loi de propagation."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor — Théorèmes fondamentaux de la marge dissipative.pdf")
 )
 },
 @{
 Order = "03"
 Key = "C"
 Title = "THEORIE_STRUCTURELLE"
 Role = "Arc structural amont"
 Mirror = "C_PRIME"
 Summary = "La theorie structurelle prepare le renversement chiastique vers le noyau."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor — Théorie Structurelle des Systèmes Dissipatifs à Amplification Bornée.pdf")
 )
 },
 @{
 Order = "04"
 Key = "X"
 Title = "NOYAU_INTEGRAL"
 Role = "Centre chiastique"
 Mirror = "X"
 Summary = "Le centre integre les formulations mathématiques du noyau. Tout converge ici puis repart en reflet."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor MATH\Chapitre XVI — Formalisation mathématique intégrale du noyau MDL Ynor.pdf"),
 (Join-Path $constitutionRoot "Chapitre I — Formalisation mathématique intégrale du noyau MDL Ynor.pdf")
 )
 },
 @{
 Order = "05"
 Key = "C_PRIME"
 Title = "CONSTITUTION_STRUCTURELLE"
 Role = "Arc structural aval"
 Mirror = "C"
 Summary = "La constitution structurelle rejoue la theorie en forme inverse et plus normative."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor — Constitution Structurelle des Systèmes Dissipatifs à Amplification Bornée.pdf")
 )
 },
 @{
 Order = "06"
 Key = "B_PRIME"
 Title = "TRAITE_DYNAMIQUE"
 Role = "Second arc de dissipation"
 Mirror = "B"
 Summary = "Le traite reprend la dynamique au retour du centre et ferme l'enveloppe theorique."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor — Traité des dynamiques dissipatives et de la stabilité structurelle.pdf")
 )
 },
 @{
 Order = "07"
 Key = "A_PRIME"
 Title = "ARCHITECTURE_RECURSIVE"
 Role = "Cloture architecturale"
 Mirror = "A"
 Summary = "La cloture se fait par l'architecture, qui replie le corpus sur lui-meme et ouvre la recursion fractale."
 Sources = @(
 (Join-Path $constitutionRoot "MDL Ynor Archtecture_")
 )
 }
)

New-Item -ItemType Directory -Force -Path $outputRoot | Out-Null

$manifestLines = @(
 "# MANIFESTE FRACTAL CHIASTIQUE MDL YNOR",
 "",
 "Ordre chiastique : A -> B -> C -> X -> C' -> B' -> A'",
 "",
 "Centre : X / NOYAU_INTEGRAL",
 "",
 "Principe fractal : chaque noeud contient trois strates repetees.",
 "- 01_SOURCE : le document ou corpus source",
 "- 02_REFLET : son role miroir dans l'axe",
 "- 03_RECURSION : la regle de retour vers le centre et vers la paire",
 ""
)

$jsonNodes = @()

foreach ($node in $nodes) {
 $nodeFolderName = "{0}_{1}_{2}" -f $node.Order, $node.Key, $node.Title
 $nodeRoot = Join-Path $outputRoot $nodeFolderName
 $sourceRoot = Join-Path $nodeRoot "01_SOURCE"
 $mirrorRoot = Join-Path $nodeRoot "02_REFLET"
 $recursionRoot = Join-Path $nodeRoot "03_RECURSION"

 New-Item -ItemType Directory -Force -Path $sourceRoot, $mirrorRoot, $recursionRoot | Out-Null

 $copiedNames = @()
 foreach ($source in $node.Sources) {
 if (-not (Test-Path $source)) {
 continue
 }

 $destination = Join-Path $sourceRoot (Split-Path $source -Leaf)
 if (Test-Path $source -PathType Container) {
 Copy-Item -Path $source -Destination $destination -Recurse -Force
 } else {
 Copy-Item -Path $source -Destination $destination -Force
 }
 $copiedNames += (Split-Path $source -Leaf)
 }

 $nodeReadme = @(
 "# $($node.Key) - $($node.Title)",
 "",
 "Role : $($node.Role)",
 "",
 "Miroir chiastique : $($node.Mirror)",
 "",
 "Resume : $($node.Summary)",
 "",
 "Contenu source :",
 $(($copiedNames | ForEach-Object { "- $_" }) -join "`n"),
 "",
 "Implementation fractale :",
 "- 01_SOURCE contient le document ou le sous-corpus original.",
 "- 02_REFLET designe la paire miroir dans la structure chiastique.",
 "- 03_RECURSION rappelle le retour vers le centre X."
 ) -join "`r`n"
 Set-Content -Path (02_B_B_MIROIR_FONDATION_MIROIR_TEXTUEL_MDL_YNOR_CONSTITUTION_BUILD_FRACTAL_CHIASM_PS1.md") -Value $nodeReadme -Encoding UTF8

 $mirrorNote = @(
 "Noeud : $($node.Key)",
 "Paire miroir : $($node.Mirror)",
 "Centre : X / NOYAU_INTEGRAL",
 "Mouvement : aller -> centre -> retour"
 ) -join "`r`n"
 Set-Content -Path (02_B_B_MIROIR_FONDATION_MIROIR_TEXTUEL_MDL_YNOR_CONSTITUTION_BUILD_FRACTAL_CHIASM_PS1.md") -Value $mirrorNote -Encoding UTF8

 $recursionNote = @(
 "Recursion fractale du noeud $($node.Key)",
 "",
 "Regle 1 : lire la source.",
 "Regle 2 : identifier son miroir chiastique ($($node.Mirror)).",
 "Regle 3 : revenir au centre X.",
 "Regle 4 : rejouer la meme logique a l'interieur du corpus local."
 ) -join "`r`n"
 Set-Content -Path (02_B_B_MIROIR_FONDATION_MIROIR_TEXTUEL_MDL_YNOR_CONSTITUTION_BUILD_FRACTAL_CHIASM_PS1.md") -Value $recursionNote -Encoding UTF8

 $manifestLines += "- $nodeFolderName -> $($node.Role) -> miroir $($node.Mirror)"
 $jsonNodes += [pscustomobject]@{
 order = $node.Order
 key = $node.Key
 title = $node.Title
 role = $node.Role
 mirror = $node.Mirror
 summary = $node.Summary
 sources = $copiedNames
 }
}

$manifestLines += ""
$manifestLines += "Resultat : les fichiers demandes sont reorientes dans une arche documentaire fractale et chiastique sans toucher aux originaux."
Set-Content -Path (02_B_B_MIROIR_FONDATION_MIROIR_TEXTUEL_MDL_YNOR_CONSTITUTION_BUILD_FRACTAL_CHIASM_PS1.md") -Value ($manifestLines -join "`r`n") -Encoding UTF8

$jsonNodes | ConvertTo-Json -Depth 5 | Set-Content -Path (02_B_B_MIROIR_FONDATION_MIROIR_TEXTUEL_MDL_YNOR_CONSTITUTION_BUILD_FRACTAL_CHIASM_PS1.md") -Encoding UTF8

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
