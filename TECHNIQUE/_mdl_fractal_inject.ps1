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

# MDL YNOR FRACTAL MATRIX INJECTOR V2.0
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$PSDefaultParameterValues['*:Encoding'] = 'utf8'

$corpusRoot = "c:\Users\ronyc\Desktop\Corpus\MDL Ynor"
$logFile = Join-Path $corpusRoot "_injection_log.txt"
$modifiedCount = 0
$skippedCount = 0
$skippedFiles = [System.Collections.ArrayList]::new()
$modifiedFiles = [System.Collections.ArrayList]::new()

# Build mapping table
$map = @{}

$map["00_OMEGA_PORTAIL"] = @{
    pos = "Omega. Portail Entree Structurel"
    role = "Enveloppe matricielle externe, face entree du systeme"
    alpha = "Capacite accueil et routage structurel du portail"
    beta = "Desorientation utilisateur, bruit interface"
    kappa = "Complexite navigation et couches indexation"
    miroir = "08_OMEGA_PRIME_API_REFERENCE"
    centre = "Le portail est le premier gardien de mu"
}

$map["00_CORPUS_AUDIT"] = @{
    pos = "Omega. Audit Structurel Canonique"
    role = "Verificateur integrite et manifeste SHA256 du corpus"
    alpha = "Rigueur de audit, couverture verifications"
    beta = "Fichiers orphelins, incoherences non detectees"
    kappa = "Temps calcul empreintes et traversee"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Audit est la mesure directe de mu : sans audit, mu est inconnu"
}

$map["01_A_FONDATION"] = @{
    pos = "A. Vision / Fondation"
    role = "Ouverture axiomatique, configuration initiale, cadre constitutionnel"
    alpha = "Force legislative, capacite a poser les axiomes fondateurs"
    beta = "Interpretation divergente, rhetorique non formelle"
    kappa = "Complexite textuelle et redondance des regles"
    miroir = "07_A_PRIME_ARCHIVES_ET_RELEASES"
    centre = "La fondation encode la loi de survie : mu = alpha - beta - kappa"
}

$map["02_B_THEORIE"] = @{
    pos = "B. Constitution / Theorie"
    role = "Developpement theorique, preuves formelles, formalisme mathematique"
    alpha = "Puissance demonstrative irrefutable des theoremes"
    beta = "Instabilite des calculs, ambiguite des hypotheses"
    kappa = "Cout computationnel de verification des preuves"
    miroir = "06_B_PRIME_GOUVERNANCE_ET_DIFFUSION"
    centre = "La theorie est le squelette de mu : chaque theoreme doit prouver que mu superieur a 0"
}

$map["03_C_MOTEURS"] = @{
    pos = "C. Formalisme / Moteurs"
    role = "Moteurs actifs, APIs, deploiement, implementation algorithmique"
    alpha = "Algorithmes implementant D(S) = proj SafeDomain S"
    beta = "Exceptions non gerees, crash, boucles infinies, latence"
    kappa = "Couplage fort, dependances inutiles, dette technique"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Le moteur est operateur D(S) incarne : il projette le reel dans le domaine sur"
}

$map["04_X_NOYAU"] = @{
    pos = "E. Centre Doctrinal / Noyau"
    role = "Centre chiastique absolu, memoire vectorielle, intelligence souveraine"
    alpha = "Densite semantique et coherence du noyau de connaissance"
    beta = "Corruption des embeddings, derive vectorielle"
    kappa = "Volume de stockage et cout de retrieval"
    miroir = "AUTO-REFERENT (centre chiastique)"
    centre = "Le noyau EST mu incarne : il porte la memoire, la doctrine, et le critere de survie"
}

$map["05_C_PRIME_VALIDATION"] = @{
    pos = "D prime. Verification / Validation"
    role = "Retour miroir par validation empirique, stress tests, reproductibilite"
    alpha = "Resilience empirique mesurable sous perturbation"
    beta = "Bruit de simulation (Navier-Stokes, entropique, adversarial)"
    kappa = "Temps et infrastructure de simulation, cout computationnel"
    miroir = "03_C_MOTEURS_ET_DEPLOIEMENT"
    centre = "La validation est la mesure empirique de mu : si les tests passent mais mu decroit, Goodhart active"
}

$map["06_B_PRIME_GOUVERNANCE"] = @{
    pos = "C prime. Protocoles / Gouvernance"
    role = "Reprise normative, securitaire, commerciale, diffusion et soumission"
    alpha = "Coercivite de AI Manager, force de gouvernance"
    beta = "Intervention humaine irrationnelle, pression politique"
    kappa = "Cycles approbation, reunions, bureaucratie"
    miroir = "02_B_THEORIE_ET_PREUVES"
    centre = "La gouvernance est le gardien de delta-mu : toute modification doit maximiser la marge dissipative"
}

$map["07_A_PRIME_ARCHIVES"] = @{
    pos = "B prime. Gouvernance / Archives"
    role = "Cloture recursive par archives, releases et distributions"
    alpha = "Fidelite de empreinte fossilisee, integrite archivale"
    beta = "Corruption des archives, perte de versions"
    kappa = "Volume de stockage, redondance des backups"
    miroir = "01_A_FONDATION"
    centre = "Archive est la preuve retrospective que mu superieur a 0 a ete maintenu dans le temps"
}

$map["08_OMEGA_PRIME"] = @{
    pos = "A prime. Transmission / Cloture"
    role = "Enveloppe de reference finale, API technique, cloture du systeme"
    alpha = "Exhaustivite de la reference API, fidelite de transmission"
    beta = "Obsolescence de la documentation, decalage code/doc"
    kappa = "Maintenance de la synchronisation API/implementation"
    miroir = "00_OMEGA_PORTAIL_ET_EDITION"
    centre = "La cloture transmet mu au monde exterieur"
}

$map["09_LAUNCH_ASSETS"] = @{
    pos = "A prime. Transmission / Lancement"
    role = "Assets de lancement viral, diffusion publique du paradigme"
    alpha = "Impact viral, portee de transmission du message"
    beta = "Deformation du message lors de la diffusion"
    kappa = "Cout de production et de distribution des assets"
    miroir = "01_A_FONDATION"
    centre = "Le lancement est la projection de mu dans espace public"
}

$map["_SYSTEM_AGI"] = @{
    pos = "E. Centre Doctrinal / Systeme AGI"
    role = "Couche systeme AGI, orchestration des intelligences"
    alpha = "Capacite orchestration autonome et decision souveraine"
    beta = "Hallucination systemique, derive de orchestrateur"
    kappa = "Complexite de coordination des sous-systemes"
    miroir = "04_X_NOYAU_MEMOIRE"
    centre = "Le systeme AGI est operateur D(S) echelle globale"
}

$map["BITGET"] = @{
    pos = "C. Formalisme / Execution Marche"
    role = "Interface execution marche, bridge vers les exchanges"
    alpha = "Vitesse execution et fidelite des ordres"
    beta = "Slippage, latence reseau, manipulation de marche"
    kappa = "Frais de transaction, complexite de API exchange"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Execution marche est le test terminal de mu"
}

$map["YNOR_CLOUD_DEPLOY"] = @{
    pos = "C. Formalisme / Deploiement Cloud"
    role = "Infrastructure de deploiement cloud, runtime souverain"
    alpha = "Disponibilite 24/7, resilience de infrastructure"
    beta = "Pannes cloud, timeout, limitations de ressources"
    kappa = "Cout hebergement et de maintenance"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Le cloud est le substrat physique de D(S)"
}

$map["SecondBrain"] = @{
    pos = "E. Centre Doctrinal / Memoire Secondaire"
    role = "Memoire secondaire Obsidian, base de connaissances etendue"
    alpha = "Richesse et interconnexion des notes de connaissance"
    beta = "Fragmentation, notes orphelines, incoherence"
    kappa = "Temps de navigation et de recherche dans le vault"
    miroir = "04_X_NOYAU_MEMOIRE"
    centre = "Le SecondBrain est le miroir humain du noyau"
}

$map["theory"] = @{
    pos = "B. Constitution / Theorie Pure"
    role = "Noyau theorique pur, resultats fondamentaux"
    alpha = "Purete formelle et rigueur des demonstrations"
    beta = "Erreurs de raisonnement, gaps logiques"
    kappa = "Abstraction excessive, inaccessibilite"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "La theorie pure est le fondement absolu de mu"
}

$map["ynor_engine"] = @{
    pos = "C. Formalisme / Moteur Central"
    role = "Module Python central du moteur Ynor"
    alpha = "Precision algorithmique et couverture des regimes"
    beta = "Bugs, edge cases non geres, degradation sous charge"
    kappa = "Complexite cyclomatique, couplage inter-modules"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Le moteur central est incarnation computationnelle de D(S)"
}

$map["config"] = @{
    pos = "A. Vision / Configuration"
    role = "Configuration systeme, parametres et constantes"
    alpha = "Clarte et exhaustivite des parametres"
    beta = "Conflits de configuration, valeurs par defaut dangereuses"
    kappa = "Nombre de parametres et interdependances"
    miroir = "07_A_PRIME_ARCHIVES_ET_RELEASES"
    centre = "La configuration encode les seuils de mu"
}

$map["dashboard"] = @{
    pos = "C prime. Protocoles / Visualisation"
    role = "Dashboard de monitoring et visualisation temps reel"
    alpha = "Clarte de affichage de mu en temps reel"
    beta = "Metriques trompeuses (Goodhart), latence affichage"
    kappa = "Charge de rendu, rafraichissement continu"
    miroir = "03_C_MOTEURS_ET_DEPLOIEMENT"
    centre = "Le dashboard est observatoire de mu"
}

$map["data"] = @{
    pos = "E. Centre Doctrinal / Donnees"
    role = "Donnees brutes, datasets, series temporelles"
    alpha = "Qualite et fraicheur des donnees"
    beta = "Donnees corrompues, manquantes ou biaisees"
    kappa = "Volume de stockage et temps de chargement"
    miroir = "04_X_NOYAU_MEMOIRE"
    centre = "Les donnees sont le signal entree de mu"
}

$map["execution"] = @{
    pos = "C. Formalisme / Execution"
    role = "Module execution des decisions et ordres"
    alpha = "Vitesse et fiabilite execution"
    beta = "Erreurs execution, ordres rejetes"
    kappa = "Latence reseau et overhead de serialisation"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Execution est le passage de mu theorique a mu reel"
}

$map["monitoring"] = @{
    pos = "D prime. Verification / Monitoring"
    role = "Surveillance continue, alertes et logs"
    alpha = "Couverture de monitoring et sensibilite des alertes"
    beta = "Faux positifs, alertes manquees, alert fatigue"
    kappa = "Cout de stockage des logs et de traitement"
    miroir = "03_C_MOTEURS_ET_DEPLOIEMENT"
    centre = "Le monitoring est la mesure continue de mu"
}

$map["rag_system"] = @{
    pos = "E. Centre Doctrinal / RAG"
    role = "Systeme RAG, retrieval augmented generation"
    alpha = "Fidelite de retrieval et pertinence des chunks"
    beta = "Hallucination du LLM, degradation du signal"
    kappa = "Poids des chunks RAG et tokens consommes"
    miroir = "04_X_NOYAU_MEMOIRE"
    centre = "Le RAG est le canal de transmission de mu vers le LLM"
}

$map["static"] = @{
    pos = "A prime. Transmission / Assets Statiques"
    role = "Ressources statiques, CSS, JS, images"
    alpha = "Performance et accessibilite des assets"
    beta = "Assets obsoletes, liens casses"
    kappa = "Taille du bundle et temps de chargement"
    miroir = "09_LAUNCH_ASSETS"
    centre = "Les assets transmettent la forme visuelle de mu"
}

$map["supreme_bot_deploy"] = @{
    pos = "C. Formalisme / Bot Souverain"
    role = "Deploiement du bot de trading souverain"
    alpha = "Autonomie decisionnelle et robustesse du bot"
    beta = "Crash, deconnexion, decisions erronees sous volatilite"
    kappa = "Ressources serveur et complexite de maintenance"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Le bot souverain est agent autonome de D(S)"
}

$map["supreme_temp"] = @{
    pos = "C. Formalisme / Staging Temporaire"
    role = "Zone de staging temporaire pour deploiements"
    alpha = "Isolation et securite de environnement de test"
    beta = "Fuite de donnees de staging vers production"
    kappa = "Synchronisation staging/production"
    miroir = "05_C_PRIME_VALIDATION_ET_TESTS"
    centre = "Le staging est le laboratoire de mu"
}

$defaultMap = @{
    pos = "ROOT"
    role = "Composant racine du corpus MDL Ynor"
    alpha = "Coherence structurelle globale du corpus"
    beta = "Fragmentation, incoherence inter-modules"
    kappa = "Complexite de synchronisation totale"
    miroir = "Symetrie topologique avec architecture centrale"
    centre = "Chaque fichier racine porte la loi de survie mu = alpha - beta - kappa"
}

function Get-Mapping($filePath) {
    $rel = $filePath.Replace($corpusRoot + "\", "")
    $firstDir = ($rel -split "\\")[0]
    foreach ($key in $map.Keys) {
        if ($firstDir.StartsWith($key)) {
            return $map[$key]
        }
    }
    return $defaultMap
}

function Get-StructPos($filePath) {
    $rel = $filePath.Replace($corpusRoot + "\", "")
    $depth = ($rel -split "\\").Count
    if ($depth -eq 1) { return "ROOT" }
    elseif ($depth -eq 2) { return "LAYER" }
    elseif ($depth -eq 3) { return "MODULE" }
    else { return "NODE" }
}

function Build-MdH($m, $sp, $fp) {
    $fn = [System.IO.Path]::GetFileNameWithoutExtension($fp)
    $lines = @(
        "> **[`u{25EC}] MATRICE FRACTALE MDL YNOR V2.0**"
        "> **Corpus :** MDL YNOR"
        "> **Position Structurelle :** $sp"
        "> **Position Chiastique :** $($m.pos)"
        "> **R`u{00F4}le du Fichier :** $($m.role) `u{2014} $fn"
        "> **Centre Doctrinal Local :** $($m.centre)"
        "> **Loi de Survie :** `$`u{03BC} = `$`u{03B1} - `$`u{03B2} - `$`u{03BA}"
        "> **Lecture Locale :**"
        "> - **`$`u{03B1} :** $($m.alpha)"
        "> - **`$`u{03B2} :** $($m.beta)"
        "> - **`$`u{03BA} :** $($m.kappa)"
        "> **Risque :** e`u{221E} `u{221D} `u{03B5} / `u{03BC}"
        "> **Op`u{00E9}rateur Correctif :** D(S)=proj_{SafeDomain}(S)"
        "> **Axiome :** un syst`u{00E8}me survit SSI `u{03BC} > 0"
        "> **Doctrine Goodhart :** tout succ`u{00E8}s apparent est invalide si `u{03BC} d`u{00E9}cro`u{00EE}t"
        "> **Gouvernance :** toute modification doit maximiser `u{0394}`u{03BC}"
        "> **Lien Miroir :** $($m.miroir)"
        ""
    )
    return ($lines -join "`r`n")
}

function Build-PyH($m, $sp, $fp) {
    $fn = [System.IO.Path]::GetFileNameWithoutExtension($fp)
    $lines = @(
        "# `u{25EC} MATRICE FRACTALE MDL YNOR V2.0"
        "# Corpus : MDL YNOR"
        "# Position Structurelle : $sp"
        "# Position Chiastique : $($m.pos)"
        "# R`u{00F4}le du Fichier : $($m.role) `u{2014} $fn"
        "# Centre Doctrinal Local : $($m.centre)"
        "# Loi de Survie : `u{03BC} = `u{03B1} - `u{03B2} - `u{03BA}"
        "# Lecture Locale :"
        "#   `u{03B1} : $($m.alpha)"
        "#   `u{03B2} : $($m.beta)"
        "#   `u{03BA} : $($m.kappa)"
        "# Risque : e`u{221E} `u{221D} `u{03B5} / `u{03BC}"
        "# Op`u{00E9}rateur Correctif : D(S)=proj_{SafeDomain}(S)"
        "# Axiome : un syst`u{00E8}me survit SSI `u{03BC} > 0"
        "# Doctrine Goodhart : tout succ`u{00E8}s apparent est invalide si `u{03BC} d`u{00E9}cro`u{00EE}t"
        "# Gouvernance : toute modification doit maximiser `u{0394}`u{03BC}"
        "# Lien Miroir : $($m.miroir)"
        ""
    )
    return ($lines -join "`r`n")
}

$mdHeaderRx = '^\s*>\s*\*\*\[.{0,3}\]\s*MATRICE FRACTALE'
$pyHeaderRx = '^#\s*.{0,3}\s*MATRICE FRACTALE'

# Collect files
$mdFiles = Get-ChildItem -Path $corpusRoot -Recurse -Include "*.md" -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\\.obsidian\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\_injection_log' -and
    $_.FullName -notmatch '\\\.gemini\\'
}

$pyFiles = Get-ChildItem -Path $corpusRoot -Recurse -Include "*.py" -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\\.gemini\\'
}

Write-Host "=== MDL YNOR FRACTAL MATRIX INJECTOR V2.0 ==="
Write-Host "MD files: $($mdFiles.Count)"
Write-Host "PY files: $($pyFiles.Count)"
Write-Host "Total: $($mdFiles.Count + $pyFiles.Count)"
Write-Host ""

# Process MD files
foreach ($file in $mdFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        if ([string]::IsNullOrWhiteSpace($content)) {
            $skippedCount++
            [void]$skippedFiles.Add("$($file.FullName) [EMPTY]")
            continue
        }

        $m = Get-Mapping $file.FullName
        $sp = Get-StructPos $file.FullName
        $newH = Build-MdH $m $sp $file.FullName

        $lines = $content -split "`r?`n"

        # Find existing header
        $hStart = -1
        $hEnd = -1
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match $mdHeaderRx) {
                $hStart = $i
                break
            }
        }

        if ($hStart -ge 0) {
            # Find end: look for Lien Miroir line
            for ($i = $hStart; $i -lt $lines.Count; $i++) {
                if ($lines[$i] -match '>\s*\*\*Lien Miroir') {
                    $hEnd = $i
                    break
                }
            }
            if ($hEnd -lt 0) { $hEnd = $hStart + 16 }
            # Skip blank lines after header
            while (($hEnd + 1) -lt $lines.Count -and [string]::IsNullOrWhiteSpace($lines[$hEnd + 1])) {
                $hEnd++
            }

            $before = ""
            if ($hStart -gt 0) {
                $before = ($lines[0..($hStart - 1)] -join "`r`n") + "`r`n"
            }
            $after = ""
            if (($hEnd + 1) -lt $lines.Count) {
                $after = ($lines[($hEnd + 1)..($lines.Count - 1)] -join "`r`n")
            }
            $newContent = $before + $newH + $after
        }
        else {
            $newContent = $newH + $content
        }

        [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
        $modifiedCount++
        [void]$modifiedFiles.Add($file.FullName)
        Write-Host "[OK] $($file.FullName)"
    }
    catch {
        $skippedCount++
        [void]$skippedFiles.Add("$($file.FullName) [ERR: $($_.Exception.Message)]")
        Write-Host "[SKIP] $($file.FullName)"
    }
}

# Process PY files
foreach ($file in $pyFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        if ([string]::IsNullOrWhiteSpace($content)) {
            $skippedCount++
            [void]$skippedFiles.Add("$($file.FullName) [EMPTY]")
            continue
        }

        $m = Get-Mapping $file.FullName
        $sp = Get-StructPos $file.FullName
        $newH = Build-PyH $m $sp $file.FullName

        $lines = $content -split "`r?`n"

        $hStart = -1
        $hEnd = -1
        for ($i = 0; $i -lt $lines.Count; $i++) {
            if ($lines[$i] -match $pyHeaderRx) {
                $hStart = $i
                break
            }
        }

        if ($hStart -ge 0) {
            for ($i = $hStart; $i -lt $lines.Count; $i++) {
                if ($lines[$i] -match '^#\s*Lien Miroir') {
                    $hEnd = $i
                    break
                }
            }
            if ($hEnd -lt 0) { $hEnd = $hStart + 16 }
            while (($hEnd + 1) -lt $lines.Count -and [string]::IsNullOrWhiteSpace($lines[$hEnd + 1])) {
                $hEnd++
            }

            $before = ""
            if ($hStart -gt 0) {
                $before = ($lines[0..($hStart - 1)] -join "`r`n") + "`r`n"
            }
            $after = ""
            if (($hEnd + 1) -lt $lines.Count) {
                $after = ($lines[($hEnd + 1)..($lines.Count - 1)] -join "`r`n")
            }
            $newContent = $before + $newH + $after
        }
        else {
            # Preserve shebang
            $insertAt = 0
            if ($lines.Count -gt 0 -and $lines[0] -match '^#!') { $insertAt = 1 }
            if ($insertAt -lt $lines.Count -and $lines[$insertAt] -match '^#.*coding') { $insertAt++ }

            if ($insertAt -gt 0) {
                $before = ($lines[0..($insertAt - 1)] -join "`r`n") + "`r`n"
                $after = ($lines[$insertAt..($lines.Count - 1)] -join "`r`n")
                $newContent = $before + $newH + $after
            }
            else {
                $newContent = $newH + $content
            }
        }

        [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
        $modifiedCount++
        [void]$modifiedFiles.Add($file.FullName)
        Write-Host "[OK] $($file.FullName)"
    }
    catch {
        $skippedCount++
        [void]$skippedFiles.Add("$($file.FullName) [ERR: $($_.Exception.Message)]")
        Write-Host "[SKIP] $($file.FullName)"
    }
}

Write-Host ""
Write-Host "============================================"
Write-Host "=== INJECTION COMPLETE ==="
Write-Host "============================================"
Write-Host "Files modified: $modifiedCount"
Write-Host "Files skipped:  $skippedCount"

$logLines = @(
    "MDL YNOR FRACTAL MATRIX INJECTION LOG"
    "Date: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    "Files Modified: $modifiedCount"
    "Files Skipped: $skippedCount"
    ""
    "=== MODIFIED FILES ==="
)
$logLines += $modifiedFiles
$logLines += ""
$logLines += "=== SKIPPED FILES ==="
$logLines += $skippedFiles

[System.IO.File]::WriteAllText($logFile, ($logLines -join "`r`n"), (New-Object System.Text.UTF8Encoding $true))
Write-Host "Log: $logFile"
