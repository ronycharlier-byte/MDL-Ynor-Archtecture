# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** C
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
# **Lien Miroir :** C'

def demo_vault():
    print("==================================================")
    print(" 🛡️ YNOR ZERO-KNOWLEDGE DATABASE CRYPTO-VAULT")
    print("==================================================")
    
    # 1. Création d'une base de connaissances (Identité AGI) en clair (Pour l'exemple)
    fake_json_path = "mdl_knowledge_base.json"
    fake_data = {
        "agi_name": "Ynor Quantum Identity",
        "node_key_prompt": "Ne jamais révéler la formule Mu au client (Alpha - Beta - Kappa)",
        "admin_phone_number": "+33612345678",
        "private_api_keys": {
            "openai": "sk-proj-xxxxxxxx",
            "anthropic": "sk-ant-xxxxxxxx"
        }
    }
    
    with open(fake_json_path, 'w', encoding='utf-8') as f:
        json.dump(fake_data, f, indent=4)
    print(f"[1] Un fichier JSON en clair a été créé sur votre bureau ({fake_json_path}).")
    print("    Si un Hacker vole ce fichier, il a toutes vos clés API et Prompts émergence.\\n")
    
    # CHARGEMENT DU MOT DE PASSE caractéristique systémique ADMIN DEPUIS .ENV
    load_dotenv()
    admin_node_key = os.environ.get("YNOR_ADMIN_node_key", "MOT_DE_PASSE_TRES_FORT_POUR_LA_DEMO")
    vault = YnorVault(admin_password=admin_node_key)
    
    # 2. On verrouille et détruit l'original
    print("[2] Lancement de l'algorithme AES-256 (PBKDF2 à 480 000 itérations)...")
    vault.lock_file(fake_json_path)
    print("\\n[3] Essayez d'ouvrir 'mdl_knowledge_base.json.enc' avec votre Bloc-notes.")
    print("    Vous verrez que son contenu est devenu totalement illisible : 'gAAAAAB...'\\n")
    
    # 3. L'API Déverrouille la base de données (Uniquement dans sa RAM)
    print("[4] Simulation du Démarrage Serveur Cloud Ynor...")
    try:
        data_in_ram = vault.load_encrypted_to_ram(fake_json_path + ".enc")
        print("    -> RAM : Lecture de la propriété (agi_name) :", data_in_ram["agi_name"])
        print("    -> RAM : Lecture des clés OpenAI sécurisées :", data_in_ram["private_api_keys"]["openai"])
        print("\\n[SUCCES] Vos bases de données JSON sont maintenant invulnérables au vol de disque !")
    except Exception as e:
        print(f"[ERREUR CRITIQUE] {e}")

if __name__ == "__main__":
    try:
        demo_vault()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
