> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D'
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
> **Lien Miroir :** D / 03_C_MOTEURS_ET_DEPLOIEMENT
# MIROIR TEXTUEL - run_demo.sh

Source : MDL_Ynor_Framework\_08_EXPERIMENTS_AND_DEMOS\run_demo.sh
Taille : 1353 octets
SHA256 : 8fa0db87478039b515f03cd161b3d3d7a3ac4b2aed252d5dd8271a9deb584973

```text
#!/bin/bash
# MDL YNOR - DEMO RUNBOOK (v2.2.0-PROD) - UNIX VERSION (SH)

echo "============================================================"
echo " ⚡ MDL YNOR - AUTOMATED DEMO & validéTION ⚡"
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
06_D_PRIME_MIROIR_C_PRIME_VALIDATION_TESTS_DEMONSTRATION_IPYNB_161208.md
pip install -e .

# 3. ENVIRONMENT CHECK
if [ ! -f .env ]; then
 echo "[WARNING] No .env file found. Copying template..."
 cp .env.template .env
 echo "[ACTION] Please edit your .env file and add your API keys!"
fi

# 4. RUN validéTION
echo ""
echo "[1/3] RUNNING HARDCORE validéTION (MU MARGIN)..."
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
echo " ✅ DEMO & AUDIT SUCCESSFUL"
echo "============================================================"

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
