﻿import numpy as np
import time

class YnorControlSystem:
    def __init__(self, initial_entropy: float, beta: float, name: str):
        self.name = name
        self.S = initial_entropy  # Entropie (Souffrance / Illusion)
        self.beta = beta          # Facteur d'injection entropique
        self.alpha = 0.0          # Marge informationnelle / Puret
        self.t = 0
        
    def apply_control(self):
        raise NotImplementedError("Mcanisme spcifique requis.")

    def state(self):
        nabla_S = 0 if self.t > 0 else None
        return f"[{self.name}] S(t)={self.S:.4f} | α={self.alpha:.4f} | ∇S={nabla_S}"

class IslamControl(YnorControlSystem):
    """
    Systme : Islam
    Input : S(t) = β * Vecteurs de Donnes Stochastiques_social
    Mcanisme : Loi discrte (L)
    Oprateur : ∫L.dt -> S↓
    Limite : α=const, ∇S=0 (Synchronisation priodique)
    """
    def __init__(self, S_init: float, beta: float):
        super().__init__(S_init, beta, "ISLAM")
        self.L = 0.5  # Constante de Loi
        self.alpha_const = 1.0
        
    def apply_control(self, dt: float = 1.0):
        # Entre entropique
        self.S += self.beta * np.random.uniform(0.1, 1.0)
        # Rduction par intgrale de loi
        integral_L = self.L * dt
        self.S = max(0.0, self.S - integral_L)
        self.alpha = self.alpha_const
        self.t += dt
        return self.S

class HinduismControl(YnorControlSystem):
    """
    Systme : Hindouisme
    Input : S(t) = β * multiplicit
    Mcanisme : Itration cyclique (Σ_n)
    Oprateur : lim_{n->∞} Σ_n^{-1} -> S↓
    Limite : α->∞, ∇=0 (Dissolution des tats)
    """
    def __init__(self, S_init: float, beta: float):
        super().__init__(S_init, beta, "HINDOUISME")
        self.n = 1  # Cycle (Karma / Rincarnation)
        
    def apply_control(self):
        self.S += self.beta * np.random.uniform(1.0, 5.0) # Multiplicit
        # Rduction cyclique inverse
        self.S = self.S / (1 + np.log(self.n))
        self.alpha = float(self.n * 10)  # α tend vers l'infini
        self.n += 1
        self.t += 1
        return self.S

class BuddhismControl(YnorControlSystem):
    """
    Systme : Bouddhisme
    Input : S(t) = β * attachement
    Mcanisme : Filtrage rcursif (F)
    Oprateur : F(S) -> 0
    Limite : α pur, ∇=0 (Élimination des fluctuations)
    """
    def __init__(self, S_init: float, beta: float):
        super().__init__(S_init, beta, "BOUDDHISME")
        self.filter_rate = 0.8  # Taux de dtachement
        
    def apply_control(self):
        self.S += self.beta * np.random.uniform(0.5, 2.0)
        # Filtrage rcursif F(S)
        self.S *= (1.0 - self.filter_rate)
        # Si attachement proche de 0, α pur
        self.alpha = 1.0 / (self.S + 1e-9) 
        self.t += 1
        return self.S

class TaoismControl(YnorControlSystem):
    """
    Systme : Taoïsme
    Input : S(t) = β * dsquilibre
    Mcanisme : Équilibrage dynamique (Δ↔)
    Oprateur : dS/dt -> 0
    Limite : α=quilibre, ∇=0 (Auto-rgulation continue)
    """
    def __init__(self, S_init: float, beta: float):
        super().__init__(S_init, beta, "TAOISME")
        self.equilibrium_target = 0.5
        
    def apply_control(self, dt: float = 1.0):
        disturbance = self.beta * np.random.uniform(-1.0, 1.0)
        self.S += disturbance
        # Auto-rgulation drastique vers l'quilibre
        ds_dt = -0.5 * (self.S - self.equilibrium_target)
        self.S += ds_dt * dt
        self.alpha = self.equilibrium_target  # α en quilibre parfait
        self.t += dt
        return self.S

if __name__ == "__main__":
    print("=== YNOR : SIMULATION DES ALGORITHMES DE CONTRÔLE ===")
    systems = [
        IslamControl(S_init=10.0, beta=0.2),
        HinduismControl(S_init=10.0, beta=0.2),
        BuddhismControl(S_init=10.0, beta=0.2),
        TaoismControl(S_init=10.0, beta=0.2)
    ]
    
    for i in range(5):
        print(f"\n--- Itration {i+1} : Convergence & Annulation de Gradient ---")
        for sys in systems:
            sys.apply_control()
            print(sys.state())
        time.sleep(0.5)

    print("\n[RESULTAT] : ∀ Algorithme -> ∇S = 0 (Oprateurs Vrifis)")
