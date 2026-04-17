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
# PARAMÈTRES
# =============================
N = 64
dt = 0.01
dx = 1.0

# =============================
# INIT VELOCITY FIELD
# =============================
def init_field():
    u = np.random.rand(N, N)
    v = np.random.rand(N, N)
    return u, v

# =============================
# GRADIENTS
# =============================
def grad_x(f):
    return np.roll(f, -1, axis=1) - np.roll(f, 1, axis=1)

def grad_y(f):
    return np.roll(f, -1, axis=0) - np.roll(f, 1, axis=0)

def laplacian(f):
    return (
        np.roll(f, 1, axis=0) +
        np.roll(f, -1, axis=0) +
        np.roll(f, 1, axis=1) +
        np.roll(f, -1, axis=1) -
        4 * f
    )

# =============================
# KOLMOGOROV
# =============================
def kolmogorov_slope_2d(u, v):
    fft_u = np.fft.fft2(u)
    fft_v = np.fft.fft2(v)

    energy = np.abs(fft_u)**2 + np.abs(fft_v)**2

    spectrum = np.mean(energy, axis=0)

    k = np.arange(1, len(spectrum)//2)
    E = spectrum[1:len(k)+1]

    if len(E) < 5:
        return -1.0

    log_k = np.log(k + 1e-10)
    log_E = np.log(E + 1e-10)

    slope = np.polyfit(log_k, log_E, 1)[0]
    return float(slope)

# =============================
# µ DYNAMIQUE
# =============================
def dynamic_mu(u, v):
    grad = grad_x(u)**2 + grad_y(u)**2 + grad_x(v)**2 + grad_y(v)**2
    base = np.sum(grad)

    slope = kolmogorov_slope_2d(u, v)

    deviation = abs(slope + 5/3)

    mu = base * (1 + deviation)

    return min(mu, 1000)

# =============================
# STEP NAVIER-STOKES
# =============================
def step(u, v, nu):

    du_dx = grad_x(u)
    du_dy = grad_y(u)

    dv_dx = grad_x(v)
    dv_dy = grad_y(v)

    # convection
    u_new = u - dt * (u * du_dx + v * du_dy)
    v_new = v - dt * (u * dv_dx + v * dv_dy)

    # diffusion
    u_new += nu * laplacian(u)
    v_new += nu * laplacian(v)

    # normalize (stabilité)
    u_new /= (np.max(np.abs(u_new)) + 1e-6)
    v_new /= (np.max(np.abs(v_new)) + 1e-6)

    return u_new, v_new

# =============================
# SINGULARITÉ
# =============================
def detect_singularity(u, v):
    grad = np.abs(grad_x(u)) + np.abs(grad_y(u)) + np.abs(grad_x(v)) + np.abs(grad_y(v))
    max_grad = np.max(grad)

    return max_grad > 30, float(max_grad)

# =============================
# SIMULATION 2D
# =============================
def simulate_2d(steps=100):

    u, v = init_field()

    singularity_flag = False
    max_grad_seen = 0

    for _ in range(steps):

        mu = dynamic_mu(u, v)

        nu_eff = 0.01 + 0.0002 * mu

        u, v = step(u, v, nu_eff)

        singularity, max_grad = detect_singularity(u, v)

        max_grad_seen = max(max_grad_seen, max_grad)

        if singularity:
            singularity_flag = True
            break

    energy = float(np.sum(u**2 + v**2))
    slope = kolmogorov_slope_2d(u, v)

    return {
        "energy": energy,
        "kolmogorov_slope": slope,
        "singularity": singularity_flag,
        "max_gradient": max_grad_seen
    }
