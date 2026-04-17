# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
# **Rôle du Fichier :** Audit structurel et controle d'integrite
# **Centre Doctrinal Local :** AI Manager garde audit structurel et controle d'integrite en limitant le bruit local et la friction structurelle.
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

import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent.parent
AUDIT_ROOT = ROOT / "00_CORPUS_AUDIT"
IGNORE_DIRS = {".git", "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache"}
TEXT_EXTENSIONS = {
    ".md",
    ".json",
    ".txt",
    ".py",
    ".ps1",
    ".bat",
    ".sh",
    ".yml",
    ".yaml",
    ".toml",
    ".tex",
    ".html",
    ".cfg",
    ".ini",
    ".sample",
}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        yield path


def relpath(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace("\\", "/")


def file_category(path: Path) -> str:
    parts = [part.lower() for part in path.parts]
    joined = "/".join(parts)
    if "source_implantee" in joined:
        return "source_implantee"
    if "miroir_textuel" in joined:
        return "miroir_textuel"
    if "static_corpus" in joined:
        return "static_corpus"
    if "_releases" in joined or "releases" in joined:
        return "releases"
    if "_submissions" in joined or "submissions" in joined:
        return "submissions"
    if "_index" in joined or "/index" in joined:
        return "index"
    return "other"


def canonical_rank(path: Path) -> tuple:
    normalized = relpath(path).lower()
    return (
        0 if "source_implantee" in normalized else 1,
        0 if "static_corpus" in normalized else 1,
        0 if "miroir_textuel" not in normalized else 1,
        0 if "_cloud_exports" not in normalized else 1,
        0 if "_releases" not in normalized else 1,
        len(path.parts),
        normalized,
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scan_encoding_issues(path: Path) -> list[str]:
    if path.suffix.lower() not in TEXT_EXTENSIONS:
        return []
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["utf-8 decode failure"]

    issues = []
    if "\ufffd" in content:
        issues.append("replacement characters")
    for token in ("à", "â", "ê", "î", "ô", "û", "é", "è", "ç"):
        if token in content:
            issues.append(f"mojibake token {token!r}")
            break
    return issues


def build_audit() -> dict:
    files = list(iter_files(ROOT))
    category_counts = Counter()
    extension_counts = Counter()
    basename_groups = defaultdict(list)
    hash_groups = defaultdict(list)
    encoding_issues = []

    for path in files:
        category_counts[file_category(path)] += 1
        extension_counts[path.suffix.lower() or "[no_ext]"] += 1
        basename_groups[path.name].append(relpath(path))
        file_hash = sha256(path)
        hash_groups[file_hash].append(relpath(path))
        issues = scan_encoding_issues(path)
        if issues:
            encoding_issues.append(
                {
                    "path": relpath(path),
                    "issues": issues,
                }
            )

    duplicate_names = []
    for name, paths in sorted(basename_groups.items()):
        if len(paths) < 2:
            continue
        duplicate_names.append(
            {
                "name": name,
                "count": len(paths),
                "paths": sorted(paths, key=lambda value: value.lower()),
                "canonical_choice": min((ROOT / p for p in paths), key=canonical_rank).relative_to(ROOT).as_posix(),
            }
        )

    duplicate_hashes = []
    for digest, paths in sorted(hash_groups.items()):
        if len(paths) < 2:
            continue
        resolved = [ROOT / path for path in paths]
        duplicate_hashes.append(
            {
                "sha256": digest,
                "count": len(paths),
                "canonical_choice": min(resolved, key=canonical_rank).relative_to(ROOT).as_posix(),
                "paths": sorted(paths, key=lambda value: value.lower()),
            }
        )

    duplicate_hashes.sort(key=lambda item: (-item["count"], item["canonical_choice"].lower()))
    duplicate_names.sort(key=lambda item: (-item["count"], item["name"].lower()))

    return {
        "stage": "step_11_corpus_audit",
        "root": str(ROOT).replace("\\", "/"),
        "file_count": len(files),
        "category_counts": dict(category_counts),
        "extension_counts": dict(extension_counts.most_common()),
        "duplicate_name_groups": duplicate_names,
        "duplicate_hash_groups": duplicate_hashes,
        "duplicate_name_count": len(duplicate_names),
        "duplicate_hash_count": len(duplicate_hashes),
        "encoding_issue_count": len(encoding_issues),
        "encoding_issues": sorted(encoding_issues, key=lambda item: item["path"].lower()),
    }


def build_report(audit: dict) -> str:
    lines = [
        "# CORPUS AUDIT",
        "",
        "## Synthese",
        f"- Fichiers scannes : `{audit['file_count']}`",
        f"- Groupes de noms dupliques : `{audit['duplicate_name_count']}`",
        f"- Groupes de hash dupliques : `{audit['duplicate_hash_count']}`",
        f"- Fichiers avec souci d'encodage : `{audit['encoding_issue_count']}`",
        "",
        "## Repartition Par Zone",
    ]
    for category, count in sorted(audit["category_counts"].items()):
        lines.append(f"- {category} : `{count}`")

    lines.extend(["", "## Repartition Par Extension"])
    for extension, count in sorted(audit["extension_counts"].items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- {extension} : `{count}`")

    lines.extend(["", "## Doublons Par Nom"])
    for item in audit["duplicate_name_groups"][:60]:
        lines.append(f"- `{item['name']}` : `{item['count']}` copies")
        lines.append(f"  Canonique suggeree : `{item['canonical_choice']}`")
        lines.append(f"  Chemins : {', '.join(f'`{path}`' for path in item['paths'][:6])}")

    lines.extend(["", "## Doublons Par Contenu"])
    for item in audit["duplicate_hash_groups"][:60]:
        lines.append(f"- `{item['sha256'][:12]}` : `{item['count']}` copies")
        lines.append(f"  Canonique suggeree : `{item['canonical_choice']}`")
        lines.append(f"  Chemins : {', '.join(f'`{path}`' for path in item['paths'][:6])}")

    if audit["encoding_issues"]:
        lines.extend(["", "## Risques D'encodage"])
        for item in audit["encoding_issues"][:60]:
            lines.append(f"- `{item['path']}` : {', '.join(item['issues'])}")

    lines.extend(
        [
            "",
            "## Priorites",
            "1. Conserver une source canonique unique pour chaque groupe de hash duplique.",
            "2. Normaliser les noms de fichiers et les encodages des textes manifestement touches.",
            "3. Rejouer l'index apres nettoyage pour figer la version de reference.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    audit = build_audit()
    AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    (AUDIT_ROOT / "corpus_audit.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    (AUDIT_ROOT / "CORPUS_AUDIT.md").write_text(
        build_report(audit),
        encoding="utf-8",
    )


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
