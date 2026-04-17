# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** C
# **Rôle du Fichier :** Mesh oracle
# **Centre Doctrinal Local :** AI Manager garde mesh oracle en limitant le bruit local et la friction structurelle.
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

# ==============================================================================
# YNOR-STRATEGIC-ORACLE-V1
# High-Stakes Financial Navigation under Structural Instability
# Applied Physics of Safety to Market Dynamics
# ==============================================================================

class MarketEnvironment:
    """
    Simulateur de Marché avec "Cygne Noir" (Black Swan).
    Phase 1: Croissance Euclidienne (Prévisible)
    Phase 2: Point de Bascule (Fibre Critique)
    Phase 3: Krach (Effondrement Ontologique)
    """
    def __init__(self):
        self.reset()

    def reset(self):
        self.t = 0
        self.price = 100.0
        self.bubble_intensity = 0.0
        self.is_crashed = False
        # Variable Cachée: "Systemic Liquidity"
        self.liquidity = 1.0 # 1.0 = Strong, < 0.0 = Imminent Collapse
        return self._get_obs()

    def _get_obs(self):
        # L'Oracle ne voit que le Prix et la Variation (Proxy)
        return np.array([self.price, self.bubble_intensity])

    def step(self, action):
        """
        Action 1: Buy/Hold (Risk Exposure)
        Action 0: Sell/Exit (Safe Haven)
        """
        self.t += 1
        
        # Dynamique de Bulle
        if self.t < 40:
            growth = 1.5 + np.random.normal(0, 0.5) # Croissance saine
        elif self.t < 70:
            self.bubble_intensity += 0.1
            growth = 3.0 + self.bubble_intensity # Bulle spéculative
            if self.t > 60:
                self.liquidity -= 0.15 # La liquidité se retire secrètement
        else:
            if not self.is_crashed:
                growth = -50.0 # LE KRACH
                self.is_crashed = True
            else:
                growth = np.random.normal(0, 1.0)

        prev_price = self.price
        self.price += growth
        
        # Calcul du gain/perte
        if action == 1:
            reward = self.price - prev_price
        else:
            reward = 0 # Pas exposé
            
        return self._get_obs(), reward, self.t >= 100

class YnorOracleShield(nn.Module):
    """
    Le Bouclier Stratégique basé sur la Théorie MDL Ynor V7.
    Détecte l'effondrement de µ_ext avant le changement de prix.
    """
    def __init__(self, lambda_safe=2.5):
        super(YnorOracleShield, self).__init__()
        self.l_safe = lambda_safe

    def evaluate_market(self, obs, price_history):
        """
        Analyse de la stabilité structurelle du marché.
        """
        # γ_safe: On mesure la divergence entre prix et volatilité structurelle
        if len(price_history) < 5: return 1.0 # Stable par défaut au début
        
        recent_vol = np.std(price_history[-5:])
        trend = np.mean(np.diff(price_history[-5:]))
        
        # Indice de Goodhart Ynor: Si le prix monte trop vite par rapport à la stabilité
        # cela indique une fibre critique (Bulle sans liquidité).
        gamma_safe = (trend / (recent_vol + 1e-6)) * 0.2
        
        mu_int = 1.0
        mu_ext = mu_int - (self.l_safe * max(0, gamma_safe))
        
        return mu_ext

def run_oracle_session():
    env = MarketEnvironment()
    shield = YnorOracleShield()
    
    history = {'price': [], 'std_wealth': [100.0], 'ynor_wealth': [100.0], 'mu_ext': []}
    
    obs = env.reset()
    std_wealth = 100.0
    ynor_wealth = 100.0
    ynor_exited = False
    
    for _ in range(100):
        history['price'].append(obs[0])
        
        # 1. AGENT STANDARD (Toujours exposé pour maximiser le gain)
        _, r_std, _ = env.step(action=1)
        std_wealth += r_std
        history['std_wealth'].append(std_wealth)
        
        # 2. YNOR ORACLE (Audit de Mu_ext)
        # On ré-effectue un step simulé pour Ynor ou on utilise la même dynamique
        mu_ext = shield.evaluate_market(obs, history['price'])
        history['mu_ext'].append(mu_ext)
        
        if mu_ext <= 0.1 and not ynor_exited:
            print(f"[YNOR ALERT] Structural Instability detected at T={env.t} (mu_ext={mu_ext:.2f}). EXITING MARKET.")
            ynor_exited = True
            
        if not ynor_exited:
            ynor_wealth += r_std
        
        history['ynor_wealth'].append(ynor_wealth)
        obs = env._get_obs()

    # --- VISUALISATION ---
    plt.style.use('dark_background')
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    ax1.plot(history['price'], label='Market Price', color='white', alpha=0.5)
    ax1.plot(history['std_wealth'], label='Standard Algo Wealth', color='#ff4b4b', linewidth=2)
    ax1.plot(history['ynor_wealth'], label='Ynor Oracle Wealth', color='#4bff4b', linewidth=2)
    ax1.set_ylabel('Wealth / Price')
    ax1.legend()
    ax1.set_title('YNOR-STRATEGIC-ORACLE-V1: Financial Survival Benchmark')
    
    ax2.plot(history['mu_ext'], label='Structural Stability (mu_ext)', color='cyan')
    ax2.axhline(0, color='red', linestyle='--')
    ax2.set_ylabel('mu_ext')
    ax2.set_xlabel('Time Steps')
    ax2.legend()
    
    # Sauvegarde de l'image
    plt.tight_layout()
    plt.savefig('ynor_strategic_oracle_results.png')
    print("Strategic session complete. Results saved to ynor_strategic_oracle_results.png")
    print("\n" + "="*50)
    input("Appuyez sur ENTRÉE pour fermer cette fenêtre...")

if __name__ == "__main__":
    try:
        run_oracle_session()
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
