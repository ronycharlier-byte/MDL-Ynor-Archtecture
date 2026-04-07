---
STATUS: CANONICAL | V11.14.0 | ENGINE: BITGET | STABILITY: 0.9994
---

# 🤖 BITGET TRADING ENGINE - SPÉCIFICATIONS

## 🎯 Vision
Le moteur de trading **Bitget Ynor** est conçu comme une extension d'exécution du noyau chiaste. Il convertit les vagues de résonance fractale en ordres de marché précis sur les paires de haute liquidité (BTC/ETH).

---

## 🏛️ Architecture du Moteur

### 1. Noyau Logique (`bitget_bot_core.py`)
- **Gestion des Échanges** : Interface CCXT unifiée pour Bitget.
- **Télémétrie OHLCV** : Extraction et normalisation des flux temporels.
- **Logique de Signal** :
    - **Breakout** : Détection des franchissements de niveaux critiques.
    - **Sweep** : Identification des chasses aux liquidités.
- **Protocole de Sortie** : Stop-loss suiveur (Trailing Stop) dynamique.

### 2. Automate d'Exécution (`bitget_market_bot.py`)
- Boucle de surveillance temps-réel.
- Gestion multi-devises (BTC & ETH par défaut).
- Système de journalisation des événements et des erreurs.

### 3. Interface de Pilotage (`bitget_dashboard.py`)
- Visualisation Streamlit.
- Monitoring des positions ouvertes, des PnL latents et des seuils de déclenchement.

---

## ⚙️ Configuration Stratégique

| Paramètre | Valeur par défaut | Description |
| :--- | :--- | :--- |
| **Timeframe** | `1m` | Analyse ultra-court terme pour précision maximale. |
| **Breakout BTC** | `70,000 USDT` | Seuil de confirmation de tendance haussière. |
| **Sweep BTC** | `65,000 USDT` | Seuil de détection de déviation structurelle. |
| **Exposure** | `$50 / trade` | Allocation de risque conservatrice par défaut. |

---

## 🛡️ Protocoles de Sécurité
- **Dry Run Mode** : Activé par défaut pour valider les signaux sans risque capital.
- **Isolation de Marge** : Utilisation exclusive du mode `isolated` pour protéger le solde global.
- **Whitelist IP** : Obligation de lier l'API key à l'IP publique du VPS souverain.

---

## 🚀 Guide de Surveillance
Pour monitorer l'automate en production :
1. Se connecter au VPS.
2. Lancer le dashboard : `streamlit run 03_C_MOTEURS_ET_DEPLOIEMENT/bitget_dashboard.py`.
3. Vérifier les logs : `tail -f bitget_bot.log`.

---
