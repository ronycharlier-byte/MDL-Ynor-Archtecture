import os

import hashlib

import json



def get_file_md5(path):

    hash_md5 = hashlib.md5()

    with open(path, "rb") as f:

        for chunk in iter(lambda: f.read(4096), b""):

            hash_md5.update(chunk)

    return hash_md5.hexdigest()



def find_identical_files():

    print("=== YNOR COLLAPSE MAXIMIZER (Audit de Doublons) ===")

    hashes = {}

    duplicates = []

    total_scanned = 0

    total_size = 0

    root_dir = '.'



    for root, dirs, files in os.walk(root_dir):

        if '.git' in dirs: dirs.remove('.git')

        for file in files:

            path = os.path.join(root, file)

            if file.endswith(('.md', '.py', '.html')):

                try:

                    f_hash = get_file_md5(path)

                    total_scanned += 1

                    total_size += os.path.getsize(path)

                    if f_hash in hashes:

                        duplicates.append({

                            "original": hashes[f_hash],

                            "duplicate": path,

                            "size": os.path.getsize(path)

                        })

                    else:

                        hashes[f_hash] = path

                except:

                    pass



    print(f"[1/2] Scan de {total_scanned} fichiers termin.")

    print(f"[2/2] {len(duplicates)} doublons exacts identifis.")



    # Rapport Final

    report = {

        "duplicates_found": len(duplicates),

        "potential_gain_files": len(duplicates),

        "potential_gain_kb": sum(d['size'] for d in duplicates) / 1024,

        "duplicate_list": duplicates[:20] # Limiter pour l'affichage

    }

    

    with open('collapse_report.json', 'w') as f:

        json.dump(report, f, indent=4)

        

    return report



if __name__ == "__main__":

    report_data = find_identical_files()

    ts = 689 # Valeur obtenue au scan prcdent

    dups = report_data['duplicates_found']

    print(f"\n[RÉSULTAT] Gain Potentiel : Supprimer {dups} fichiers.")

    print(f"[RÉSULTAT] Nouveau Taux CollapsEstim: {((dups / ts) * 100):.2f}% de Gain Immdiat.")

