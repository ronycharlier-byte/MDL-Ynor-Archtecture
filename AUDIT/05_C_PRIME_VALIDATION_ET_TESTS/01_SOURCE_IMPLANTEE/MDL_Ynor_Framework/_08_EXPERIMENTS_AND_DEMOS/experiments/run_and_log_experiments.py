# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** D
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
# **Lien Miroir :** D'

def run_experiment(seed=42):
    random.seed(seed)
    
    # Simulate a run
    config = {
        "alpha_weight": 0.2,
        "beta_weight": 0.05,
        "kappa_base": 0.01,
        "seed": seed
    }
    
    metrics = []
    mu_total = 1.0
    for step in range(1, 11):
        alpha = random.uniform(0.1, 0.5) * (1/step)
        beta = 0.05 + (0.01 * step)
        kappa = 0.01 * (step**1.1)
        mu = alpha - beta - kappa
        mu_total += mu
        
        metrics.append({
            "step": step,
            "alpha": round(alpha, 4),
            "beta": round(beta, 4),
            "kappa": round(kappa, 4),
            "mu": round(mu, 4)
        })
        
        if mu <= 0:
            break
            
    result = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "config": config,
        "metrics": metrics,
        "final_status": "SUCCESS" if mu_total > 0 else "COLLAPSE"
    }
    
    os.makedirs("experiments", exist_ok=True)
    filename = f"experiments/run_{seed}_{int(time.time())}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
    print(f"Experiment finished. Results saved to {filename}")

if __name__ == "__main__":
    try:
        for s in [42, 101, 2026]:
            run_experiment(s)
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
