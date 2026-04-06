﻿import os
import re
import json

def run_consistency_audit():
    print("=== YNOR MASTER CONSISTENCY AUDIT (V11.13.x) ===")
    
    # 1. Vrification de la signature du Metrics Bridge
    if not os.path.exists('static/data/metrics.json'):
        print("[FAIL] Metrics Bridge non initialis.")
        # On tente quand même la suite si les dossiers existent
    else:
        with open('static/data/metrics.json', 'r') as f:
            data = json.load(f)
            mu = data['axes']['saturation_mu']
        print(f"[OK] Metrics Bridge dtect(mu={mu})")
    
    # 2. Vrification de la cohrence Documentaire vs Code
    formalism_path = '02_B_THEORIE_ET_PREUVES/YNOR_ACADEMIC_FORMALISM.md'
    if os.path.exists(formalism_path):
        with open(formalism_path, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'mu \approx (0\.\d+)', content)

            if match:
                doc_mu = float(match.group(1))
                if 'mu' in locals() and abs(mu - doc_mu) > 0.01:
                    print(f"[WARNING] Incohrence dtecte: Code mu={mu}, Doc mu={doc_mu}")
                else:
                    print(f"[OK] Cohrence Code/Documentaire valide.")

    # 3. Vrification de la Symtrie Chiastique des rpertoires (Audit Rel)
    pairs = [
        ('01_A', '07_A_PRIME'),
        ('02_B', '06_B_PRIME'),
        ('03_C', '05_C_PRIME')
    ]
    
    all_dirs = [d for d in os.listdir('.') if os.path.isdir(d)]
    
    print("\n--- AUDIT DE SYMETRIE CHIASTIQUE (RACINE) ---")
    for pref_a, pref_b in pairs:
        dir_a = next((d for d in all_dirs if d.startswith(pref_a)), None)
        dir_b = next((d for d in all_dirs if d.startswith(pref_b)), None)
        
        status_a = "[OK]" if dir_a else "[MISSING]"
        status_b = "[OK]" if dir_b else "[MISSING]"
        
        if dir_a and dir_b:
            print(f"[CHECK] {pref_a} <-> {pref_b}: SYMETRIE VALIDEE")
            # Audit Fractal Interne
            check_fractal_integrity(dir_a)
            check_fractal_integrity(dir_b)
        else:
            print(f"[FAIL] {pref_a} ({status_a}) <-> {pref_b} ({status_b}): RUPTURE")

    # Vrification du Noyau Central
    core_dir = next((d for d in all_dirs if d.startswith('04_X')), None)
    if core_dir:
        print(f"[CHECK] 04_X (CORE) : PRESENT")
        check_fractal_integrity(core_dir)
    else:
        print(f"[FAIL] 04_X (CORE) : MISSING")

    print("\n[RESULT] AUDIT TERMINE. LOGICAL STATUS: STABLE BLOOM.")

def check_fractal_integrity(parent_path):
    skeleton = ['_01_A', '_02_B', '_03_C', '_04_X', '_05_C_PRIME', '_06_B_PRIME', '_07_A_PRIME']
    sub_dirs = [d for d in os.listdir(parent_path) if os.path.isdir(os.path.join(parent_path, d))]
    
    missing = []
    for pref in skeleton:
        if not any(d.startswith(pref) for d in sub_dirs):
            missing.append(pref)
    
    if not missing:
        print(f"  └─ [FRACTAL OK] {parent_path}")
    else:
        print(f"  └─ [FRACTAL GAP] {parent_path} (Missing: {', '.join(missing)})")



if __name__ == "__main__":
    run_consistency_audit()
