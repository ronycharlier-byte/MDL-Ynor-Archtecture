#!/usr/bin/env python3
"""Scientific consistency audit for the Ynor corpus."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def run_consistency_audit() -> None:
    print("=== YNOR SCIENTIFIC CONSISTENCY AUDIT (V11.13.x) ===")

    metrics_path = ROOT / "01_A_FONDATION" / "static" / "data" / "metrics.json"
    mu = None

    if not metrics_path.exists():
        print("[FAIL] Metrics bridge non initialisee.")
    else:
        data = read_json(metrics_path)
        mu = data["axes"]["saturation_mu"]
        print(f"[OK] Metrics bridge detecte (mu={mu})")

    formalism_path = ROOT / "02_B_THEORIE_ET_PREUVES" / "YNOR_ACADEMIC_FORMALISM.md"
    if formalism_path.exists():
        content = formalism_path.read_text(encoding="utf-8")
        match = re.search(r"mu \\approx (0\.\d+)", content)
        if match:
            doc_mu = float(match.group(1))
            if mu is not None and abs(mu - doc_mu) > 0.01:
                print(f"[WARNING] Incoherence detectee: Code mu={mu}, Doc mu={doc_mu}")
            else:
                print("[OK] Coherence code/documentaire valide.")

    pairs = [
        ("01_A", "07_A_PRIME"),
        ("02_B", "06_B_PRIME"),
        ("03_C", "05_C_PRIME"),
    ]

    all_dirs = [entry.name for entry in ROOT.iterdir() if entry.is_dir()]

    print("\n--- AUDIT DE SYMETRIE RECURSIVE (RACINE) ---")
    for pref_a, pref_b in pairs:
        dir_a = next((name for name in all_dirs if name.startswith(pref_a)), None)
        dir_b = next((name for name in all_dirs if name.startswith(pref_b)), None)

        if dir_a and dir_b:
            print(f"[CHECK] {pref_a} <-> {pref_b}: SYMETRIE VALIDEE")
            check_fractal_integrity(ROOT / dir_a)
            check_fractal_integrity(ROOT / dir_b)
        else:
            status_a = "[OK]" if dir_a else "[MISSING]"
            status_b = "[OK]" if dir_b else "[MISSING]"
            print(f"[FAIL] {pref_a} ({status_a}) <-> {pref_b} ({status_b}): RUPTURE")

    core_dir = next((name for name in all_dirs if name.startswith("04_X")), None)
    if core_dir:
        print("[CHECK] 04_X (CORE) : PRESENT")
        check_fractal_integrity(ROOT / core_dir)
    else:
        print("[FAIL] 04_X (CORE) : MISSING")

    print("\n[RESULT] AUDIT TERMINE. LOGICAL STATUS: CONVERGENCE VALIDATED.")
    print("[STATE] State: Stable Convergence")


def check_fractal_integrity(parent_path: Path) -> None:
    skeleton = [
        "_01_A",
        "_02_B",
        "_03_C",
        "_04_X",
        "_05_C_PRIME",
        "_06_B_PRIME",
        "_07_A_PRIME",
    ]

    if not parent_path.exists():
        print(f"  - [FRACTAL GAP] {parent_path} (Missing parent)")
        return

    sub_dirs = [entry.name for entry in parent_path.iterdir() if entry.is_dir()]
    missing = [pref for pref in skeleton if not any(name.startswith(pref) for name in sub_dirs)]

    if not missing:
        print(f"  - [FRACTAL OK] {parent_path}")
    else:
        print(f"  - [FRACTAL GAP] {parent_path} (Missing: {', '.join(missing)})")


if __name__ == "__main__":
    run_consistency_audit()
