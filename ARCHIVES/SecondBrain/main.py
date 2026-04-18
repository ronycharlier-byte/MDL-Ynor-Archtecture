# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Point d'entree principal du corpus
# **Centre Doctrinal Local :** AI Manager garde point d'entree principal du corpus en limitant le bruit local et la friction structurelle.
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

# Force l'encodage UTF-8 pour la sortie console (Windows fix)
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Charge les variables d'environnement (optionnel)
load_dotenv()

# Remplacer par votre clé API ou définir la variable d'environnement OPENAI_API_KEY
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY", "TA_CLE_API"))

# Chemins relatifs ajustés pour plus de flexibilité
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KNOWLEDGE_PATH = os.path.join(BASE_DIR, "KNOWLEDGE")
LEARNING_PATH = os.path.join(BASE_DIR, "LEARNING")  # 🔺 V6 : Mémoire d'apprentissage
CHAT_PATH = os.path.join(BASE_DIR, "chat_logs")
SYSTEM_PATH = os.path.join(BASE_DIR, "SYSTEM")

# Création automatique des répertoires
for _p in [KNOWLEDGE_PATH, LEARNING_PATH, CHAT_PATH, SYSTEM_PATH]:
    os.makedirs(_p, exist_ok=True)

# Structure de données : chaque note est un dict { "name": str, "content": str }
notes = []
vectors = []
index = None

# 🔺 V9 : OBJECTIVE LAYER + USER MODEL
def load_objectives():
    """Charge la direction du système."""
    obj_path = os.path.join(SYSTEM_PATH, "objectives.md")
    if os.path.exists(obj_path):
        with open(obj_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

def load_user_model():
    """Charge le profil cognitif de l'utilisateur."""
    um_path = os.path.join(SYSTEM_PATH, "user_model.md")
    if os.path.exists(um_path):
        with open(um_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# 🔺 1. LOAD NOTES
def load_notes():
    global notes, vectors

    if not os.path.exists(KNOWLEDGE_PATH):
        os.makedirs(KNOWLEDGE_PATH)

    files = [f for f in os.listdir(KNOWLEDGE_PATH) if f.endswith(".md")]
    
    if not files:
        print("Aucune note existante dans KNOWLEDGE. Initialisation avec une note vide pour l'index.")
        notes = [{"name": "init.md", "content": "Base de connaissance initiale vide."}]
        emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=notes[0]["content"]
        )
        vectors = [emb.data[0].embedding]
        return

    for file in files:
        with open(os.path.join(KNOWLEDGE_PATH, file), "r", encoding="utf-8") as f:
            text = f.read()

        emb = client.embeddings.create(
            model="text-embedding-3-small",
            input=text[:1000] # Limite pour l'embedding initial
        )

        vector = emb.data[0].embedding

        notes.append({"name": file, "content": text})
        vectors.append(vector)

# 🔺 2. BUILD INDEX
def build_index():
    global index
    if not vectors:
        return
    vec = np.array(vectors).astype("float32")
    index = faiss.IndexFlatL2(len(vec[0]))
    index.add(vec)

# 🔺 3. SEARCH
def search(query):
    if index is None or not notes:
        return [{"name": "none", "content": "Pas de contexte disponible."}]

    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=query
    )

    q = np.array([emb.data[0].embedding]).astype("float32")
    # S'assurer que k ne dépasse pas le nombre de notes
    k = min(3, len(notes))
    D, I = index.search(q, k=k)

    return [notes[i] for i in I[0] if i != -1]

# 🔺 4. THINK (AGENT — V9 FINAL)
def think(text):
    context = search(text)
    objectives = load_objectives()
    user_model = load_user_model()
    
    # 🔥 AUTO-LINK
    links = [f"[[Retrieved_Note_{i}]]" for i in range(len(context))]
    
    prompt_path = os.path.join(SYSTEM_PATH, "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        system_prompt = f.read()

    full_prompt = system_prompt + f"\n\n# OBJECTIFS SYSTÈME\n{objectives}\n\n# PROFIL UTILISATEUR\n{user_model}\n\nAjoute des liens Obsidian pertinents. Maximum 3 liens par note."

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": full_prompt},
            {"role": "user", "content": f"""
            CONTEXTE PROCHE:
            {[n.get('content', n) if isinstance(n, dict) else n for n in context]}

            LIENS SUGGÉRÉS (MAX 3):
            {links[:3]}

            INPUT:
            {text}
            """}
        ]
    )

    return response.choices[0].message.content

# 🔺 5. AUTO-UPDATE INDEX
def add_to_index(name, text):
    emb = client.embeddings.create(
        model="text-embedding-3-small",
        input=text[:1000]
    )
    vector = emb.data[0].embedding

    vectors.append(vector)
    notes.append({"name": name, "content": text})

    index.add(np.array([vector]).astype("float32"))
    print("Base vectorielle mise à jour.")

# 🔺 6. CREATE NOTE
def create_note(content, name):
    # Sanitize name
    name = name.replace(" ", "_").replace(".md", "")
    target_file = os.path.join(KNOWLEDGE_PATH, f"{name}.md")
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(content)
    
    add_to_index(f"{name}.md", content) # 🔥 Mise à jour auto de la mémoire
    print(f"Note créée et indexée : {target_file}")

# 🔺 7. QUALITY FILTER (V6 — retourne le score)
def quality_filter(text, return_score=False):
    """Évalue la qualité. Retourne bool par défaut, ou (bool, score) si return_score=True."""
    print("⚖️ Examen de la qualité...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Évalue la valeur réelle de cette idée (0-10). Réponds uniquement avec le chiffre."},
            {"role": "user", "content": text}
        ]
    )

    try:
        score_text = response.choices[0].message.content.strip()
        import re
        match = re.search(r'\d+', score_text)
        score = int(match.group()) if match else 0
        print(f"Score de qualité : {score}/10")
        passed = score >= 7
        return (passed, score) if return_score else passed
    except Exception as e:
        print(f"Erreur de filtrage : {e}")
        return (True, 5) if return_score else True

# 🔺 7b. SAVE TO LEARNING (V6 — Mémoire d'apprentissage)
def save_to_learning(content, name, score=0, reason="rejected"):
    """Sauvegarde les décisions rejetées dans LEARNING pour analyse ultérieure."""
    import datetime
    name = name.replace(" ", "_").replace(".md", "")
    target_file = os.path.join(LEARNING_PATH, f"{name}.md")
    
    header = f"""# LEARNING : {name}
**Score** : {score}/10
**Raison** : {reason}
**Date** : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
**Statut** : A analyser

---

"""
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(header + content)
    print(f"📓 Sauvegardé dans LEARNING : {target_file}")

# 🔺 7c. LEARN FROM FAILURES (V8 — STABILITÉ COGNITIVE)
ERROR_PATTERNS_FILE = os.path.join(SYSTEM_PATH, "error_patterns.json")
MAX_RULES = 10  # 🔺 V8 : Limite absolue de règles injectées

def load_error_patterns():
    """Charge la mémoire persistante des patterns d'erreurs."""
    import json
    if os.path.exists(ERROR_PATTERNS_FILE):
        with open(ERROR_PATTERNS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_error_patterns(patterns):
    """Sauvegarde la mémoire des patterns d'erreurs."""
    import json
    with open(ERROR_PATTERNS_FILE, "w", encoding="utf-8") as f:
        json.dump(patterns, f, indent=2, ensure_ascii=False)

def decay_errors(patterns):
    """Décroissance progressive : le système oublie les vieux patterns."""
    decayed = {}
    for key, val in patterns.items():
        new_val = round(val * 0.9, 2)
        if new_val >= 0.1:  # Seuil minimum — en-dessous on purge
            decayed[key] = new_val
    purged = len(patterns) - len(decayed)
    if purged > 0:
        print(f"🧹 Decay : {purged} pattern(s) oublié(s).")
    return decayed

def trim_rules(rules_text):
    """Garde uniquement les MAX_RULES règles les plus récentes."""
    lines = [l for l in rules_text.strip().splitlines() if l.strip().startswith("- ")]
    if len(lines) > MAX_RULES:
        trimmed = len(lines) - MAX_RULES
        lines = lines[-MAX_RULES:]
        print(f"✂️ Trim : {trimmed} règle(s) ancienne(s) retirée(s). Max = {MAX_RULES}.")
    return "\n".join(lines)

def sanity_check():
    """Vérifie la cohérence des règles injectées. Détecte contradictions et sur-optimisation."""
    prompt_path = os.path.join(SYSTEM_PATH, "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        current = f.read()
    
    marker = "# AUTO-LEARNING RULES"
    if marker not in current:
        print("🛡️ Sanity Check : Aucune règle injectée. OK.")
        return True
    
    rules_section = current[current.index(marker):]
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """Analyse ces règles système et détecte :
1. Contradictions entre règles (ex: "simplifier" vs "approfondir")
2. Sur-optimisation (trop restrictif, le système devient muet)
3. Redondances (règles qui disent la même chose)

Réponds avec ce format exact :
STATUS: OK ou PROBLEME
CONTRADICTIONS: [liste ou "aucune"]
REDONDANCES: [liste ou "aucune"]
RISQUE_MUTISME: [faible/moyen/élevé]
ACTION: [aucune / fusionner X et Y / supprimer Z]"""},
            {"role": "user", "content": rules_section}
        ],
        temperature=0.2
    )
    
    check_result = response.choices[0].message.content
    print(f"🛡️ Sanity Check :\n{check_result}")
    
    # Si problème critique détecté, on sauvegarde le rapport
    if "PROBLEME" in check_result.upper():
        import datetime
        report_path = os.path.join(SYSTEM_PATH, f"sanity_alert_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.md")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(f"# 🛡️ Alerte Sanity Check\n**Date** : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n{check_result}")
        print(f"⚠️ ALERTE sauvegardée : {report_path}")
        return False
    
    return True

def update_system_prompt(rules):
    """Injecte les règles apprises dans le prompt système (avec trim)."""
    prompt_path = os.path.join(SYSTEM_PATH, "prompt.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        current = f.read()
    
    # Récupérer les anciennes règles pour les fusionner
    marker = "# AUTO-LEARNING RULES"
    old_rules = ""
    if marker in current:
        old_rules = current[current.index(marker) + len(marker):]
        current = current[:current.index(marker)]
    
    # Fusionner anciennes + nouvelles, puis trim
    combined = old_rules.strip() + "\n" + rules.strip()
    trimmed = trim_rules(combined)
    
    updated = current.rstrip() + f"\n\n{marker}\n{trimmed}\n"
    with open(prompt_path, "w", encoding="utf-8") as f:
        f.write(updated)
    print(f"🔄 Prompt mis à jour : {len(trimmed.splitlines())} règles actives (max {MAX_RULES}).")

def learn_from_failures():
    """V8 : Analyse les échecs, extrait des règles, les injecte, puis régule."""
    import datetime
    import json
    print("🧠 FEEDBACK ACTIF V8 : Analyse + Régulation...")
    
    learning_files = [f for f in os.listdir(LEARNING_PATH) if f.endswith(".md")]
    if not learning_files:
        print("Aucun fichier dans LEARNING. Système encore trop jeune.")
        return None
    
    # Charger et décroître les patterns
    patterns = load_error_patterns()
    patterns = decay_errors(patterns)
    
    # Lire les échecs et mettre à jour les patterns
    failures = []
    for file in learning_files:
        with open(os.path.join(LEARNING_PATH, file), "r", encoding="utf-8") as f:
            content = f.read()
            failures.append(content)
            content_lower = content.lower()
            for tag in ["low_value", "redundant", "vague", "off_topic", "too_abstract"]:
                if tag in content_lower or (tag == "low_value" and "score" in content_lower):
                    patterns[tag] = patterns.get(tag, 0) + 1
    
    save_error_patterns(patterns)
    
    failures_text = "\n===\n".join(failures[-10:])
    patterns_text = json.dumps(patterns, indent=2)
    
    # ÉTAPE 1 : Analyser + extraire des règles
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": """Tu analyses des décisions rejetées par un filtre qualité.
Tu dois produire 2 choses :

PARTIE 1 — RAPPORT (pour l'humain)
## Patterns détectés
## Biais identifiés
## Ajustements recommandés

PARTIE 2 — RÈGLES MACHINE (pour injection dans le prompt)
Commence cette partie par la ligne exacte : ---RULES---
Puis liste exactement 1 à 5 règles courtes et directes que l'agent doit suivre.
Format : une règle par ligne, commençant par "- "
"""},
            {"role": "user", "content": f"""
PATTERNS ACCUMULÉS :
{patterns_text}

ÉCHECS RÉCENTS :
{failures_text}
"""}
        ],
        temperature=0.3
    )
    
    full_analysis = response.choices[0].message.content
    
    # ÉTAPE 2 : Extraire et injecter les règles (avec trim)
    rules = ""
    if "---RULES---" in full_analysis:
        rules = full_analysis.split("---RULES---")[1].strip()
        update_system_prompt(rules)
        print(f"🔺 Nouvelles règles extraites et injectées.")
    else:
        print("⚠️ Aucune règle extractible.")
    
    # ÉTAPE 3 : Sanity Check (détection de contradictions)
    is_sane = sanity_check()
    if not is_sane:
        print("⚠️ SANITY CHECK FAILED — Le système a détecté un risque de dérive.")
    
    # ÉTAPE 4 : Rapport
    report_name = f"learning_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M')}.md"
    report_path = os.path.join(SYSTEM_PATH, report_name)
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"""# 🧠 Rapport d'Apprentissage V8 (FEEDBACK ACTIF + RÉGULATION)
**Date** : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}
**Fichiers analysés** : {len(learning_files)}
**Patterns accumulés** : {json.dumps(patterns)}
**Règles injectées** : {"Oui" if rules else "Non"}
**Sanity Check** : {"PASS" if is_sane else "FAIL"}

---

{full_analysis}
""")
    
    print(f"📊 Rapport : {report_path}")
    print(f"📊 Patterns (post-decay) : {patterns}")
    return full_analysis

# 🔺 8. AUTO-THINK (V9 FINAL)
def auto_think():
    print("🧠 AUTO THINKING (Intelligence Alignée)...")
    objectives = load_objectives()
    user_model = load_user_model()
    notes_text = "\n---\n".join([n['content'] for n in notes[-10:]])

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": f"""
            OBJECTIFS :
            {objectives}

            PROFIL UTILISATEUR :
            {user_model}

            En respectant ces objectifs et ce profil, génère uniquement :
            - insights non évidents alignés avec la direction
            - connexions nouvelles entre piliers existants
            - amélioration système mesurable

            Format : bullet points directs, pas de blabla.
            Refuse toute idée faible ou hors-objectif.
            """},
            {"role": "user", "content": notes_text}
        ]
    )

    return response.choices[0].message.content

# 🔺 9. STRUCTURAL INTELLIGENCE (V4)
def detect_core_notes():
    print("🔍 Détection du noyau cognitif...")
    scores = {}
    for note in notes:
        # On compte le nombre de liens sortants comme indicateur de centralité
        link_count = note['content'].count("[[")
        scores[note['name']] = link_count
    
    core = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
    return core

def cluster_notes():
    print("📂 Clustering thématique...")
    clusters = {}
    keywords = ["système", "fractal", "chiastique", "mémoire", "académique", "discipline"]
    
    for note in notes:
        content_lower = note['content'].lower()
        for kw in keywords:
            if kw in content_lower:
                clusters.setdefault(kw, []).append(note['name'])
    
    return clusters

def update_dashboard():
    print("📊 Mise à jour du Dashboard...")
    core = detect_core_notes()
    clusters = cluster_notes()
    
    dashboard_content = f"""# 🔺 SYSTEM DASHBOARD
**Dernière mise à jour** : {os.popen('date /t').read().strip()} {os.popen('time /t').read().strip()}

## 🧠 Noyau Cognitif (Top Notes)
{chr(10).join([f"- {name} ({score} liens)" for name, score in core])}

## 📂 Clusters Thématiques
{chr(10).join([f"- **{kw.upper()}** : {', '.join(files[:3])}{'...' if len(files)>3 else ''}" for kw, files in clusters.items()])}

## 📈 Statistiques
- Total des notes : {len(notes)}
- Santé du système : {"Stricte" if len(notes) < 50 else "Expansion"}

## 💡 Opportunités
- Zones à renforcer : { "Démarrage" if len(clusters) < 3 else "Diversifier les thèmes" }
"""
    
    if not os.path.exists(SYSTEM_PATH):
        os.makedirs(SYSTEM_PATH)
        
    with open(os.path.join(SYSTEM_PATH, "dashboard.md"), "w", encoding="utf-8") as f:
        f.write(dashboard_content)
    print("Dashboard mis à jour.")

# 🔺 10. STRATEGIC THINK (V9 FINAL — MDL + Objectifs + User Model)
def strategic_think(situation):
    """Pipeline MDL : INTERPRET → PROJECT (α,β,κ) → CALCULATE μ → DIAGNOSTIC → DECISION"""
    import re as _re
    print("🔺 STRATEGIC ENGINE V9 FINAL...")
    
    context = search(situation)
    objectives = load_objectives()
    user_model = load_user_model()
    context_text = "\n---\n".join([
        n.get('content', str(n)) if isinstance(n, dict) else str(n)
        for n in context
    ])
    
    strat_prompt_path = os.path.join(SYSTEM_PATH, "strategic_prompt.txt")
    with open(strat_prompt_path, "r", encoding="utf-8") as f:
        strat_prompt = f.read()
    
    core_path = os.path.join(KNOWLEDGE_PATH, "MDL_YNOR_CORE.md")
    with open(core_path, "r", encoding="utf-8") as f:
        core_ref = f.read()
    
    full_prompt = strat_prompt + f"\n\n# OBJECTIFS SYSTÈME\n{objectives}\n\n# PROFIL UTILISATEUR\n{user_model}"
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": full_prompt},
            {"role": "user", "content": f"""
REFERENCE MDL_YNOR_CORE:
{core_ref}

CONTEXTE VECTORIEL:
{context_text}

SITUATION A ANALYSER:
{situation}
"""}
        ],
        temperature=0.3
    )
    
    analysis = response.choices[0].message.content
    
    # Extraction de mu
    match = _re.search(r'[μmu]\s*=\s*(-?[\d.]+)', analysis.lower().replace('μ', 'mu'))
    mu = float(match.group(1)) if match else 0.0
    
    print(f"🔺 mu = {mu}")
    if mu <= 0:
        print("🔴 INSTABLE — Action immédiate requise")
    elif mu <= 0.3:
        print("🟡 FRAGILE — Surveillance requise")
    else:
        print("🟢 STABLE et OPTIMAL")
    
    return analysis, mu

# 🔺 11. PROCESS CHAT (V6 — Dual Memory)
def process_chat(file):
    print(f"Traitement du chat : {file}")
    with open(os.path.join(CHAT_PATH, file), "r", encoding="utf-8") as f:
        text = f.read()

    result = think(text)
    passed, score = quality_filter(result, return_score=True)
    name = file.replace(".txt", "").replace(".log", "")

    if passed:
        create_note(result, name)
    else:
        save_to_learning(result, f"chat_{name}", score, "Score insuffisant")
        print(f"⚠️ Note '{file}' redirigée vers LEARNING (score={score}).")

# 🔺 12. RUN (V6 — avec mode learn)
def run(mode="full"):
    print("🚀 Démarrage du système SecondBrain V6 (Dual Memory + Learning)...")
    load_notes()
    build_index()

    if mode == "strategic":
        # Mode stratégique interactif
        situation = input("Situation à analyser : ")
        analysis, mu = strategic_think(situation)
        print("\n" + analysis)
        passed, score = quality_filter(analysis, return_score=True)
        name = f"DECISION_{np.random.randint(1000, 9999)}"
        tagged = analysis + f"\n\n---\n**Anchor** : [[MDL_YNOR_CORE]]\n**mu** : {mu}"
        if passed:
            create_note(tagged, name)
        else:
            save_to_learning(tagged, name, score, f"mu={mu} | Score={score}")
        update_dashboard()
        return

    if mode == "learn":
        # Mode apprentissage : analyse des échecs
        report = learn_from_failures()
        if report:
            print("\n" + report)
        update_dashboard()
        return

    # Mode complet standard
    if os.path.exists(CHAT_PATH):
        files = [f for f in os.listdir(CHAT_PATH) if f.endswith(".txt")]
        for file in files:
            process_chat(file)

    # Phase de réflexion autonome
    idea = auto_think()
    passed, score = quality_filter(idea, return_score=True)
    if passed:
        create_note(idea, f"auto_thought_{np.random.randint(1000, 9999)}")
    else:
        save_to_learning(idea, f"auto_thought_{np.random.randint(1000, 9999)}", score, "Auto-think rejeté")
        print("⚠️ Réflexion autonome redirigée vers LEARNING.")
    
    # Intelligence Structurelle
    update_dashboard()
    
    # Apprentissage automatique si assez de données
    learning_count = len([f for f in os.listdir(LEARNING_PATH) if f.endswith(".md")])
    if learning_count >= 3:
        print(f"📓 {learning_count} fichiers dans LEARNING — Lancement de l'analyse...")
        learn_from_failures()
    
    print("✅ Session V6 terminée.")

if __name__ == "__main__":
    try:
        import sys as _sys
        if len(_sys.argv) > 1 and _sys.argv[1] == "--strategic":
            run(mode="strategic")
        elif len(_sys.argv) > 1 and _sys.argv[1] == "--learn":
            run(mode="learn")
        else:
            run()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
