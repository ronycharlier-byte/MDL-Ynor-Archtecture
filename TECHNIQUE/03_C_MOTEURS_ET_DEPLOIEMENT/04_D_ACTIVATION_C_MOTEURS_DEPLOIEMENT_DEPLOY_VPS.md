> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** D
> **Role du Fichier :** Procedure VPS de deploiement
> **Centre Doctrinal Local :** mise en service et configuration VPS
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** mise en service et configuration VPS
> - **β :** configuration divergente
> - **κ :** cout d execution
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** D' / 05_C_PRIME_VALIDATION_ET_TESTS
# VPS Deployment Guide

This project can run on a small Ubuntu VPS with a fixed public IPv4.

## 1. System setup

You can run the automation script instead of typing everything manually:

```bash
cd /opt/FRACTAL_CHIASTE
bash 03_C_MOTEURS_ET_DEPLOIEMENT/install_vps.sh
```

The script will prompt for:

- repository URL
- Bitget API key
- Bitget caractéristique systémique
- Bitget passphrase
- swap/spot mode
- whether to enable live trading

If you prefer the manual steps, keep reading.

```bash
sudo apt update
sudo apt install -y git python3 python3-venv python3-pip
```

## 2. Clone the repository

```bash
git clone <your-repo-url>
cd FRACTAL_CHIASTE
```

## 3. Create the virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
04_D_ACTIVATION_03_C_MOTEURS_DEPLOIEMENT_NOEUD_ORCHESTRATION_MOTEUR_DEPLOIEMENT_03_C_MOTEURS_DEPLOIEMENT.md
```

## 4. Configure environment variables

```bash
cp 03_C_MOTEURS_ET_DEPLOIEMENT/.env.example .env
nano .env
```

Fill in:

- `BITGET_API_KEY`
- `BITGET_node_key`
- `BITGET_PASSPHRASE`
- `DEFAULT_TYPE=swap` for futures
- `LEVERAGE=1` for a first test
- `LIVE_TRADING=false` for testing first

The VPS installer now uses `03_C_MOTEURS_ET_DEPLOIEMENT/requirements-bitget.txt`, which keeps the Python install minimal.

## 5. Whitelist the VPS IP in Bitget

Use the VPS public IPv4 only, for example `123.123.123.123`.

Do not paste CIDR ranges such as `74.220.48.0/24`.

## 6. Test the dashboard

```bash
streamlit run 03_C_MOTEURS_ET_DEPLOIEMENT/bitget_dashboard.py --server.address 0.0.0.0 --server.port 8501
```

For a swap test, choose:

- `Type de marché = swap`
- `Margin mode = isolated`
- `Symbols = BTC/USDT:USDT`
- `Max USDT/order = 10` or lower
- `Leverage = 1`

## 7. Run the bot

```bash
python 03_C_MOTEURS_ET_DEPLOIEMENT/bitget_market_bot.py
```

## 8. Switch to live trading

After the dry run is validéted, set:

```bash
sed -i 's/LIVE_TRADING=false/LIVE_TRADING=true/' .env
```

Then restart the bot service:

```bash
sudo systemctl restart bitget-bot.service
```

## 9. Suggested process model

- Use `systemd` for the bot process.
- Run the dashboard separately.
- Keep the bot and UI in the same repository but not in the same process in production.


---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
