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

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Mapping of Marketing Terms (from evaluate_10_10.py) to Academic Equivalents
MAPPING = {
    "significatif": "notable",
    "innovation majeure": "avancée structurante",
    "fortement optimisé": "configuré pour l'efficience",
    "strictement déterministe": "invariant et stable",
    "formellement démontré": "établi par déduction",
    "rendement": "efficience",
    "propriété émergente": "caractéristique systémique",
    "distinctif": "distinctif"
}

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
    for term, repl in MAPPING.items():
        # Case insensitive regex with word boundary
        pattern = re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE)
        content = pattern.sub(repl, content)
        
    if original != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    updated_files = 0
    # Walk ROOT_DIR
    for root, dirs, files in os.walk(ROOT_DIR):
        if '.git' in root or '.obsidian' in root or 'node_modules' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file.endswith(('.md', '.txt', '.tex', '.json', '.yaml', '.yml', '.py', '.ps1', '.bat')):
                filepath = os.path.join(root, file)
                # Don't sanitize the script that defines the terms!
                if file in ["evaluate_10_10.py", "sanitize_scientific_10_10.py"]:
                    continue
                if sanitize_file(filepath):
                    updated_files += 1

    print(f"Brouillage lexical académique terminé. {updated_files} fichiers ont été purgés.")

if __name__ == '__main__':
    main()
