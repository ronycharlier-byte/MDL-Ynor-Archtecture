import torch
import time
from typing import Dict, Any, Optional
from config.settings import SAFE_MODE, DELTA_OOD

class YnorSovereignAgentV16:
    """
    MDL YNOR - AGENT SOUVERAIN V1.6.1
    Implemente la decision pure (pi_s) et l'allocation saturee (L).
    """
    def __init__(self, observer, quarantine_monitor):
        self.observer = observer
        self.monitor = quarantine_monitor
        self.active_position = False

    def L(self, sigma: torch.Tensor) -> torch.Tensor:
        """ Allocation saturee via tanh """
        return torch.tanh(sigma)

    def decide(self, x: torch.Tensor, psi_reg: torch.Tensor, S: float) -> Dict[str, Any]:
        """
        Calcul de la politique selon le formalisme V1.6.1
        """
        # 1. GATE ONTOLOGIQUE (Abstention)
        if S > DELTA_OOD:
            return {
                "action": None,
                "pi_s": None,
                "size": 0.0,
                "status": "ABSTENTION (OOD)"
            }

        # 2. PROJECTION Phi'
        with torch.no_grad():
            sigma, theta = self.observer(x)

        # 3. DECISION STRUCTURELLE pi_s = psi * theta
        pi_s = psi_reg * theta

        # 4. ALLOCATION L(sigma)
        size = self.L(sigma)

        return {
            "action": pi_s * size,
            "pi_s": pi_s,
            "size": size.item(),
            "status": "SOVEREIGN_VALIDATED"
        }
