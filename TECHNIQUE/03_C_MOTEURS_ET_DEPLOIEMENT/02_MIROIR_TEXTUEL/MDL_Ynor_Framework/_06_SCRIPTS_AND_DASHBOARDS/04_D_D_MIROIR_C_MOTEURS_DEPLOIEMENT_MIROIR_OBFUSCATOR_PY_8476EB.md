> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D
> **Role du Fichier :** Surface miroir et symetrie locale
> **Centre Doctrinal Local :** boucle locale de reflet et de coherence
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence reflexive et effet miroir
> - **β :** derive de boucle et bruit de reflet
> - **κ :** cout de cycle et de stabilisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
# MIROIR TEXTUEL - secure_upload_obfuscator.py

Source : MDL_Ynor_Framework\_06_SCRIPTS_AND_DASHBOARDS\secure_upload_obfuscator.py
Taille : 3232 octets
SHA256 : 4bf11385459116dae24700c9032b68c25ae9db6e3a40940ffa6fb2f034448781

```text
import os
import json
import re
import shutil
import uuid

# =====================================================================
# 🛡️ MDL YNOR - SECURE UPLOAD OBFUSCATOR v1.0
# Ce script prépare votre dossier d'upload pour le GPT Store en :
# 1. Masquant les informations personnelles (emails, chemins)
# 2. Renommant les fichiers avec des noms aléatoires
# 3. Créant une archive propre pour l'upload final
# =====================================================================

SOURCE_DIR = r"C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\MDL_YNOR_GPT_UPLOAD_V3"
OUTPUT_DIR = r"C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\MDL_YNOR_GPT_FINAL_DIST"
MAPPING_LOG = os.path.join(04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_OBFUSCATOR_PY_8476EB.md")

# Regex de détection
EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@mdlstrategy\.[a-zA-Z0-9.-]+" # Cible spécifique MDL
PATH_REGEX = r"C:\\Users\\[a-zA-Z0-9 ]+\\[a-zA-Z0-9 ]+" # Vise les chemins Windows locaux

def redact_content(content):
 # Remplacer les emails
 content = re.sub(EMAIL_REGEX, "[REDACTED_AUTHOR_EMAIL]", content)
 # Remplacer les chemins Windows
 content = re.sub(PATH_REGEX, "[REDACTED_LOCAL_PATH]", content)
 # Autres remplacements de sécurité (codes sha, etc.)
 content = re.sub(r"[a-f0-9]{32,64}", "[REDACTED_SECURE_TOKEN]", content)
 return content

def obfuscate_and_clean():
 if os.path.exists(OUTPUT_DIR):
 shutil.rmtree(OUTPUT_DIR)
 os.makedirs(OUTPUT_DIR)

 mapping = {}
 print(f" Initialisation du moteur d'obfuscation Ynor...")

 for filename in os.listdir(SOURCE_DIR):
 src_path = os.path.join(SOURCE_DIR, filename)
 if os.path.isdir(src_path):
 continue

 # Générer un nouveau nom (UUID + extension originale ou .bin)
 name, ext = os.path.splitext(filename)
 new_id = str(uuid.uuid4())[:8]
 new_filename = f"ynor_node_{new_id}{ext}"
 
 # Pour les JSON, on peut forcer l'obfuscation même de l'extension
04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_CF_PS1_FBE668.md":
 new_filename = f"ynor_logic_{new_id}.bin"

 dest_path = os.path.join(OUTPUT_DIR, new_filename)
 mapping[new_filename] = filename

 print(f" [*] Traitement : {filename} -> {new_filename}...")

 try:
 with open(src_path, 'r', encoding='utf-8', errors='ignore') as f:
 content = f.read()
 
 # Nettoyage
 clean_content = redact_content(content)

 with open(dest_path, 'w', encoding='utf-8') as f:
 f.write(clean_content)
 except Exception as e:
 print(f" [⚠️] Erreur sur {filename}: {str(e)}")
 # Copie brute si échec de lecture texte (pdf, etc.)
 shutil.copy2(src_path, dest_path)

 # Sauvegarder le mapping pour le créateur
 with open(MAPPING_LOG, 'w', encoding='utf-8') as f:
 json.dump(mapping, f, indent=4)

 print(f"\n✅ OPÉRATION TERMINÉE.")
 print(f"Dossier final : {OUTPUT_DIR}")
 print(f"⚠️ NE JAMAIS UPLOADER LE FICHIER : {os.path.basename(MAPPING_LOG)}")
 print(f"Compressez le reste du dossier pour votre GPT Store.")

if __name__ == "__main__":
 obfuscate_and_clean()

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
