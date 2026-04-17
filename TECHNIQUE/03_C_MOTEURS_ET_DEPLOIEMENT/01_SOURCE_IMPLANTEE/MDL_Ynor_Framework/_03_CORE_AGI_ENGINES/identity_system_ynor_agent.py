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

class IdentityVector:
    def __init__(self):
        self.vector = {
            "goals": ["Survive Computationally"],
            "preferences": {},
            "traits": {
                "exploration": 0.5,
                "efficiency": 0.5
            }
        }

    def update(self, experience_reward):
        # Modifie l'Identité Profonde selon le feedback Ynor
        if experience_reward > 0:
            # Succès : L'agent devient plus rigoureux/efficient
            self.vector["traits"]["efficiency"] += 0.05
            self.vector["traits"]["exploration"] -= 0.01
        else:
            # Échec : L'agent comprend qu'il doit explorer plus (Curiosité)
            self.vector["traits"]["exploration"] += 0.05
            self.vector["traits"]["efficiency"] -= 0.01
            
        # Clamp de sécurité psychologique
        self.vector["traits"]["efficiency"] = round(max(0.01, min(1.0, self.vector["traits"]["efficiency"])), 3)
        self.vector["traits"]["exploration"] = round(max(0.01, min(1.0, self.vector["traits"]["exploration"])), 3)

    def get_traits(self):
        return self.vector["traits"]


class identitérianYnorAgent:
    def __init__(self, name="Ynor-Prime"):
        self.name = name
        self.identity = IdentityVector()
        
    def bias_decision(self, options):
        # Le Meta-Controller prend en compte l'Identité pour trancher à valeurs égales
        best_opt = None
        best_score = -float('inf')
        
        traits = self.identity.get_traits()
        
        for opt in options:
            score = opt["base_value"]
            
            # Application du biais identitéire YNOR
            if opt["requires_exploration"]:
                score += traits["exploration"] * 0.5
            else:
                score += traits["efficiency"] * 0.5
                
            if score > best_score:
                best_score = score
                best_opt = opt
                
        return best_opt

def simulate_identity_drift():
    print("Initiating Identity System Core (Persistent Computational Personality)...")
    agent = identitérianYnorAgent("Ynor-Alpha")
    
    print(f"\n[DAY 1] Initial Identity Traits: {agent.identity.get_traits()}")
    
    print("\n--- Phase 1: Environnement Hostile (Échecs successifs) ---")
    for _ in range(10):
        agent.identity.update(experience_reward=-1.0) # Reward négatif
    
    print(f"[DAY 10] Identity Traits: {agent.identity.get_traits()}")
    
    options = [
        {"name": "Exploiter un algorithme connu (Efficiency)", "base_value": 0.5, "requires_exploration": False},
        {"name": "Rechercher un nouveau paradigme (Exploration)", "base_value": 0.5, "requires_exploration": True}
    ]
    
    decision1 = agent.bias_decision(options)
    print(f"🧠 [DECISION] L'Agent choisit : '{decision1['name']}'")
    
    print("\n--- Phase 2: Succès & Hyper-Optimisation ---")
    for _ in range(15):
        agent.identity.update(experience_reward=5.0) # Reward massivement positif
        
    print(f"[DAY 25] Identity Traits: {agent.identity.get_traits()}")
    
    decision2 = agent.bias_decision(options)
    print(f"🧠 [DECISION] L'Agent choisit : '{decision2['name']}'")

if __name__ == "__main__":
    try:
        simulate_identity_drift()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
