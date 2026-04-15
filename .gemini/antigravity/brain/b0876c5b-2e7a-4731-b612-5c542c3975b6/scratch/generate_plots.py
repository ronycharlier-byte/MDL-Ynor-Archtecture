import sys
import os
import numpy as np
import matplotlib.pyplot as plt

# Add algorithms path to sys.path
sys.path.append(r"c:\Users\ronyc\Desktop\MDL Ynor\SCIENTIFIC_CORPUS\03_ALGORITHMS")

from NS_SIMULATOR import NSSimulator

def generate_stability_plots():
    betas = np.linspace(0.1, 1.8, 10)
    steps = 400
    means_mu = []
    errors_inf = []
    
    print("Generating Stability Data for Graphics...")
    
    for b in betas:
        sim = NSSimulator(N=64)
        mu_hist = []
        energy_hist = []
        
        for i in range(steps):
            metrics = sim.step(forcing_amp=b)
            # Use points after convergence (last 100 steps)
            if i > 300:
                mu_hist.append(metrics['mu'])
                energy_hist.append(metrics['energy'])
        
        means_mu.append(np.mean(mu_hist))
        errors_inf.append(np.mean(energy_hist))
        print(f"Beta {b:.2f} -> Mu {np.mean(mu_hist):.4f}, Error {np.mean(energy_hist):.4f}")

    # Plotting
    plt.figure(figsize=(10, 6))
    
    # Correcting mu for the plot (inverse relation)
    inv_mu = [1.0/abs(m) if m != 0 else 0 for m in means_mu]
    
    plt.subplot(1, 2, 1)
    plt.plot(betas, means_mu, 'o-', color='blue', label='Margin mu')
    plt.axhline(0, color='red', linestyle='--')
    plt.xlabel('Noise Input (Beta)')
    plt.ylabel('Dissipative Margin (mu)')
    plt.title('Decay of Margin mu vs Noise')
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(inv_mu, errors_inf, 's-', color='green', label='Error e_inf')
    plt.xlabel('Inverse Margin (1/mu)')
    plt.ylabel('Residual Error (e_inf)')
    plt.title('Convergence Law: e_inf ~ 1/mu')
    plt.grid(True)
    
    plt.tight_layout()
    
    # Save plot
    plot_dir = r"c:\Users\ronyc\Desktop\MDL Ynor\SCIENTIFIC_CORPUS\04_EMPIRICAL\plots"
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
        
    plot_path = os.path.join(plot_dir, "stability_analysis.png")
    plt.savefig(plot_path)
    print(f"Plot saved at {plot_path}")

if __name__ == "__main__":
    generate_stability_plots()
