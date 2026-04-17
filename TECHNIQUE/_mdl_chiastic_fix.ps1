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

# MDL YNOR - FIX CHIASTIC POSITION MAPPING
# Pass 2: Replace generic ROOT with correct chiastic positions

$corpusRoot = "c:\Users\ronyc\Desktop\Corpus\MDL Ynor"
$fixCount = 0

# Mapping: directory prefix -> chiastic position, role, alpha, beta, kappa, miroir, centre
$mappings = @(
    @{ prefix="00_OMEGA_PORTAIL"; pos="Omega. Portail Entree Structurel"; role="Enveloppe matricielle externe, face entree du systeme"; a="Capacite accueil et routage structurel du portail"; b="Desorientation utilisateur, bruit interface"; k="Complexite navigation et couches indexation"; mir="08_OMEGA_PRIME_API_REFERENCE"; cen="Le portail est le premier gardien de mu" }
    @{ prefix="00_CORPUS_AUDIT"; pos="Omega. Audit Structurel Canonique"; role="Verificateur integrite et manifeste SHA256 du corpus"; a="Rigueur de audit, couverture verifications"; b="Fichiers orphelins, incoherences non detectees"; k="Temps calcul empreintes et traversee"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Audit est la mesure directe de mu" }
    @{ prefix="01_A_FONDATION"; pos="A. Vision / Fondation"; role="Ouverture axiomatique, cadre constitutionnel"; a="Force legislative, capacite a poser les axiomes fondateurs"; b="Interpretation divergente, rhetorique non formelle"; k="Complexite textuelle et redondance des regles"; mir="07_A_PRIME_ARCHIVES_ET_RELEASES"; cen="La fondation encode la loi de survie" }
    @{ prefix="02_B_THEORIE"; pos="B. Constitution / Theorie"; role="Developpement theorique, preuves formelles"; a="Puissance demonstrative irrefutable des theoremes"; b="Instabilite calculs, ambiguite hypotheses"; k="Cout computationnel de verification des preuves"; mir="06_B_PRIME_GOUVERNANCE_ET_DIFFUSION"; cen="La theorie est le squelette de mu" }
    @{ prefix="03_C_MOTEURS"; pos="C. Formalisme / Moteurs"; role="Moteurs actifs, APIs, deploiement algorithmique"; a="Algorithmes implementant D(S)=proj SafeDomain"; b="Exceptions non gerees, crash, boucles infinies"; k="Couplage fort, dependances inutiles, dette technique"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Le moteur est operateur D(S) incarne" }
    @{ prefix="04_X_NOYAU"; pos="E. Centre Doctrinal / Noyau"; role="Centre chiastique absolu, memoire vectorielle"; a="Densite semantique et coherence du noyau"; b="Corruption des embeddings, derive vectorielle"; k="Volume de stockage et cout de retrieval"; mir="AUTO-REFERENT (centre chiastique)"; cen="Le noyau EST mu incarne" }
    @{ prefix="05_C_PRIME"; pos="D prime. Verification / Validation"; role="Retour miroir par validation empirique, stress tests"; a="Resilience empirique mesurable sous perturbation"; b="Bruit simulation (Navier-Stokes, entropique)"; k="Temps et infrastructure de simulation"; mir="03_C_MOTEURS_ET_DEPLOIEMENT"; cen="La validation est la mesure empirique de mu" }
    @{ prefix="06_B_PRIME"; pos="C prime. Protocoles / Gouvernance"; role="Reprise normative, securitaire, diffusion"; a="Coercivite de AI Manager, force de gouvernance"; b="Intervention humaine irrationnelle"; k="Cycles approbation, reunions, bureaucratie"; mir="02_B_THEORIE_ET_PREUVES"; cen="La gouvernance est le gardien de delta-mu" }
    @{ prefix="07_A_PRIME"; pos="B prime. Gouvernance / Archives"; role="Cloture recursive par archives et releases"; a="Fidelite empreinte fossilisee, integrite archivale"; b="Corruption des archives, perte de versions"; k="Volume de stockage, redondance backups"; mir="01_A_FONDATION"; cen="Archive est la preuve retrospective que mu fut maintenu" }
    @{ prefix="08_OMEGA_PRIME"; pos="A prime. Transmission / Cloture"; role="Enveloppe reference finale, API technique"; a="Exhaustivite reference API, fidelite transmission"; b="Obsolescence documentation, decalage code/doc"; k="Maintenance synchronisation API/implementation"; mir="00_OMEGA_PORTAIL_ET_EDITION"; cen="La cloture transmet mu au monde exterieur" }
    @{ prefix="09_LAUNCH"; pos="A prime. Transmission / Lancement"; role="Assets de lancement viral, diffusion publique"; a="Impact viral, portee de transmission"; b="Deformation du message lors de diffusion"; k="Cout de production et distribution assets"; mir="01_A_FONDATION"; cen="Le lancement projette mu dans espace public" }
    @{ prefix="_SYSTEM_AGI"; pos="E. Centre Doctrinal / Systeme AGI"; role="Couche systeme AGI, orchestration intelligences"; a="Capacite orchestration autonome"; b="Hallucination systemique, derive orchestrateur"; k="Complexite coordination sous-systemes"; mir="04_X_NOYAU_MEMOIRE"; cen="Systeme AGI est operateur D(S) echelle globale" }
    @{ prefix="BITGET"; pos="C. Formalisme / Execution Marche"; role="Interface execution marche, bridge exchanges"; a="Vitesse execution et fidelite ordres"; b="Slippage, latence reseau, manipulation"; k="Frais transaction, complexite API"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Execution marche est test terminal de mu" }
    @{ prefix="YNOR_CLOUD"; pos="C. Formalisme / Deploiement Cloud"; role="Infrastructure deploiement cloud souverain"; a="Disponibilite 24/7, resilience infrastructure"; b="Pannes cloud, timeout, limitations"; k="Cout hebergement et maintenance"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Le cloud est substrat physique de D(S)" }
    @{ prefix="SecondBrain"; pos="E. Centre Doctrinal / Memoire Secondaire"; role="Memoire secondaire Obsidian"; a="Richesse et interconnexion des notes"; b="Fragmentation, notes orphelines"; k="Temps navigation et recherche"; mir="04_X_NOYAU_MEMOIRE"; cen="SecondBrain est miroir humain du noyau" }
    @{ prefix="theory"; pos="B. Constitution / Theorie Pure"; role="Noyau theorique pur, resultats fondamentaux"; a="Purete formelle et rigueur demonstrations"; b="Erreurs de raisonnement, gaps logiques"; k="Abstraction excessive"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="La theorie pure est fondement absolu de mu" }
    @{ prefix="ynor_engine"; pos="C. Formalisme / Moteur Central"; role="Module Python central du moteur Ynor"; a="Precision algorithmique, couverture regimes"; b="Bugs, edge cases non geres"; k="Complexite cyclomatique, couplage"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Moteur central est incarnation computationnelle de D(S)" }
    @{ prefix="config"; pos="A. Vision / Configuration"; role="Configuration systeme, parametres et constantes"; a="Clarte et exhaustivite des parametres"; b="Conflits configuration, defauts dangereux"; k="Nombre parametres et interdependances"; mir="07_A_PRIME_ARCHIVES_ET_RELEASES"; cen="La configuration encode les seuils de mu" }
    @{ prefix="dashboard"; pos="C prime. Protocoles / Visualisation"; role="Dashboard monitoring et visualisation temps reel"; a="Clarte affichage de mu en temps reel"; b="Metriques trompeuses (Goodhart), latence"; k="Charge de rendu, rafraichissement continu"; mir="03_C_MOTEURS_ET_DEPLOIEMENT"; cen="Le dashboard est observatoire de mu" }
    @{ prefix="data"; pos="E. Centre Doctrinal / Donnees"; role="Donnees brutes, datasets, series temporelles"; a="Qualite et fraicheur des donnees"; b="Donnees corrompues, manquantes, biaisees"; k="Volume stockage et temps chargement"; mir="04_X_NOYAU_MEMOIRE"; cen="Les donnees sont signal entree de mu" }
    @{ prefix="execution"; pos="C. Formalisme / Execution"; role="Module execution decisions et ordres"; a="Vitesse et fiabilite execution"; b="Erreurs execution, ordres rejetes"; k="Latence reseau, overhead serialisation"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Execution passe mu theorique a mu reel" }
    @{ prefix="monitoring"; pos="D prime. Verification / Monitoring"; role="Surveillance continue, alertes et logs"; a="Couverture monitoring, sensibilite alertes"; b="Faux positifs, alertes manquees"; k="Cout stockage logs et traitement"; mir="03_C_MOTEURS_ET_DEPLOIEMENT"; cen="Monitoring est mesure continue de mu" }
    @{ prefix="rag_system"; pos="E. Centre Doctrinal / RAG"; role="Systeme RAG, retrieval augmented generation"; a="Fidelite retrieval et pertinence chunks"; b="Hallucination LLM, degradation signal"; k="Poids chunks RAG et tokens"; mir="04_X_NOYAU_MEMOIRE"; cen="RAG est canal de transmission de mu vers LLM" }
    @{ prefix="static"; pos="A prime. Transmission / Assets Statiques"; role="Ressources statiques, CSS, JS, images"; a="Performance et accessibilite assets"; b="Assets obsoletes, liens casses"; k="Taille bundle et temps chargement"; mir="09_LAUNCH_ASSETS"; cen="Assets transmettent forme visuelle de mu" }
    @{ prefix="supreme_bot"; pos="C. Formalisme / Bot Souverain"; role="Deploiement bot trading souverain"; a="Autonomie decisionnelle, robustesse bot"; b="Crash, deconnexion, decisions erronees"; k="Ressources serveur, complexite maintenance"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Bot souverain est agent autonome de D(S)" }
    @{ prefix="supreme_temp"; pos="C. Formalisme / Staging Temporaire"; role="Zone staging temporaire deploiements"; a="Isolation et securite environnement test"; b="Fuite donnees staging vers production"; k="Synchronisation staging/production"; mir="05_C_PRIME_VALIDATION_ET_TESTS"; cen="Staging est laboratoire de mu" }
)

function Find-Mapping($filePath) {
    $rel = $filePath.Substring($corpusRoot.Length + 1)
    $parts = $rel -split '\\'
    $firstDir = $parts[0]
    
    foreach ($m in $mappings) {
        if ($firstDir.StartsWith($m.prefix)) {
            return $m
        }
    }
    return $null
}

# Collect files
$allFiles = Get-ChildItem -Path $corpusRoot -Recurse -Include "*.md" -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\\.obsidian\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\\.gemini\\'
}

Write-Host "=== CHIASTIC POSITION FIX ==="
Write-Host "MD files: $($allFiles.Count)"

foreach ($file in $allFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        
        # Only process files that have our header with ROOT position
        if ($content -notmatch '\*\*Position Chiastique :\*\* ROOT') {
            continue
        }
        
        $m = Find-Mapping $file.FullName
        if ($null -eq $m) { continue }
        
        $fn = [System.IO.Path]::GetFileNameWithoutExtension($file.FullName)
        $depth = ($file.FullName.Substring($corpusRoot.Length + 1) -split '\\').Count
        $sp = switch ($depth) { 1 {"ROOT"} 2 {"LAYER"} 3 {"MODULE"} default {"NODE"} }
        
        # Replace the generic values with specific ones
        $newContent = $content
        $newContent = $newContent -replace '\*\*Position Structurelle :\*\* NODE', "**Position Structurelle :** $sp"
        $newContent = $newContent -replace '\*\*Position Chiastique :\*\* ROOT', "**Position Chiastique :** $($m.pos)"
        $newContent = $newContent -replace "Composant racine du corpus MDL Ynor [^\r\n]+", "$($m.role) `u{2014} $fn"
        $newContent = $newContent -replace "Chaque fichier racine porte la loi de survie mu = alpha - beta - kappa", $m.cen
        $newContent = $newContent -replace "Coherence structurelle globale du corpus", $m.a
        $newContent = $newContent -replace "Fragmentation, incoherence inter-modules", $m.b
        $newContent = $newContent -replace "Complexite de synchronisation totale", $m.k
        $newContent = $newContent -replace '\*\*Lien Miroir :\*\* Symetrie topologique avec architecture centrale', "**Lien Miroir :** $($m.mir)"
        
        if ($newContent -ne $content) {
            [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
            $fixCount++
            if ($fixCount % 50 -eq 0) { Write-Host "  ... $fixCount files fixed" }
        }
    }
    catch {
        Write-Host "[ERR] $($file.FullName)"
    }
}

# Now fix PY files too
$pyFiles = Get-ChildItem -Path $corpusRoot -Recurse -Include "*.py" -File | Where-Object {
    $_.FullName -notmatch '\\\.git\\' -and
    $_.FullName -notmatch '\\__pycache__\\' -and
    $_.FullName -notmatch '\\\.gemini\\'
}

Write-Host "PY files: $($pyFiles.Count)"

foreach ($file in $pyFiles) {
    try {
        $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
        
        if ($content -notmatch '# Position Chiastique : ROOT') {
            continue
        }
        
        $m = Find-Mapping $file.FullName
        if ($null -eq $m) { continue }
        
        $fn = [System.IO.Path]::GetFileNameWithoutExtension($file.FullName)
        $depth = ($file.FullName.Substring($corpusRoot.Length + 1) -split '\\').Count
        $sp = switch ($depth) { 1 {"ROOT"} 2 {"LAYER"} 3 {"MODULE"} default {"NODE"} }
        
        $newContent = $content
        $newContent = $newContent -replace '# Position Structurelle : NODE', "# Position Structurelle : $sp"
        $newContent = $newContent -replace '# Position Chiastique : ROOT', "# Position Chiastique : $($m.pos)"
        $newContent = $newContent -replace "Composant racine du corpus MDL Ynor [^\r\n]+", "$($m.role) `u{2014} $fn"
        $newContent = $newContent -replace "Chaque fichier racine porte la loi de survie mu = alpha - beta - kappa", $m.cen
        $newContent = $newContent -replace "Coherence structurelle globale du corpus", $m.a
        $newContent = $newContent -replace "Fragmentation, incoherence inter-modules", $m.b
        $newContent = $newContent -replace "Complexite de synchronisation totale", $m.k
        $newContent = $newContent -replace '# Lien Miroir : Symetrie topologique avec architecture centrale', "# Lien Miroir : $($m.mir)"
        
        if ($newContent -ne $content) {
            [System.IO.File]::WriteAllText($file.FullName, $newContent, (New-Object System.Text.UTF8Encoding $true))
            $fixCount++
            if ($fixCount % 50 -eq 0) { Write-Host "  ... $fixCount files fixed" }
        }
    }
    catch {
        Write-Host "[ERR] $($file.FullName)"
    }
}

Write-Host ""
Write-Host "=== CHIASTIC FIX COMPLETE ==="
Write-Host "Files with corrected chiastic positions: $fixCount"
