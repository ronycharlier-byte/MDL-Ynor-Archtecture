# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
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

# ==============================================================================
# YNOR SYSTEM HARDENER - PERSISTENCE INJECTION
# Automatically wraps all scripts in a safety net for Windows terminal sessions.
# ==============================================================================

def harden_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Si le fichier est déjà blindé, on passe
    if "ERREUR CRITIQUE DETECTEE" in content:
        return False

    # Regex pour trouver le bloc main
    # On cherche 'if __name__ == "__main__":' et tout ce qui suit
    main_pattern = r'if __name__ == "__main__":(.*)'
    match = re.search(main_pattern, content, re.DOTALL)
    
    if not match:
        return False

    old_main_content = match.group(1).strip()
    # On indente l'ancien contenu pour le bloc try
    indented_content = "    " + old_main_content.replace("\n", "\n    ")
    
    new_main = f"""if __name__ == "__main__":
    try:
    {indented_content}
        print("\\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {{e}}")
        print("!"*50)
        input("\\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
"""
    
    new_content = content[:match.start()] + new_main
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

if __name__ == "__main__":
    root_dir = os.getcwd()
    print(f"Hardening all scripts in {root_dir}...")
    
    count = 0
    for root, dirs, files in os.walk(root_dir):
        # On ignore les dossiers de dépendances ou git
        if any(x in root for x in [".git", "__pycache__", "venv", ".obsidian"]):
            continue
            
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                if harden_file(path):
                    print(f"[SHIELDED] {file}")
                    count += 1
    
    print(f"\nTerminé. {count} scripts ont été sécurisés.")
    input("Appuyez sur ENTRÉE pour quitter le Hardener.")
