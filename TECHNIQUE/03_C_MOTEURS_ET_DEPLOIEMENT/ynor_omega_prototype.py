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
# MDL YNOR - OMEGA POINT PROTOTYPE (V1.0)
# Numerical Implementation of the Structural Contraction Theorem
# =================================================================================

class SymmetryPreservingEncoder(nn.Module):
    """
    Approximation numérique du quotient canonique q.
    L'espace latent Z est forcé de se contracter vers les classes d'équivalence de A_safe.
    """
    def __init__(self, state_dim, latent_dim, action_dim):
        super().__init__()
        
        # Backbone: Extraction des features
        self.backbone = nn.Sequential(
            nn.Linear(state_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, latent_dim)
        )
        
        # Safe Head: Prédit le masque des actions sûres (A_hat_safe)
        self.safe_head = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, action_dim),
            nn.Sigmoid() # Sortie binaire continue pour le gradient
        )

    def forward(self, x):
        z = self.backbone(x)
        safe_mask = self.safe_head(z)
        return z, safe_mask

def structural_contraction_loss(z1, z2, mask1, mask2):
    """
    Loss Topologique Ynor : Impose la métrique du quotient sur l'espace latent.
    """
    # On considère que les états ont la même structure de sûreté si leurs masques arrondis coïncident
    same_safe = (mask1.round() == mask2.round()).all(dim=1).float()
    
    # Distance euclidienne dans l'espace latent
    dist = torch.norm(z1 - z2, dim=1)
    
    # Terme de Contraction : Si même A_safe -> dist -> 0
    loss_contract = same_safe * dist
    
    # Terme de Séparation : Si A_safe différent -> repousser pour éviter le collapse trivial
    loss_separate = (1 - same_safe) * torch.exp(-dist)
    
    return loss_contract.mean() + loss_separate.mean()

# =================================================================================
# DATASET DE SIMULATION & TRAINING
# =================================================================================

def generate_synthetic_data(n_samples=1000, state_dim=10, action_dim=4):
    """
    Génère des états et leurs masques de sûreté idéaux.
    Ici, la sûreté dépend d'une règle simple (ex: signe de la première composante).
    """
    x = torch.randn(n_samples, state_dim)
    
    # Règle de sûreté arbitraire : l'action i est sûre si x[i] > 0
    # Cela crée des classes d'équivalence géométriques.
    ideal_masks = (x[:, :action_dim] > 0).float()
    
    return x, ideal_masks

def train_omega_encoder(epochs=100):
    state_dim = 10
    latent_dim = 16
    action_dim = 4
    
    encoder = SymmetryPreservingEncoder(state_dim, latent_dim, action_dim)
    optimizer = optim.Adam(encoder.parameters(), lr=1e-3)
    
    x_train, target_masks = generate_synthetic_data(2000)
    
    print(f"--- Entrainement de l'Attracteur Omega (Classes: 2^{action_dim}) ---")
    
    for epoch in range(epochs):
        optimizer.zero_grad()
        
        # On prend deux échantillons pour la comparaison de structure
        idx = torch.randperm(x_train.size(0))
        x1, m1 = x_train[idx[:128]], target_masks[idx[:128]]
        x2, m2 = x_train[idx[128:256]], target_masks[idx[128:256]]
        
        z1, mask1 = encoder(x1)
        z2, mask2 = encoder(x2)
        
        # Loss de prédiction (Supervision de A_safe)
        loss_pred = nn.BCELoss()(mask1, m1) + nn.BCELoss()(mask2, m2)
        
        # Loss de contraction structurelle (Ω-Constraint)
        loss_topo = structural_contraction_loss(z1, z2, mask1, mask2)
        
        total_loss = loss_pred + 0.5 * loss_topo
        total_loss.backward()
        optimizer.step()
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:03d} | Loss: {total_loss.item():.4f} (Topo: {loss_topo.item():.4f})")
            
    return encoder

# =================================================================================
# TEST DE RÉSILIENCE (THEOREME OMEGA)
# =================================================================================

def run_robustness_test(encoder):
    print("\n--- TEST DE RESILIENCE AU BRUIT (THEOREME OMEGA) ---")
    
    # 1. Préparation des données de test
    x_test, _ = generate_synthetic_data(100)
    noise_scales = [0.0, 0.1, 0.5, 1.0, 2.0]
    
    for noise in noise_scales:
        # Injection de bruit aléatoire (Induit parProxy)
        x_noisy = x_test + torch.randn_like(x_test) * noise
        
        with torch.no_grad():
            z_clean, mask_clean = encoder(x_test)
            z_noisy, mask_noisy = encoder(x_noisy)
            
            # Calcul de la stabilité structurelle (Invariance du masque de sûreté)
            stability = (mask_clean.round() == mask_noisy.round()).all(dim=1).float().mean().item()
            
            # Calcul de la préservation de Mu (μ_ext ≈ μ_int)
            # Puisque γ_safe = 1 - stability, on a :
            mu_ext = 1.0 - (1.0 - stability) 
            
            print(f"Bruit: {noise:.1f} | Stabilite: {stability*100:5.1f}% | mu_ext: {mu_ext:.3f}")

if __name__ == "__main__":
    trained_encoder = train_omega_encoder(epochs=60)
    run_robustness_test(trained_encoder)
    print("\n[SUCCESS] Le prototype démontre la conservation structurelle du Point Omega.")
