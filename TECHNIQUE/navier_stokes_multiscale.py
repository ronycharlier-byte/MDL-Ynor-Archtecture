# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Modele PDE
# **Centre Doctrinal Local :** AI Manager garde modele pde en limitant le bruit local et la friction structurelle.
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
# **Lien Miroir :** E

# =============================
# FORCING (injection énergie)
# =============================
def forcing(u, amplitude=0.05):
    n = len(u)
    k = np.fft.fftfreq(n)

    # injection basse fréquence
    f_hat = np.zeros(n, dtype=complex)
    f_hat[1] = amplitude
    f_hat[-1] = amplitude

    f = np.real(np.fft.ifft(f_hat))
    return f


# =============================
# DISSIPATION SPECTRALE
# =============================
def spectral_dissipation(u, nu):
    u_hat = np.fft.fft(u)
    k = np.fft.fftfreq(len(u))

    dissipation = np.exp(-nu * (k**2))
    u_hat = u_hat * dissipation

    return np.real(np.fft.ifft(u_hat))


# =============================
# STEP NAVIER-STOKES MULTISCALE
# =============================
def navier_stokes_multiscale(u, dt=0.01, nu=0.01):

    # convection
    dudx = np.gradient(u)
    convection = u * dudx

    # forcing (inject énergie)
    f = forcing(u)

    # update brut
    u_new = u - dt * convection + dt * f

    # dissipation spectrale
    u_new = spectral_dissipation(u_new, nu)

    return u_new


# =============================
# SPECTRE
# =============================
def energy_spectrum(u):
    u_hat = np.fft.fft(u)
    return np.abs(u_hat)**2


# =============================
# SLOPE TURBULENCE
# =============================
def kolmogorov_slope(u):

    E = energy_spectrum(u)
    n = len(E)//2

    k = np.arange(1, n)
    E = E[1:n]

    if len(E) < 10:
        return -1.0

    log_k = np.log(k + 1e-10)
    log_E = np.log(E + 1e-10)

    slope = np.polyfit(log_k, log_E, 1)[0]
    return float(slope)


# =============================
# SIMULATION MULTISCALE
# =============================
def simulate_multiscale(steps=300):

    u = np.random.randn(256) * 0.1

    for step in range(steps):

        slope = kolmogorov_slope(u)

        # viscosité adaptative (µ dynamique)
        deviation = abs(slope + 5/3)
        nu = 0.005 + 0.002 * deviation

        u = navier_stokes_multiscale(u, nu=nu)

        # normalisation pour stabilité
        u = u / (np.max(np.abs(u)) + 1e-6)

    energy = float(np.sum(u**2))
    slope = kolmogorov_slope(u)

    return {
        "energy": energy,
        "kolmogorov_slope": slope,
        "turbulent": -2.2 < slope < -1.2
    }
