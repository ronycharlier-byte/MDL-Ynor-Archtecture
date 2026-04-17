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

ROOT = Path(__file__).resolve().parent.parent.parent

IGNORE_DIRS = {".git", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache", "node_modules", ".obsidian", "_SYSTEM_AGI"}
TEXT_EXTENSIONS = {
    ".md", ".txt", ".tex", ".py", ".html", ".json", ".yaml", ".yml", ".ps1"
}

ACADEMIC_TERMS = ["hypothèse", "démonstration", "preuve", "référence", "bibliographie", "méthodologie", "théorème", "corollaire", "analyse", "empirique"]
MARKETING_TERMS = ["innovation majeure", "fortement optimisé", "strictement déterministe", "formellement démontré", "rendement", "propriété émergente"]

def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.name in ["evaluate_10_10.py", "fix_encoding_issues.py", "diagnose.py", "final_fix_10_10.py", "sanitize_scientific_10_10.py", "final_sanitization.py"]:
            continue
        yield path

def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except Exception:
        pass
    return digest.hexdigest()

def scan_text(path: Path):
    num_academic = 0
    num_marketing = 0
    issues = False
    
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return 0, 0, False

    try:
        content = path.read_text(encoding="utf-8").lower()
        
        for term in ACADEMIC_TERMS:
            num_academic += content.count(term)
        for term in MARKETING_TERMS:
            num_marketing += content.count(term)
        
        if "\ufffd" in content or "ã" in content or "â€" in content:
            issues = True
            
    except UnicodeDecodeError:
        issues = True
        
    return num_academic, num_marketing, issues

def main():
    files = list(iter_files(ROOT))
    total_files = len(files)
    
    hash_counts = Counter()
    total_academic = 0
    total_marketing = 0
    total_encoding_issues = 0
    
    for path in files:
        hash_val = sha256(path)
        hash_counts[hash_val] += 1
        
        ack, mkt, iss = scan_text(path)
        if mkt > 0:
            print(f"MARKETING TERMS IN: {path} ({mkt})")
        total_academic += ack
        total_marketing += mkt
        if iss:
            print(f"ISSUE: {path}")
            total_encoding_issues += 1

    duplicate_files = sum(count - 1 for count in hash_counts.values())
    # List duplicates
    if duplicate_files > 0:
        print("DUPLICATE FILES DETECTED:")
        for h, c in hash_counts.items():
            if c > 1:
                duplicate_paths = [str(p) for p in files if sha256(p) == h]
                print(f"Hash {h}: {duplicate_paths}")

    # Mathematical Variables (Hygiene & Deduplication)
    # 0 duplicates = 100%, 10% duplicates = 0%
    math_score = max(0, 10.0 - (duplicate_files / total_files * 10 * 10)) if total_files > 0 else 0
    math_score = min(10.0, math_score)
    math_score = round(math_score, 2)
    
    # Scientific Variables (Tone and Vocabulary)
    if total_academic + total_marketing == 0:
        sci_score = 5.0  # Neutral
    else:
        # Ideal: high academic, 0 marketing
        ratio = total_academic / (total_academic + total_marketing * 5)
        sci_score = min(10.0, ratio * 10)
    sci_score = round(sci_score, 2)
    
    # Academic Variables (Encoding and Formatting Integrity)
    # 0 issues = 10.0
    academic_score = max(0, 10.0 - (total_encoding_issues / total_files * 100)) if total_files > 0 else 0
    academic_score = min(10.0, academic_score)
    academic_score = round(academic_score, 2)
    
    # Final Calculation
    final_score = round((math_score + sci_score + academic_score) / 3, 2)
    
    result = {
        "total_files": total_files,
        "duplicate_files": duplicate_files,
        "total_encoding_issues": total_encoding_issues,
        "total_academic_terms": total_academic,
        "total_marketing_terms": total_marketing,
        "scores": {
            "mathematical_structural": math_score,
            "scientific_epistemological": sci_score,
            "academic_integrity": academic_score,
            "final_grade": final_score
        }
    }
    
    print(json.dumps(result, indent=4))

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
