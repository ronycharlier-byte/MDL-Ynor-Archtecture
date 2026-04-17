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
# MIROIR TEXTUEL - full_update_knowledge.py

Source : MDL_Ynor_Framework\_03_CORE_AGI_ENGINES\MDL_YNOR_GPT_KNOWLEDGE\full_update_knowledge.py
Taille : 5602 octets
SHA256 : dce8cb965301f43f3173066fd9e5434dd10e5059771c152ef9092b66a29f5123

```text
import os
import json
import hashlib

FRAMEWORK_DIR = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework"
JSON_FILE = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_03_CORE_AGI_ENGINES\MDL_YNOR_GPT_KNOWLEDGE\mdl_global_knowledge.json"

def estimate_tokens(text):
 return len(text) // 4

def get_file_hash(filepath):
 try:
 with open(filepath, "rb") as f:
04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md5(f.read()).hexdigest()
 except Exception:
 return ""

def update_json():
 current_meta = {
 "version": "2.2.0-PROD",
 "description": "Auto-Generated Knowledge Base with Geomagnetism and WMM Integration",
 "last_updated": "2026-03-24",
 "security_protocols": {} 
 }

 if os.path.exists(JSON_FILE) and os.path.getsize(JSON_FILE) > 0:
 with open(JSON_FILE, "r", encoding="utf-8") as f:
 data = json.load(f)
 # Update existing meta while preserving security protocols
 existing_meta = data.get("system_meta", {})
 current_meta["security_protocols"] = existing_meta.get("security_protocols", {})
 data["system_meta"] = current_meta
 else:
 data = {
 "system_meta": current_meta,
 "knowledge_nodes": []
 }

 # Use filepath + filename as unique identifier for nodes
 # If the JSON doesn't have it, we might need to map by file/folder
 # Map existing nodes by (folder, file) and determine the next ID
 existing_nodes = {}
 max_id_num = -1
 for node in data.get("knowledge_nodes", []):
 key = (node.get("folder"), node.get("file"))
 existing_nodes[key] = node
 # Extract numeric part of id (e.g., node_fw_042 -> 42)
 try:
 id_num = int(node.get("id", "node_fw_0").split("_")[-1])
 if id_num > max_id_num:
 max_id_num = id_num
 except (ValueError, IndexError):
 pass

 next_id_num = max_id_num + 1
 new_count = 0
 updated_count = 0
 seen_keys = set()

 print(f"Scanning {FRAMEWORK_DIR} for sources...")
 
 # Extensions to include
 include_exts = [04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md"]
 # Files to ignore
 exclude_files = [04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_KNOWLEDGE_PY_8629E7.md04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md", ".env"]
 # Directories to ignore
 exclude_dirs = ["__pycache__", ".git", "node_modules", ".gemini", "logs", "_ARCHIVES_LOGIQUE_MDL"]

 for root, dirs, files in os.walk(FRAMEWORK_DIR):
 # Filter directories
 dirs[:] = [d for d in dirs if d not in exclude_dirs]
 
 rel_folder = os.path.relpath(root, FRAMEWORK_DIR)
 if rel_folder == ".":
 rel_folder = "Root"

 for file in files:
 ext = os.path.splitext(file)[1].lower()
 if ext not in include_exts:
 continue
 if file in exclude_files:
 continue

 filepath = os.path.join(root, file)
 key = (rel_folder, file)
 seen_keys.add(key)
 
 file_hash = get_file_hash(filepath)

 try:
 # If node exists and hash matches, skip expensive reading
 if key in existing_nodes and existing_nodes[key].get("hash") == file_hash:
 continue

 with open(filepath, "r", encoding="utf-8", errors="ignore") as f_in:
 content = f_in.read().strip()
 except Exception:
 continue

 if not content:
 continue

 preview = content[:2000]
 token_cost = estimate_tokens(content)
 
 # Determine node type
 if ext in [".py", ".bat", ".ps1"]:
 node_type = "FRAMEWORK_CODE"
 elif ext in [04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md"]:
 node_type = "DOCUMENTATION"
04_D_D_MIROIR_C_MOTEURS_DEPLOIEMENT_MIROIR_API_PY_063868.md":
 node_type = "DATA_STRUCTURE"
 else:
 node_type = "ASSET"

 if key in existing_nodes:
 node = existing_nodes[key]
 node["preview"] = preview
 node["token_cost"] = token_cost
 node["type"] = node_type
 node["folder"] = rel_folder
 node["hash"] = file_hash
 updated_count += 1
 else:
 node = {
 "id": f"node_fw_{next_id_num:03d}",
 "file": file,
 "folder": rel_folder,
 "type": node_type,
 "priority": 1,
 "token_cost": token_cost,
 "mu_impact": "positive",
 "preview": preview,
 "hash": file_hash
 }
 data["knowledge_nodes"].append(node)
 next_id_num += 1
 new_count += 1

 # Cleanup deleted files
 initial_count = len(data["knowledge_nodes"])
 data["knowledge_nodes"] = [n for n in data["knowledge_nodes"] if (n.get("folder"), n.get("file")) in seen_keys or (n.get("folder"), n.get("file")) == (None, None)]
 removed_count = initial_count - len(data["knowledge_nodes"])

 with open(JSON_FILE, "w", encoding="utf-8") as f:
 json.dump(data, f, ensure_ascii=False, indent=2)
 
 print(f"Summary: Added {new_count} new sources, updated {updated_count} existing sources, removed {removed_count} stale entries.")
 print(f"Knowledge base now contains {len(data['knowledge_nodes'])} nodes.")

if __name__ == "__main__":
 update_json()

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
