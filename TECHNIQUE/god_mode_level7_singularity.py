# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Script ou configuration declarative
# **Centre Doctrinal Local :** AI Manager garde script ou configuration declarative en limitant le bruit local et la friction structurelle.
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
# INIT
# =============================
memory = VectorMemory()

MEMORY_PATH = r"C:\Users\ronyc\Desktop\Corpus\MDL Ynor\TECHNIQUE\vector_memory.json"

if os.path.exists(MEMORY_PATH):
    memory.load_from_json(MEMORY_PATH)
else:
    print("⚠️ Memory file not found → fallback mode")

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

knowledge = []

# =============================
# NAVIER-STOKES 1D (STABLE)
# =============================
def navier_stokes_1d(u, nu=0.05, dt=0.005, dx=1.0):
    dudx = np.gradient(u, dx)
    d2udx2 = np.gradient(dudx, dx)

    # CFL stabilization
    u = u - dt * (u * dudx) + nu * dt * d2udx2

    # normalize to avoid explosion
    u = u / (np.max(np.abs(u)) + 1e-6)

    return u

# =============================
# SPECTRAL ANALYSIS
# =============================
def spectral_analysis(u):
    u_hat = np.fft.fft(u)
    spectrum = np.abs(u_hat) ** 2
    return spectrum

# =============================
# KOLMOGOROV SLOPE
# =============================
def kolmogorov_slope(u):
    spectrum = spectral_analysis(u)

    n = len(spectrum) // 2
    k = np.arange(1, n)

    E = spectrum[1:n]

    if len(E) < 5:
        return -1.0

    log_k = np.log(k + 1e-10)
    log_E = np.log(E + 1e-10)

    slope = np.polyfit(log_k, log_E, 1)[0]
    return float(slope)

# =============================
# µ DYNAMIQUE (SAFE)
# =============================
def dynamic_mu(u):
    grad = np.gradient(u)
    base = np.sum(grad**2)

    slope = kolmogorov_slope(u)

    deviation = abs(slope + 5/3)

    mu = base * (1 + deviation)

    # clamp pour éviter explosion
    mu = min(mu, 1000)

    return mu

# =============================
# SINGULARITY DETECTION
# =============================
def detect_singularity(u):
    grad = np.gradient(u)
    max_grad = np.max(np.abs(grad))

    return max_grad > 20, float(max_grad)

# =============================
# SIMULATION
# =============================
def simulate(steps=120):
    u = np.random.rand(128)

    singularity_flag = False
    max_gradient_seen = 0

    for _ in range(steps):
        mu = dynamic_mu(u)

        nu_eff = 0.01 + 0.0003 * mu

        u = navier_stokes_1d(u, nu=nu_eff)

        singularity, max_grad = detect_singularity(u)

        max_gradient_seen = max(max_gradient_seen, max_grad)

        if singularity:
            singularity_flag = True
            break

    energy = float(np.sum(u**2))
    grad_energy = float(np.sum(np.gradient(u)**2))
    slope = kolmogorov_slope(u)

    return {
        "energy": energy,
        "gradient": grad_energy,
        "kolmogorov_slope": slope,
        "singularity": singularity_flag,
        "max_gradient": max_gradient_seen
    }

# =============================
# QUESTION
# =============================
def generate_question(context):
    prompt = f"""
Tu es un chercheur.

CONTEXTE:
{context}

Pose UNE question profonde sur stabilité ou singularité.
"""
    return llm.invoke(prompt).content.strip()

# =============================
# ANALYSE
# =============================
def analyze(question):
    try:
        results = memory.search(question, top_k=5)
    except:
        results = []

    if not results:
        return "Pas de données corpus."

    context = "\n\n".join([r["text"] for r in results if "text" in r])

    prompt = f"""
Analyse:

QUESTION:
{question}

CONTEXTE:
{context}

FORMAT:
- idées clés
- mécanismes
- limites
"""
    return llm.invoke(prompt).content

# =============================
# HYPOTHÈSE
# =============================
def generate_hypothesis(analysis):
    prompt = f"""
Formule une hypothèse scientifique testable :

{analysis}
"""
    return llm.invoke(prompt).content.strip()

# =============================
# TEST
# =============================
def test_hypothesis():
    result = simulate()

    stable_energy = result["energy"] < 10
    slope = result["kolmogorov_slope"]

    kolmogorov_ok = -2.2 < slope < -1.2
    no_singularity = not result["singularity"]

    stable = stable_energy and kolmogorov_ok and no_singularity

    return result, stable

# =============================
# SCORE
# =============================
def score_hypothesis(hypothesis, stable):
    score = 0

    if stable:
        score += 3

    keywords = ["seuil", "critique", "singular", "μ", "mu"]

    for k in keywords:
        if k in hypothesis.lower():
            score += 1

    return score

# =============================
# SAVE
# =============================
def save_knowledge():
    with open("knowledge.json", "w", encoding="utf-8") as f:
        json.dump(knowledge, f, indent=2, ensure_ascii=False)

# =============================
# GOD MODE
# =============================
def god_mode(topic, iterations=10):

    context = topic

    for i in range(iterations):
        print(f"\n🧠 ITERATION {i+1}")

        question = generate_question(context)
        print(f"\n❓ {question}")

        analysis = analyze(question)
        print(f"\n📊 {analysis}")

        hypothesis = generate_hypothesis(analysis)
        print(f"\n💡 {hypothesis}")

        result, stable = test_hypothesis()

        print("\n🧪 Simulation:", result)
        print("Stable:", stable)

        score = score_hypothesis(hypothesis, stable)
        print("🏁 Score:", score)

        knowledge.append({
            "question": question,
            "analysis": analysis,
            "hypothesis": hypothesis,
            "result": result,
            "stable": stable,
            "score": score
        })

        context = hypothesis

    save_knowledge()

# =============================
# RUN
# =============================
if __name__ == "__main__":
    topic = input("🎯 Sujet: ")
    god_mode(topic, iterations=10)
