import torch
import time
from config.settings import S_CRIT, TAU, MIN_PI_NORM

class YnorExitMorphismV16:
    """
    MDL YNOR - MORPHISME DE SORTIE V1.6
    Sortie uniquement sur degradation de structure.
    """
    def __init__(self):
        self.s_crit = S_CRIT
        self.tau = TAU
        self.min_pi_norm = MIN_PI_NORM

    def should_exit(self, current_psi, entry_psi, current_s, pi_s, entry_time) -> tuple[bool, str]:
        now = time.time()
        duration = now - entry_time

        # 1. Flip de polarite
        if current_psi * entry_psi < 0:
            return True, "POLARITY_FLIP"

        # 2. Desagregation structurelle
        if current_s > self.s_crit:
            return True, "STRUCTURAL_DEGRADATION"

        # 3. Entropie + Affaiblissement
        if duration > self.tau and torch.norm(pi_s) < self.min_pi_norm:
            return True, "ENTROPIC_TIMEOUT_WEAKENING"

        return False, "VALID"
