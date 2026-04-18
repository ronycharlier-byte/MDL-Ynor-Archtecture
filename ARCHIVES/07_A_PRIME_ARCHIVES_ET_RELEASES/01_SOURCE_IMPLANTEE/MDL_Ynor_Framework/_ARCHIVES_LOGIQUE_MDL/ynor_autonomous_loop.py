# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** B'
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
# **Lien Miroir :** B

def autonomous_system_loop():
    print("=====================================================")
    print("   GOUVERNANCE AUTONOME MDL YNOR (COCKPIT IA)")
    print("=====================================================\n")

    # Système initial (Instable : E > D)
    dim = 2
    E = lambda S: 1.5 * S  # beta ≈ 1.5
    D = lambda S: 0.5 * S  # alpha ≈ 0.5
    S = np.array([2.0, 2.0])
    
    sys = YnorSystem(dim, E, D)
    
    t = 0.0
    dt = 0.5
    
    print(f"Lancement de la surveillance autonome sur 20 cycles...")
    print("-" * 60)

    for _ in range(20):
        mu = sys.measure_dissipative_margin(S)
        regime = check_viability_regime(mu)
        
        print(f"t={t:<4.1f} | mu={mu:<5.2f} | {regime:<10} | Etat={S}")
        
        # SI LE SYSTÈME ENTRE EN CRISE (mu <= 0)
        if mu <= 0.0:
            print("\n[CRISE DÉTECTÉE] ALARME ROUGE : µ = " + str(mu))
            
            # APPEL À L'AGENCE DE GOUVERNANCE IA (OpenAI)
            strategy = get_ai_reconstruction_strategy(mu, S.tolist())
            
            r = strategy["mutation_rate"]
            desc = strategy["explanation"]
            
            print(f"[MUTATION IA] Taux appliqué : +{r*100}%")
            print(f"[EXPLICATION] : {desc}")
            
            # APPLICATION DE LA MUTATION STRUCTURELLE
            old_D = sys.D
            # Nouveau D boosté par l'IA
            sys.D = lambda S, D_old=old_D, rate=r: (1.0 + rate) * D_old(S)
            
            print("[SYSTÈME RECONSTRUIT] Continuité de la simulation...\n")
            
        # Evolution
        S_dot = sys.dynamics(t, S)
        S = S + S_dot * dt
        t += dt
        time.sleep(0.3)

    print("\nSimulation Autonome terminée.")

if __name__ == "__main__":
    try:
        autonomous_system_loop()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
