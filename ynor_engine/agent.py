import torch
from config.settings import DELTA_OOD

class YnorSovereignAgent:
    def __init__(self, observer):
        self.observer = observer

    def decide(self, x, psi_reg, S):
        if S > DELTA_OOD:
            return {"action": None}
        with torch.no_grad():
            sigma, theta = self.observer(x)
        size = torch.tanh(sigma)
        return {"action": psi_reg * theta * size, "pi_s": psi_reg * theta, "size": size.item()}
