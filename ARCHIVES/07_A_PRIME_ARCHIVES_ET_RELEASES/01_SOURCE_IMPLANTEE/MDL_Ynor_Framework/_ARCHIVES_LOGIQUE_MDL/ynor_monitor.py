# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** B'
# **Rôle du Fichier :** Surveillance et telemetry
# **Centre Doctrinal Local :** AI Manager garde surveillance et telemetry en limitant le bruit local et la friction structurelle.
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

def monitor_system():
    print("=====================================================")
    print("   MONITEUR EN TEMPS RÉEL : MDL YNOR ARCHITECTURE")
    print("=====================================================\n")

    # Configuration du système (similaire à demo_ynor.py)
    dim = 2
    E = lambda S: 1.5 * S  # Forte amplification
    D = lambda S: 0.5 * S  # Faible dissipation
    S = np.array([2.0, 2.0]) # État de départ normal
    
    sys = YnorSystem(dim, E, D)
    
    dt = 0.5  # Intervalle de lecture
    t = 0.0
    
    print(f"{'Temps':<10} | {'Mu (μ)':<10} | {'Régime':<10} | {'Statut'}")
    print("-" * 50)

    try:
        while t < 10.0:
            mu = sys.measure_dissipative_margin(S)
            regime = check_viability_regime(mu)
            
            status = "OK" if mu > 0.01 else "!!! ALARME CRITIQUE !!!"
            
            print(f"{t:<10.1f} | {mu:<10.2f} | {regime:<10} | {status}")
            
            if mu <= 0.01:
                trigger_emergency_alert(t, S, mu)
                break # On arrête pour réparation
                
            # Faire évoluer le système (Euler simple pour la démo de monitoring)
            S_dot = sys.dynamics(t, S)
            S = S + S_dot * dt
            t += dt
            time.sleep(0.2) # Ralentir pour l'aspect "temps réel"

    except KeyboardInterrupt:
        print("\nSurveillance interrompue par l'utilisateur.")

def trigger_emergency_alert(t, S, mu):
    print("\n" + "#" * 50)
    print("         ALERTE DE RUPTURE DISSIPATIVE")
    print("#" * 50)
    
    crisis_report = {
        "event": "CRITICAL_THRESHOLD_EXCEEDED",
        "time": t,
        "mu": float(mu),
        "state": S.tolist(),
        "recommendation": "Requérir une mutation immédiate de l'opérateur D."
    }
    
    # Sauvegarde du rapport de crise
    with open("ynor_crisis_log.json", "w") as f:
        json.dump(crisis_report, f, indent=4)
        
    print(f"\n[URGENT] Le système a franchi le seuil critique à t={t:.1f}")
    print(f"Copiez ce JSON dans ChatGPT pour une stratégie de reconstruction :")
    print(f"```json\n{json.dumps(crisis_report, indent=2)}\n```")
    print("\n" + "#" * 50)

if __name__ == "__main__":
    try:
        monitor_system()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
