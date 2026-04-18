# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** B'
# **Rôle du Fichier :** Audit structurel et controle d'integrite
# **Centre Doctrinal Local :** AI Manager garde audit structurel et controle d'integrite en limitant le bruit local et la friction structurelle.
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
# **Lien Miroir :** B

def run_audit_export():
    # 1. Configuration actuelle du système (extraite de demo_ynor.py)
    dim = 2
    E = lambda S: 1.5 * S  # Amplification (beta)
    D = lambda S: 0.5 * S  # Dissipation (alpha)
    S0 = np.array([2.0, 2.0]) # État actuel
    
    sys = YnorSystem(dim, E, D)
    mu = sys.measure_dissipative_margin(S0)
    
    # 2. Décomposition des facteurs (alpha, beta, kappa)
    s_norm_sq = np.sum(S0**2)
    alpha = np.dot(S0, D(S0)) / s_norm_sq
    beta = np.dot(S0, E(S0)) / s_norm_sq
    kappa = 0.0 # Par défaut dans la démo
    
    regime = check_viability_regime(mu)
    
    # 3. Création du Snapshot JSON
    audit_data = {
        "architecture": "MDL Ynor",
        "timestamp": datetime.datetime.now().isoformat(),
        "state": {
            "S": S0.tolist(),
            "dimension": dim
        },
        "coefficients": {
            "alpha": float(alpha),
            "beta": float(beta),
            "kappa": float(kappa)
        },
        "result": {
            "mu": float(mu),
            "regime": regime
        }
    }
    
    # Sauvegarde dans un fichier
    output_file = "ynor_audit_snapshot.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(audit_data, f, indent=4)
        
    # 4. Affichage du Prompt à copier pour ChatGPT
    print("\n" + "="*50)
    print("   YNOR AUDIT REPORT (POUR CHATGPT)")
    print("="*50)
    print("\n--- COPIEZ LE TEXTE CI-DESSOUS DANS CHATGPT ---\n")
    print(f"Bonjour ChatGPT, voici le snapshot d'audit MDL Ynor à analyser :")
    print(f"```json\n{json.dumps(audit_data, indent=2)}\n```")
    print("\nPeux-tu me confirmer si ce système est stable et quelles sont tes recommandations pour restaurer la viabilité (mu > 0) ?")
    print("\n" + "="*50)
    print(f"\n[OK] Fichier d'audit sauvegardé sous : {output_file}")

if __name__ == "__main__":
    try:
        run_audit_export()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
