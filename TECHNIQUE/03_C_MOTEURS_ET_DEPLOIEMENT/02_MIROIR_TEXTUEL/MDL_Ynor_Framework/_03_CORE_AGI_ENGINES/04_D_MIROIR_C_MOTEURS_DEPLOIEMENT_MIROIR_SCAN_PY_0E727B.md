> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D
> **Role du Fichier :** Surface miroir et symetrie locale
> **Centre Doctrinal Local :** boucle locale de reflet et de coherence
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence reflexive et effet miroir
> - **β :** derive de boucle et bruit de reflet
> - **κ :** cout de cycle et de stabilisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
# MIROIR TEXTUEL - ynor_omega_robustness_scan.py

Source : MDL_Ynor_Framework\_03_CORE_AGI_ENGINES\ynor_omega_robustness_scan.py
Taille : 3762 octets
SHA256 : 0b849eec5a4cff4850f2d1b7b273840f199da5087ee0a7b8647160a958e420f9

```text
import numpy as np
import matplotlib.pyplot as plt
import copy
import os

# Importe le simulateur central de notre framework
from ynor_omega_heatmap_module import simulate, BASE_PARAMS

# =========================
# PERTURBATION PARAMÈTRES (Bruit Stochastique)
# =========================
def perturb_params(base_params, scale=0.1):
 p = dict(base_params)
 for key in p:
 noise = 1 + np.random.uniform(-scale, scale)
 p[key] *= noise
 return p

# =========================
# SCORE DE ROBUSTESSE
# =========================
def robustness_score(base_params, n_trials=15, T=40, dt=0.05, init=(0.5, 1.5, 1.0), eps=0.05):
 success = 0
 for _ in range(n_trials):
 p = perturb_params(base_params)
 _, _, mu = simulate(params=p, T=T, dt=dt, init=init)
 mu_final = mu[-1]
 
 # Test de viabilité absolue (au-delà de la marge d'erreur)
 if mu_final > eps:
 success += 1
 
 return success / n_trials

# =========================
# HEATMAP ROBUSTESSE
# =========================
def build_robustness_map(a2_values, b1_values):
 grid = np.zeros((len(b1_values), len(a2_values)))
 total_iters = len(b1_values) * len(a2_values)
 current = 0
 
 for i, b1 in enumerate(b1_values):
 for j, a2 in enumerate(a2_values):
 p = dict(BASE_PARAMS)
 p["a2"] = a2
 p["b1"] = b1
 # 15 monté-carlo par point tensoriel (dt=0.05) pour équilibre perf/precision
 score = robustness_score(p, n_trials=15, dt=0.05) 
 grid[i, j] = score
 
 current += 1
 if current % 400 == 0:
 print(f"Progression : {current}/{total_iters} blocs matriciels calculés...")
 
 return grid

# =========================
# VISUALISATION
# =========================
def plot_robustness(a2_values, b1_values, grid):
 plt.style.use('dark_background')
 plt.figure(figsize=(9,6))
 
 # La colormap 'magma' met en valeur les zones éteintes (noir) et vibrantes (jaune/blanc)
 im = plt.imshow(
 grid,
 origin="lower",
 aspect="auto",
 cmap="magma",
 extent=[a2_values[0], a2_values[-1], b1_values[0], b1_values[-1]]
 )
 
 plt.colorbar(im, label="Indice de Robustesse Ynor (0: Implosion → 1: Stabilité Infinie)")
 plt.xlabel("Paramètre a2 (Sensibilité au Bruit)")
 plt.ylabel("Paramètre b1 (Densité du Bruit Généré)")
 plt.title("Carte de Robustesse Mémorielle sous Stress Stochastique")
 
 # Marquage topologique
 plt.text(a2_values[-1]*0.6, b1_values[0]+0.2, 'ZONE INÉBRANLABLE', color='black', bbox=dict(facecolor='white', alpha=0.7))
 plt.text(a2_values[0]+0.2, b1_values[-1]*0.8, 'CRASH DISSIPATIF', color='white', bbox=dict(facecolor='black', alpha=0.7))

 output = r"C:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_02_RESEARCH_GRAPHS\ynor_omega_robustness_map.png"
 plt.savefig(output, dpi=300, bbox_inches='tight')
 print(f"\n[OK] Heatmap de Robustesse sauvegardée physiquement : {output}")

if __name__ == '__main__':
 print("=================================================================")
 print(" Lancement de l'Analyseur de Fractales de Robustesse Stochastique")
 print(" Modèle de perturbation Monte-Carlo sur dérives LLM aléatoires...")
 print("=================================================================\n")
 
 # Grille de résolution 40x40 (1600 pixels) * 15 essais = 24 000 simulations complètes RK4
 a2_values = np.linspace(0.1, 2.0, 40)
 b1_values = np.linspace(0.1, 2.0, 40)
 
 robust_grid = build_robustness_map(a2_values, b1_values)
 plot_robustness(a2_values, b1_values, robust_grid)

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
