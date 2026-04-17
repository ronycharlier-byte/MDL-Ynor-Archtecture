# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Moteur de generation
# **Centre Doctrinal Local :** AI Manager garde moteur de generation en limitant le bruit local et la friction structurelle.
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

ROOT_DIR = r"c:\Users\ronyc\Desktop\MDL Ynor"
TARGET_DIRS = ["00_", "01_", "02_", "03_", "04_", "05_", "06_", "07_", "08_", "_SYSTEM_AGI"]
OUTPUT_FILE = os.path.join(ROOT_DIR, "00_CORPUS_AUDIT", "SHA256_CANONICAL_MANIFEST.md")

def sha256_file(filepath):
    sha = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha.update(chunk)
        return sha.hexdigest()
    except Exception:
        return "<ERROR_READING_FILE>"

def main():
    if not os.path.exists(os.path.dirname(OUTPUT_FILE)):
        os.makedirs(os.path.dirname(OUTPUT_FILE))

    manifest_lines = [
        "# 🛡️ MANIFESTE CRYPTOGRAPHIQUE CANONIQUE (SHA-256)",
        f"**Date de génération :** {datetime.now().astimezone().isoformat()}",
        "**Objectif :** Ancrage temporel du Corpus Chiaste (Phase III)",
        "**Niveau SOUVERAIN (L0)**",
        "\n| Fichier | Empreinte CPH-SHA256 |",
        "| :--- | :--- |"
    ]

    count = 0
    # Walk chronologically
    for root, dirs, files in os.walk(ROOT_DIR):
        is_target = any(d in root.replace(ROOT_DIR, '') for d in TARGET_DIRS)
        if root == ROOT_DIR or is_target:
            # Exclude git or pycache
            if '.git' in root or '__pycache__' in root or '.obsidian' in root:
                continue

            for file in sorted(files):
                filepath = os.path.join(root, file)
                # Ignore this very file we are writing if it exists
                if filepath == OUTPUT_FILE:
                    continue
                # calculate relative path for clean display
                rel_path = os.path.relpath(filepath, ROOT_DIR).replace("\\", "/")
                file_hash = sha256_file(filepath)
                manifest_lines.append(f"| `{rel_path}` | `{file_hash}` |")
                count += 1
    
    # footer
    manifest_lines.append(f"\n---")
    manifest_lines.append(f"**Total des éléments scellés :** {count}")
    manifest_lines.append(f"**Certificat d'Intégrité :** SCIENTIFIC-READY v3.0.0")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(manifest_lines))
    
    print(f"Manifest genere avec succes: {count} fichiers scelles dans {OUTPUT_FILE}")

if __name__ == "__main__":
    try:
        main()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
