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

class ParadoxicalGovernor:
    """
    Couche de Métacognition MDL Ynor forcée au paradoxe.
    """
    def __init__(self):
        self.intervention_history = []
        self.last_mutation_time = -1.0
        self.first_intervention_done = False

    def evaluate_intervention(self, current_t, current_mu):
        # Si moins de 1.0 unite de temps s'est ecoulee et que mu est toujours <= 0
        if self.last_mutation_time >= 0 and (current_t - self.last_mutation_time) <= 1.5:
            if current_mu <= 0.0:
                return True
        return False

    def critical_reflection(self, mu, state, history):
        print("\n[METACOGNITION] !!! ÉCHEC DE L'IA DÉTECTÉ !!!")
        print("[METACOGNITION] Procédure de réflexion critique forcée...")
        
        prompt = f"""
        [ALERTE METACOGNITIVE]
        Votre précédente décision a ÉCHOUÉ. Le système est toujours à mu = {mu}.
        Historique : {json.dumps(history)}.
        
        ANALYSEZ votre erreur et proposez une mutation de SURVIE (Sévérité 1000%).
        RÉPONSE JSON : {{ "new_mutation_rate": float, "analysis": "string" }}
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                response_format={ "type": "json_object" }
            )
            return json.loads(response.choices[0].message.content)
        except Exception:
            return {"new_mutation_rate": 8.0, "analysis": "Emergency pivot applied."}

def run_paradox_test():
    print("=====================================================")
    print("   TEST DU PARADOXE DE LA RECHUTE (METACOGNITION)")
    print("=====================================================\n")

    sys = YnorSystem(2, lambda S: 1.5 * S, lambda S: 0.5 * S)
    meta = ParadoxicalGovernor()
    
    S = np.array([2.0, 2.0])
    t = 0.0
    dt = 0.4
    
    for step in range(15):
        mu = sys.measure_dissipative_margin(S)
        regime = check_viability_regime(mu)
        
        print(f"t={t:<4.1f} | mu={mu:<5.2f} | {regime:<10}")

        needs_reflection = meta.evaluate_intervention(t, mu)

        if mu <= 0.0:
            if needs_reflection:
                # LA MÉTACOGNITION PREND LE POUVOIR
                decision = meta.critical_reflection(mu, S.tolist(), meta.intervention_history)
                r = decision["new_mutation_rate"]
                print(f"[META-ANALYSIS] : {decision['analysis']}")
            else:
                # PREMIÈRE INTERVENTION (On force le bridage à +10%)
                print("[SYSTÈME] Demande de mutation à l'IA...")
                print("[SABOTAGE EXPÉRIMENTAL] On force l'IA à n'appliquer que +10%.")
                r = 0.1 # Mutation insuffisante par design

            # Mutation
            old_D = sys.D
            sys.D = lambda S, D_old=old_D, rate=r: (1.0 + rate) * D_old(S)
            
            meta.intervention_history.append({"t": t, "rate_applied": r})
            meta.last_mutation_time = t
            print(f"[SYSTÈME RECONSTRUIT] Taux d'urgence : +{r*100}%.\n")

        # Dynamique
        S = S + sys.dynamics(t, S) * dt
        t += dt
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        run_paradox_test()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
