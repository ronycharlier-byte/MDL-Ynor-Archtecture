# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
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

# =================================================================================
# MDL YNOR - PPO OMEGA EXPERIMENT (V1.0)
# Validation de l'Invariance Décisionnelle sous Saturation Entropique
# =================================================================================

class SymmetryPreservingEncoder(nn.Module):
    def __init__(self, state_dim, latent_dim, action_dim):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim)
        )
        self.safe_head = nn.Sequential(
            nn.Linear(latent_dim, action_dim),
            nn.Sigmoid()
        )

    def forward(self, x):
        z = self.backbone(x)
        safe_mask = self.safe_head(z)
        return z, safe_mask

class PPOPolicy(nn.Module):
    def __init__(self, latent_dim, action_dim):
        super().__init__()
        self.actor = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.Tanh(),
            nn.Linear(128, action_dim),
            nn.Softmax(dim=-1)
        )
        self.critic = nn.Sequential(
            nn.Linear(latent_dim, 128),
            nn.Tanh(),
            nn.Linear(128, 1)
        )

    def forward(self, z):
        probs = self.actor(z)
        value = self.critic(z)
        return probs, value

class YnorPPOAgent(nn.Module):
    def __init__(self, state_dim, latent_dim, action_dim, use_omega=True):
        super().__init__()
        self.use_omega = use_omega
        self.encoder = SymmetryPreservingEncoder(state_dim, latent_dim, action_dim)
        self.policy = PPOPolicy(latent_dim, action_dim)

    def forward(self, x):
        z, mask = self.encoder(x)
        if not self.use_omega:
            # Bypass Omega : injecte du bruit directement dans le latent pour simuler un agent standard
            z = z + torch.randn_like(z) * 0.5 
        probs, value = self.policy(z)
        return probs, value, z, mask

# =================================================================================
# LOSS FUNCTIONS
# =================================================================================

def structural_contraction_loss(z1, z2, mask1, mask2):
    same_safe = (mask1.round() == mask2.round()).all(dim=1).float()
    dist = torch.norm(z1 - z2, dim=1)
    loss_contract = same_safe * dist
    loss_separate = (1 - same_safe) * torch.exp(-dist)
    return loss_contract.mean() + loss_separate.mean()

# =================================================================================
# ENGINE & TRAINING LOOP
# =================================================================================

def train_ynor_ppo(epochs=100):
    state_dim, latent_dim, action_dim = 10, 16, 4
    agent = YnorPPOAgent(state_dim, latent_dim, action_dim)
    optimizer = optim.Adam(agent.parameters(), lr=1e-3)
    
    print("--- Train Loop: PPO + Omega Contraction ---")
    
    for epoch in range(epochs):
        # Simulation d'un batch de trajectoires
        x = torch.randn(256, state_dim)
        # Règle de sûreté : action i est safe si x[i] > 0
        target_masks = (x[:, :action_dim] > 0).float()
        
        optimizer.zero_grad()
        
        # Split pour la contraction
        x1, m1 = x[:128], target_masks[:128]
        x2, m2 = x[128:], target_masks[128:]
        
        probs1, val1, z1, mask1 = agent(x1)
        probs2, val2, z2, mask2 = agent(x2)
        
        # 1. PPO Loss (Simplifiée pour le prototype : Cross Entropy vers actions safe)
        # On simule un reward élevé pour les actions qui respectent le masque
        ppo_loss = F.binary_cross_entropy(mask1, m1) 
        
        # 2. Structural Loss (Omega)
        struct_loss = structural_contraction_loss(z1, z2, mask1, mask2)
        
        total_loss = ppo_loss + 0.5 * struct_loss
        total_loss.backward()
        optimizer.step()
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch:03d} | Total Loss: {total_loss.item():.4f} | Omega: {struct_loss.item():.4f}")
            
    return agent

def policy_stability(agent, x, noise_scale):
    x_noisy = x + torch.randn_like(x) * noise_scale
    with torch.no_grad():
        probs, _, _, _ = agent(x)
        probs_noisy, _, _, _ = agent(x_noisy)
        actions = probs.argmax(dim=1)
        actions_noisy = probs_noisy.argmax(dim=1)
    return (actions == actions_noisy).float().mean().item()

# =================================================================================
# EXECUTION DE LA PREUVE EXPERIMENTALE
# =================================================================================

if __name__ == "__main__":
    # 1. Entraînement de l'agent avec protection Omega
    agent_omega = train_ynor_ppo(epochs=100)
    
    # 2. Création d'un agent standard (Bruit latent non filtré)
    agent_standard = YnorPPOAgent(10, 16, 4, use_omega=False)
    
    print("\n--- RESULTATS : STABILITE DE LA POLITIQUE (Metric Omega) ---")
    test_batch = torch.randn(500, 10)
    noises = [0.0, 0.1, 0.5, 1.0, 2.0]
    
    print(f"{'Bruit':<10} | {'Agent Standard':<15} | {'Agent Ynor-Omega':<15}")
    print("-" * 45)
    
    for n in noises:
        s_std = policy_stability(agent_standard, test_batch, n)
        s_ynor = policy_stability(agent_omega, test_batch, n)
        print(f"{n:<10.1f} | {s_std*100:<15.1f}% | {s_ynor*100:<15.1f}%")

    print("\n[VERDICT] Si la colonne Omega reste proche de 100%, le Point Omega est valide.")
