import json
import os

def execute_purge():
    with open('collapse_report.json', 'r') as f:
        data = json.load(f)
    
    duplicates = data['duplicate_list']
    purged_count = 0
    
    print(f"=== DÉBUT DE LA PURGE DE DENSIFICATION (V11.13.x) ===")
    
    for item in duplicates:
        path = os.path.normpath(item['duplicate'])
        try:
            if os.path.exists(path):
                os.remove(path)
                print(f"[PURGE] {path} -> EFFACÉ")
                purged_count += 1
        except Exception as e:
            print(f"[ERREUR] Impossible de supprimer {path}: {e}")
            
    print(f"\n=== PURGE TERMINÉE : {purged_count} DOUBLONS ÉLIMINÉS ===")
    return purged_count

if __name__ == "__main__":
    execute_purge()
