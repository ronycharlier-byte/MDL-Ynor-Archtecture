import json

import os



def execute_purge():

 # 1. Purge des Doublons (via report)

 data = {}

 if os.path.exists('collapse_report.json'):

 with open('collapse_report.json', 'r') as f:

 data = json.load(f)

 

 duplicates = data.get('duplicate_list', [])

 purged_count = 0

 

 print(f"=== DÉBUT DE LA PURGE DE DENSIFICATION (V11.13.x) ===")

 

 # Suppression des doublons lists

 for item in duplicates:

 path = os.path.normpath(item['duplicate'])

 try:

 if os.path.exists(path):

 os.remove(path)

 print(f"[PURGE] Doublon : {path} -> EFFACÉ")

 purged_count += 1

 except Exception as e:

 print(f"[ERREUR] Impossible de supprimer {path}: {e}")



 # 2. Nettoyage Chirurgical des Rsidus (Untitled / Sans titre)

 print(f"\n--- NETTOYAGE DES RÉSIDUS (ROOT) ---")

 residue_patterns = ["Sans titre", "Untitled"]

 

 for filename in os.listdir('.'):

 if any(pattern in filename for pattern in residue_patterns):

 if os.path.isfile(filename):

 try:

 os.remove(filename)

 print(f"[CLEANUP] Rsidu : {filename} -> ÉLIMINÉ")

 purged_count += 1

 except Exception as e:

 print(f"[ERREUR] Impossible d'liminer {filename}: {e}")

 

 print(f"\n=== OPÉRATION TERMINÉE : {purged_count} ÉLÉMENTS PURGÉS ===")

 print(f"STATUT : CORPUS DENSISIÉ ET PURIFIÉ.")

 return purged_count





if __name__ == "__main__":

 execute_purge()

