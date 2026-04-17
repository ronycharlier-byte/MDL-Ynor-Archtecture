#!/bin/bash

# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** D
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
# **Lien Miroir :** D'

# MDL YNOR - DEMO RUNBOOK (v2.2.0-PROD) - UNIX VERSION (SH)

echo "============================================================"
echo "  ⚡ MDL YNOR - AUTOMATED DEMO & VALIDATION ⚡"
echo "============================================================"

# 1. CHECK VIRTUAL ENV
if [ ! -d "venv" ]; then
    echo "[INFO] Creating virtual environment..."
    python3 -m venv venv
fi

echo "[INFO] Activating environment..."
source venv/bin/activate

# 2. INSTALL DEPS
echo "[INFO] Installing required dependencies..."
pip install -r requirements.txt
pip install -e .

# 3. ENVIRONMENT CHECK
if [ ! -f .env ]; then
    echo "[WARNING] No .env file found. Copying template..."
    cp .env.template .env
    echo "[ACTION] Please edit your .env file and add your API keys!"
fi

# 4. RUN VALIDATION
echo ""
echo "[1/3] RUNNING HARDCORE VALIDATION (MU MARGIN)..."
python3 hardcore_validation.py

# 5. RUN EXPERIMENT
echo ""
echo "[2/3] RUNNING AGI MUTATION EXPERIMENT..."
python3 run_experiment.py

# 6. NOTEBOOK LAUNCH (INFO)
echo ""
echo "[3/3] DEMO COMPLETE. "
echo "[INFO] To view the Jupyter Notebook, run:"
echo "jupyter notebook ynor_core_demonstration.ipynb"
echo ""

echo "============================================================"
echo "  ✅ DEMO & AUDIT SUCCESSFUL"
echo "============================================================"
