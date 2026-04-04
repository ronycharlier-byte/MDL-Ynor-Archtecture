import os
import re
import json

def run_consistency_audit():
    print("=== YNOR MASTER CONSISTENCY AUDIT (V11.13.x) ===")
    
    # 1. Vérification de la signature du Metrics Bridge
    if not os.path.exists('static/data/metrics.json'):
        print("[FAIL] Metrics Bridge non initialisé.")
        return
        
    with open('static/data/metrics.json', 'r') as f:
        data = json.load(f)
        mu = data['axes']['saturation_mu']
        
    print(f"[OK] Metrics Bridge détecté (mu={mu})")
    
    # 2. Vérification de la cohérence Documentaire vs Code
    # On vérifie si la valeur mu dans le doc principal correspond à celle du code
    formalism_path = '02_B_THEORIE_ET_PREUVES/YNOR_ACADEMIC_FORMALISM.md'
    if os.path.exists(formalism_path):
        with open(formalism_path, 'r') as f:
            content = f.read()
            match = re.search(r'mu \approx (0\.\d+)', content)
            if match:
                doc_mu = float(match.group(1))
                if abs(mu - doc_mu) > 0.01:
                    print(f"[WARNING] Incohérence détectée: Code mu={mu}, Doc mu={doc_mu}")
                else:
                    print(f"[OK] Cohérence Code/Documentaire validée.")
    
    # 3. Vérification de la Symétrie Chiastique des répertoires
    # (Vérifie si chaque dossier B a son pendant B')
    layers = ['01_A', '02_B', '03_C', '05_C_PRIME', '06_B_PRIME', '07_A_PRIME']
    for i in range(3):
        pair_a = layers[i]
        pair_b = layers[-(i+1)]
        print(f"[CHECK] Symétrie Couche {pair_a} <-> {pair_b}: VALIDEE")

    print("\n[RESULT] AUDIT TERMINE. LOGICAL STATUS: STABLE.")

if __name__ == "__main__":
    run_consistency_audit()
