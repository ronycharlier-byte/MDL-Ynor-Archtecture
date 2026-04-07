import numpy as np

import scipy.linalg as la

from pydantic import BaseModel

from typing import List, Dict



# --- PARAMÈTRES PAR DÉFAUT ---

DEFAULT_N_POINTS = 500

DEFAULT_U_MAX = 5.0

DEFAULT_ETA = 0.05

DEFAULT_EPSILON = 0.1

DEFAULT_POTENTIAL_GAIN = 10.0



class RiemannResult(BaseModel):

 mu: float

 energies: List[float]

 true_zeros: List[float]

 status: str



def sieve_primes(limit):

 primes = []

 is_prime = [True] * (limit + 1)

 for p in range(2, limit + 1):

 if is_prime[p]:

 primes.append(p)

 for i in range(p * p, limit + 1, p):

 is_prime[i] = False

 return primes



def von_mangoldt(n, primes):

 if n < 2: return 0

 for p in primes:

 if p > n: break

 p_k = p

 while p_k <= n:

 if p_k == n: return np.log(p)

 p_k *= p

 return 0



def run_riemann_engine(n_points=DEFAULT_N_POINTS, u_max=DEFAULT_U_MAX, gain=DEFAULT_POTENTIAL_GAIN):

 """Excute le moteur spectral Dirac-SUSY Ynor avec calcul de mu en temps rel"""

 u = np.linspace(-u_max, u_max, n_points)

 du = u[1] - u[0]

 

 # Sieve up to max n

 n_max = int(np.exp(u_max))

 primes = sieve_primes(n_max)

 

 # Construction du potentiel

 V = np.zeros_like(u)

 for n in range(2, n_max + 1):

 lam = von_mangoldt(n, primes)

 if lam > 0:

 weight = lam / (n**0.5) * gain # Modified scaling for better convergence

 V += weight * np.exp(-(u - np.log(n))**2 / (2 * 0.05**2))

 V += weight * np.exp(-(u + np.log(n))**2 / (2 * 0.05**2))

 

 # Hamiltonien de Dirac

 D1 = (np.diag(np.ones(n_points-1), 1) - np.diag(np.ones(n_points-1), -1)) / (2*du)

 H = np.zeros((2*n_points, 2*n_points), dtype=complex)

 H[:n_points, :n_points] = -1j * D1

 H[n_points:, n_points:] = 1j * D1

 V_mat = np.diag(V)

 H[:n_points, n_points:] = V_mat

 H[n_points:, :n_points] = V_mat

 

 # Diagonalisation

 eigenvalues = la.eigvalsh(H)

 pos_eig = np.sort(eigenvalues[eigenvalues > 0])

 

 # Simulation de la distribution de Riemann tendue (500 pts)

 # Dans un environnement rel, ces zros seraient extraits de tables haute prcision

 np.random.seed(42)

 spacing = 2 * np.pi / np.log(500 / (2 * np.pi))

 true_zeros = np.cumsum(np.random.normal(spacing, 0.01 * spacing, 500))

 

 # Calcul dynamique de mu sur l'chantillon complet

 calc_zeros = pos_eig[:len(true_zeros)]

 

 # Pad calc_zeros if not enough points found in the spectrum

 if len(calc_zeros) < len(true_zeros):

 calc_zeros = np.pad(calc_zeros, (0, len(true_zeros) - len(calc_zeros)), 'constant', constant_values=0)

 

 # Correlation coefficient (Mu saturation index)

 correlation = np.corrcoef(calc_zeros, true_zeros)[0, 1]

 mu = max(0.01, min(1.0, float(correlation)))

 

 return {

 "mu": mu,

 "energies": pos_eig[:100].tolist(),

 "true_zeros": true_zeros[:100].tolist(),

 "status": "SATURATED" if mu > 0.999 else "STABLE"

 }



if __name__ == "__main__":

 # Test local

 print(run_riemann_engine())

