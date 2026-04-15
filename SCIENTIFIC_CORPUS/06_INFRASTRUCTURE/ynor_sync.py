import subprocess
import os
import sys

# Constants for the AI Manager Identity
VERSION_TARGET = "v2.0.0-DS"
REPO_URL = "https://github.com/ronycharlier-byte/MDL-Ynor-Archtecture" # Verified URL

def run_sync():
    print(f"--- MDL YNOR AI-MANAGER SYNC (Target: {VERSION_TARGET}) ---")
    
    # 1. Pull Latest from GitHub
    try:
        print("Syncing with GitHub...")
        subprocess.run(["git", "pull", "origin", "main", "--tags"], check=True)
        print("Successfully synchronized local state.")
    except Exception as e:
        print(f"Sync failed or no internet: {e}")

    # 2. Integrity Audit (mu check)
    print("\nAuditing Algorithm Layer (03_ALGORITHMS)...")
    algorithms_dir = r"c:\Users\ronyc\Desktop\MDL Ynor\SCIENTIFIC_CORPUS\03_ALGORITHMS"
    files_to_check = ["DISSIPATIVE_ENGINE.py", "YNOR_NS_TURBULENCE_ULTIMATE.py"]
    
    for filename in files_to_check:
        path = os.path.join(algorithms_dir, filename)
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                if "mu =" in content or "mu >" in content:
                    print(f"  [PASS] {filename}: Dissipative logic detected.")
                else:
                    print(f"  [WARN] {filename}: Potential loss of mu-margin logic!")
        else:
            print(f"  [FAIL] {filename}: File missing!")

    print("\n--- SYNC COMPLETE ---")

if __name__ == "__main__":
    run_sync()
