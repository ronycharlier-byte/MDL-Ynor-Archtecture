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
# MIROIR TEXTUEL - generate_ynor_graphs.py

Source : MDL_Ynor_Framework\_03_CORE_AGI_ENGINES\generate_ynor_graphs.py
Taille : 4113 octets
SHA256 : 45c121c7a43e3c55c564e9ddb0a09bf1d5246711ca55a53c0b1c913a566f9e3b

```text
import matplotlib.pyplot as plt
import numpy as np

# Paramètres du modèle
steps = np.arange(1, 16)
alpha = 0.2
beta = 0.05

# ==========================================================
# Graph 1: Compute vs Difficulty
# ==========================================================
difficulties = [0.5, 1.0, 2.0, 3.5, 6.0, 10.0]
ynor_computes = []
for diff in difficulties:
 best_step = 1
 best_L = -999
 for s in steps:
 err = np.exp(-s / diff)
 I_eff = 1.0 - err
 D_kl = err * 1.5
 L = I_eff - (alpha * D_kl) - (beta * s)
 if L > best_L:
 best_L = L
 best_step = s
 ynor_computes.append(best_step)

plt.figure(figsize=(9,6))
plt.plot(difficulties, ynor_computes, marker='o', color='#2ca02c', linewidth=2.5, markersize=8, label="AGI Ynor (Compute Auto-Régulé)")
plt.axhline(y=15, color='#d62728', linestyle='--', linewidth=2, label="Baseline LLM (Compute Statique)")
plt.title("Fig 1: Scaling Computationnel Endogène vs Difficulté", fontsize=14, fontweight='bold')
plt.xlabel("Difficulté de la Synthèse (Facteur d'atténuation de l'erreur)", fontsize=12)
plt.ylabel("Ressources physiques allouées (Steps)", fontsize=12)
plt.fill_between(difficulties, ynor_computes, 15, color='#d62728', alpha=0.1, label="Gaspillage d'énergie LLM")
plt.legend(fontsize=11)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig("fig1_compute_vs_difficulty.png", dpi=300)
plt.close()

# ==========================================================
# Graph 2: Pareto Frontier (Accuracy vs Cost)
# ==========================================================
diff = 2.5
costs = steps
accuracies = [1.0 - np.exp(-s / diff) for s in steps]
viabilities = [accuracies[s-1] - alpha * (1.5*np.exp(-s/diff)) - beta * s for s in steps]

plt.figure(figsize=(9,6))
plt.plot(costs, accuracies, 'k--', linewidth=1.5, label="Courbe d'Accuracy Brute ($I_{eff}$)")
sc = plt.scatter(costs, accuracies, c=viabilities, cmap='plasma', s=150, zorder=5, edgecolors='black')
cbar = plt.colorbar(sc)
cbar.set_label("Marge de Viabilité Ynor ($\mu$)", fontsize=12)

best_idx = np.argmax(viabilities)
plt.plot(costs[best_idx], accuracies[best_idx], 'r*', markersize=25, label=f"Optimum Strict Ynor (Step {costs[best_idx]})", markeredgecolor='white')
plt.title("Fig 2: La Frontière de Pareto Inférentielle Ynor", fontsize=14, fontweight='bold')
plt.xlabel("Coût computationnel / FLOPs ($C$)", fontsize=12)
plt.ylabel("Accuracy / Information Extraite ($I_{eff}$)", fontsize=12)
plt.axvline(x=costs[best_idx], color='gray', linestyle=':')
plt.legend(fontsize=11)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig("fig2_pareto_frontier.png", dpi=300)
plt.close()

# ==========================================================
# Graph 3: Viability Dynamics (Ablation Study)
# ==========================================================
plt.figure(figsize=(9,6))
L_ynor = [accuracies[s-1] - alpha * (1.5*np.exp(-s/diff)) - beta * s for s in steps]
L_no_c = [accuracies[s-1] - alpha * (1.5*np.exp(-s/diff)) for s in steps]
L_no_d = [accuracies[s-1] - beta * s for s in steps]

plt.plot(steps, L_ynor, color='#1f77b4', linewidth=3.5, label="Action Ynor Complète ($S_{Ynor}$)")
plt.plot(steps, L_no_c, color='#ff7f0e', linestyle='--', linewidth=2, label="Ablation NO_C ($\Rightarrow$ Crash par sur-calcul)")
plt.plot(steps, L_no_d, color='#9467bd', linestyle='-.', linewidth=2, label="Ablation NO_D ($\Rightarrow$ Halt trop précoce)")

plt.plot(best_idx+1, L_ynor[best_idx], marker='*', color='gold', markersize=20, markeredgecolor='black', label="Attracteur de Survie AGI")
plt.title("Fig 3: Dynamique Variationnelle de la Viabilité", fontsize=14, fontweight='bold')
plt.xlabel("Profondeur de calcul (steps)", fontsize=12)
plt.ylabel("Marge de Viabilité Globale ($\mu$)", fontsize=12)
plt.axhline(0, color='black', linewidth=1)
plt.legend(fontsize=11)
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig("fig3_ablation_viability.png", dpi=300)
plt.close()

print("Figures 1, 2 et 3 générées et sauvegardées avec succès !")

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
