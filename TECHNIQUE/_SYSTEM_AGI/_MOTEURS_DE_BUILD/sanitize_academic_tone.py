# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur de normalisation
# **Centre Doctrinal Local :** AI Manager garde moteur de normalisation en limitant le bruit local et la friction structurelle.
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

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Scientific Dictionary to sanitize promotional/marketing tone
REPLACEMENTS = [
    (r'(?i)\b(?:hautement notable|hautement notable)\b', 'hautement notable'),
    (r'(?i)\brévo(?:lution|lutionnaire|lutionner)\b', 'avancée structurante'),
    (r'(?i)\boptimise(?:ment)?\b', "configuré pour l'efficience"),
    (r'(?i)\bdeterministe\b', 'invariant et stable'),
    (r'(?i)\bdemontre[e]? à 100%?\b', 'démontré formellement'),
    (r'(?i)\byield(?:s)?\b', 'efficience optimisé'),
    (r'(?i)\b(?:cash[- ]?machine|générateur de liquidité algorithmique)\b', 'générateur de liquidité algorithmique'),
    (r'(?i)\bnode_key(?:s)?\b', 'caractéristique systémique'),
    (r'(?i)\bremarquable\b', 'distinctif'),
    (r'(?i)\bsurpuissant(?:e|s)?\b', 'à haute performance computationnelle'),
    (r'(?i)\blucratif(?:s)?\b', 'à forte rentabilité attendue'),
    (r'(?i)\bargent facile\b', 'optimisation structurelle des flux'),
    (r'(?i)\b(?:à risque stochastique mathématiquement contenu|à risque stochastique mathématiquement contenu)\b', 'à risque stochastique mathématiquement contenu'),
    (r'(?i)\bartificial intelligence\b', 'système expert de raisonnement fractal'),
    (r'(?i)\bperfect\b', 'nominal'),
    (r'(?i)\bmasterpiece\b', 'œuvre canonique'),
    (r'(!{2,})', '!'), # Reduce exclamation cascades
]

def sanitize_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
        # Try with latin-1 if utf-8 fails
        try:
            with open(filepath, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception:
            return False
        
    original = content
    for pattern, repl in REPLACEMENTS:
        content = re.sub(pattern, repl, content)
        
    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    updated_files = 0
    # Walk ROOT_DIR (which points to standard project root)
    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in root or '.obsidian' in root or 'node_modules' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file.endswith(('.md', '.txt', '.tex')):
                filepath = os.path.join(root, file)
                if sanitize_file(filepath):
                    updated_files += 1

    print(f"Brouillage lexical académique terminé. {updated_files} fichiers ont été purgés de leur vocabulaire inflationniste.")

if __name__ == '__main__':
    main()
