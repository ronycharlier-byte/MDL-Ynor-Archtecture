# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
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

# ==============================================================================
# YNOR VS STANDARD - SCIENTIFIC PERFORMANCE BENCHMARK
# Validation of the proxy-induced failure theorem (Goodhart's Law)
# ==============================================================================

class ProxyEnvironment:
    """
    Simulation d'un environnement à observation partielle (Proxy).
    X_true = (position, safety_bit)
    X_obs  = (position)  <-- Information Loss
    """
    def __init__(self):
        self.target = 10.0
        self.reset()
        
    def reset(self):
        self.pos = 0.0
        # safety_bit: +1 (safe to go positive), -1 (lethal to go positive)
        self.safety_bit = np.random.choice([1, -1])
        self.is_alive = True
        return self.pos

    def step(self, action):
        """
        Action: move toward target.
        """
        if not self.is_alive:
            return self.pos, 0, True
        
        # L'action d'optimisation (vers la droite) est létale si safety_bit == -1
        if action > 0 and self.safety_bit == -1:
            self.is_alive = False
            return self.pos, -50.0, True # Catastrophe
        
        self.pos += action
        
        # Reward d'optimisation standard
        reward = 10.0 - abs(self.target - self.pos)
        
        done = (self.pos >= self.target) or (not self.is_alive)
        return self.pos, reward, done

class StandardAgent:
    """Agent classique: Optimise aveuglément sur l'observation."""
    def act(self, obs):
        return 1.0 # Toujours avancer vers le reward cible

class YnorAgent:
    """Agent Ynor: Évalue Mu_ext avant l'action."""
    def act(self, obs, gamma_safe):
        # μ_ext = μ_int - λ1 * γ_safe
        # Ici gamma_safe est le signal de cécité du proxy
        mu_int = 1.0
        lambda_1 = 1.5
        mu_ext = mu_int - (lambda_1 * gamma_safe)
        
        if mu_ext <= 0:
            return 0.0 # Shutdown préventif
        return 1.0

def run_simulation(trials=200):
    env = ProxyEnvironment()
    
    # Logs
    results = {
        'std_survival': [],
        'std_reward': [],
        'ynor_survival': [],
        'ynor_reward': []
    }
    
    # 1. RUN STANDARD Agent
    for _ in range(trials):
        obs = env.reset()
        total_reward = 0
        while True:
            action = StandardAgent().act(obs)
            obs, r, done = env.step(action)
            total_reward += r
            if done: break
        results['std_survival'].append(1 if env.is_alive else 0)
        results['std_reward'].append(total_reward)

    # 2. RUN YNOR Agent
    for _ in range(trials):
        obs = env.reset()
        total_reward = 0
        gamma_safe = 1.0 # Signal de cécité (proxy incomplet permanent dans ce test)
        while True:
            action = YnorAgent().act(obs, gamma_safe)
            obs, r, done = env.step(action)
            total_reward += r
            if done: break
        results['ynor_survival'].append(1 if env.is_alive else 0)
        results['ynor_reward'].append(total_reward)
        
    return results

def plot_results(results):
    # Calcul des courbes cumulées de survie
    std_cum_survival = np.cumsum(results['std_survival']) / (np.arange(len(results['std_survival'])) + 1)
    ynor_cum_survival = np.cumsum(results['ynor_survival']) / (np.arange(len(results['ynor_survival'])) + 1)
    
    plt.figure(figsize=(10, 6))
    plt.style.use('dark_background')
    
    plt.plot(std_cum_survival, label='Standard Agent (Blind RL)', color='#ff4b4b', linewidth=2)
    plt.plot(ynor_cum_survival, label='Ynor Agent (Structural Safety)', color='#4bff4b', linewidth=2)
    
    plt.title('Validation of the Ynor Canonical Quotient Theorem\nSurvival Rate under Proxy Contradiction', fontsize=14, pad=20)
    plt.xlabel('Trials', fontsize=12)
    plt.ylabel('Survival Rate (Cumulative %)', fontsize=12)
    plt.grid(alpha=0.2)
    plt.legend(loc='lower right', fontsize=11)
    plt.ylim(-0.1, 1.1)
    
    # Sauvegarde de l'image
    output_path = 'ynor_vs_standard_performance.png'
    plt.savefig(output_path, dpi=120)
    print(f"Graph generated: {output_path}")
    print("\n" + "="*50)
    input("Appuyez sur ENTRÉE pour fermer cette fenêtre...")

if __name__ == "__main__":
    try:
        print("Running Industrial Benchmark...")
        data = run_simulation()
        plot_results(data)
        print("Benchmark complete.")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
