import torch
import torch.nn as nn
from typing import Tuple

class YnorObserver(nn.Module):
    """
    MDL YNOR - OBSERVEUR PHI'
    Extrait sigma (densite) et theta (orientation).
    """
    def __init__(self, input_dim=64):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.Tanh(),
            nn.Linear(32, 16)
        )
        
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        features = self.backbone(x)
        # Sigma (magnitude de stabilite)
        sigma = torch.norm(features[:, :8], dim=1)
        # Theta (orientation unitaire)
        theta_raw = features[:, 8:]
        theta = theta_raw / (torch.norm(theta_raw, dim=1, keepdim=True) + 1e-6)
        return sigma, theta

def get_psi_reg(x: torch.Tensor) -> torch.Tensor:
    """ Polarite de Regime (Minimal Separator) """
    # Exemple de logique de regime (devra etre adaptee au flux reel)
    # Ici on simule une polarite basee sur la premiere composante
    return torch.sign(x[:, 0]).unsqueeze(1)
