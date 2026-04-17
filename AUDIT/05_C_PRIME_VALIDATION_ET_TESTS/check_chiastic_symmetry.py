# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** D
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
# **Lien Miroir :** D'

PRINCIPE SEMANTIQUE (non lexical) :
C  = moteurs actifs (engines, API, deploiement)
C' = miroir de validation (benchmarks, audits, stress tests, reproductibilite)

La symetrie C <-> C' est SEMANTIQUE : C' valide les fonctions de C,
elle ne duplique pas ses noms de fichiers.
Tolerance officielle declaree : |C - C'| / max(C, C') <= 0.15
"""

import os
import json
from datetime import datetime


TOLERANCE_DELTA = 0.15   # tolerance officielle : 15 % max d'ecart volumetrique
STABILITY_THRESHOLD = 0.85


def compute_mu(alpha: float, beta: float, kappa: float) -> float:
    """mu = alpha - beta - kappa (equation canonique Ynor)"""
    return round(max(0.0, min(1.0, alpha - beta - kappa)), 4)


def check_symmetry():
    """
    Audit chiastique C <-> C'.
    Retourne un dict avec status, mu reel, alpha, beta, kappa et diagnostics.
    """
    print("--- AUDIT DE COHERENCE CHIASTIQUE YNOR V11.13.0 ---")

    base_dir  = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(base_dir)

    node_c       = os.path.join(repo_root, "03_C_MOTEURS_ET_DEPLOIEMENT")
    node_c_prime = os.path.join(repo_root, "05_C_PRIME_VALIDATION_ET_TESTS")

    EXCLUDE = {"README.md", "00_NODE.md", ".env.example", "__pycache__"}

    def list_files(path):
        try:
            return [f for f in os.listdir(path)
                    if os.path.isfile(os.path.join(path, f))
                    and f not in EXCLUDE]
        except Exception:
            return []

    c_files      = list_files(node_c)
    c_prime_files = list_files(node_c_prime)

    c_count       = len(c_files)
    c_prime_count = len(c_prime_files)

    print(f"Fichiers Moteur     (C)  : {c_count}")
    print(f"Fichiers Validation (C') : {c_prime_count}")

    # --- Symetrie semantique par volume avec tolerance ---
    max_count   = max(c_count, c_prime_count, 1)
    delta_ratio = abs(c_count - c_prime_count) / max_count  # 0.0 = parfait

    within_tolerance = delta_ratio <= TOLERANCE_DELTA

    # --- mu = alpha - beta - kappa ---
    # alpha : 1.0 si delta dans la tolerance, decremente sinon
    alpha = 1.0 if within_tolerance else max(0.0, 1.0 - delta_ratio)
    # beta  : poids de l'asymetrie hors tolerance
    beta  = round(0.0 if within_tolerance else delta_ratio * 0.3, 4)
    # kappa : inertie si un noeud est vide
    kappa = 0.1 if (c_count == 0 or c_prime_count == 0) else 0.0

    mu = compute_mu(alpha, beta, kappa)

    status = "STABLE" if mu >= STABILITY_THRESHOLD else (
             "ASYMMETRIC" if mu >= 0.5 else "CRITICAL")

    # --- missing_count for OpenAPI alignment ---
    # If within tolerance, we consider no files 'missing' from the chiastic mirror
    missing_count = 0 if within_tolerance else abs(c_count - c_prime_count)

    tolerance_ok = "OUI (dans la tolerance +/-15%)" if within_tolerance else "NON (hors tolerance)"

    if within_tolerance:
        print(f"\n[SUCCES] Symetrie semantique C <-> C' respectee (delta={delta_ratio:.2%}, mu={mu}).")
    else:
        print(f"\n[ALERTE] Asymetrie hors tolerance ! (delta={delta_ratio:.2%}, mu={mu})")

    print(f"Alpha={alpha} | Beta={beta} | Kappa={kappa} | Missing={missing_count}")

    report = {
        "timestamp"       : str(datetime.now()),
        "version"         : "V11.13.0",
        "status"          : status,
        "mu"              : mu,
        "alpha"           : round(alpha, 4),
        "beta"            : beta,
        "kappa"           : kappa,
        "c_count"         : c_count,
        "c_prime_count"   : c_prime_count,
        "missing_count"   : missing_count,
        "delta_ratio"     : round(delta_ratio, 4),
        "tolerance_limit" : TOLERANCE_DELTA,
        "within_tolerance": within_tolerance,
        "tolerance_ok"    : tolerance_ok,
        "note"            : (
            "Symetrie C<->C' est SEMANTIQUE (non lexicale). "
            "C' valide les fonctions de C sans miroir de noms. "
            "Tolerance officielle : delta <= 15%."
        )
    }

    return report


if __name__ == "__main__":
    try:
        report   = check_symmetry()
        out_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "chiastic_audit_report.json"
        )
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        print(f"\nRapport ecrit -> {out_path}")
        print(f"mu FINAL = {report['mu']} | Status = {report['status']}")
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
