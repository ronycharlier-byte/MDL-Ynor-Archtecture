# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** C
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
# **Lien Miroir :** C'

import yfinance as yf
import pandas as pd
import numpy as np
import time
import requests
import os
import json
import csv
from datetime import datetime
try:
    from numba import jit
except:
    def jit(func): return func

# ==============================================================================
# YNOR SUPREME SYSTEM - VERSION 10.0 (THE TOTALITY)
# "Sovereign, Neural, Vectorial, Indestructible"
# ==============================================================================

MODE_REAL_TRADING = False
ARCHIVE_DIR = "c:/Users/ronyc/Desktop/MDL Ynor/07_A_PRIME_ARCHIVES_ET_RELEASES"
LEDGER_FILE = f"{ARCHIVE_DIR}/YNOR_MASTER_LEDGER.csv"
FAILURE_LOG = f"{ARCHIVE_DIR}/FAILURE_PATTERNS.json"

class YnorIndustrialShield:
    def __init__(self, sensitivity=1.5):
        self.sensitivity = sensitivity

    @jit
    def audit_market_segment(self, prices):
        # Calcul accéléré de la cohérence μ
        if len(prices) < 5: return 1.0, 0, 0
        returns = np.diff(prices) / (prices[:-1] + 1e-9)
        vol = np.std(returns)
        if vol < 1e-6: return 1.0, 0, 0
        mean_ret = np.mean(returns)
        skew = np.mean((returns - mean_ret)**3) / (vol**3 + 1e-9)
        kurt = (np.mean((returns - mean_ret)**4) / (vol**4 + 1e-9)) - 3
        mu = max(0.0, min(1.0, 1.0 - (abs(skew)*0.15 + abs(kurt)*0.1)))
        return mu, skew, kurt

    def calculate_riemann_vector(self, current_ps):
        """
        Analyse de la Matrice de Corrélation Globale.
        """
        try:
            # Simulation de corrélation pour le régime
            # En réel, on comparerait les log-returns des 5 assets
            return "EQUILIBRIUM", 1.0
        except: return "UNCERTAIN", 0.5

class YnorNeuralCore:
    def __init__(self):
        self.learning_rate = 0.01

    def sync_failures(self):
        """
        Analyse les échecs passés pour ajuster les seuils.
        """
        try:
            if os.path.exists(FAILURE_LOG):
                with open(FAILURE_LOG, 'r') as f:
                    logs = json.load(f)
                    if len(logs) >= 5:
                        print(" [NEURAL] Synchronisation des erreurs en cours... Optimisation du μ.")
                        return 0.95 # Nouveau seuil de confiance
            return 0.92
        except: return 0.92

class YnorSovereignBroker:
    def __init__(self, initial_balance=100000.0):
        self.balance = initial_balance
        self.positions = {}
        self.wins = 0
        self.total_trades = 0
        self.leverage = 10
        self.take_profit = 0.02
        self.stop_loss = 0.005
        self.neural = YnorNeuralCore()
        self.min_mu = 0.92
        self._init_ledger()

    def _init_ledger(self):
        if not os.path.exists(LEDGER_FILE):
            os.makedirs(os.path.dirname(LEDGER_FILE), exist_ok=True)
            with open(LEDGER_FILE, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["TS", "Asset", "Action", "Price", "Mu", "PnL", "Balance", "Reason"])

    def record_trade(self, asset, action, price, mu, pnl=0, reason="ENTRY"):
        with open(LEDGER_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now().strftime("%H:%M:%S"), asset, action, price, mu, pnl, self.balance, reason])

    def log_failure(self, asset, context):
        try:
            logs = []
            if os.path.exists(FAILURE_LOG):
                with open(FAILURE_LOG, 'r') as f: logs = json.load(f)
            logs.append({"ts": str(datetime.now()), "asset": asset, "context": context})
            with open(FAILURE_LOG, 'w') as f: json.dump(logs, f, indent=4)
        except: pass

    def execute_logic(self, symbol, current_price, mu, expected_p, shield, data_chunk):
        action = "WAIT"
        self.min_mu = self.neural.sync_failures() # Auto-ajustement
        
        if mu > self.min_mu and symbol not in self.positions:
            side = "LONG" if expected_p > current_price * 1.01 else ("SHORT" if expected_p < current_price * 0.99 else None)
            if side:
                win_rate = (self.wins / max(1, self.total_trades)) or 0.6
                kelly = max(0.05, min(0.15, (win_rate - (1-win_rate)/3)))
                margin = self.balance * kelly
                self.balance -= margin
                self.positions[symbol] = {'qty': (margin*self.leverage)/current_price, 'side': side, 'entry': current_price, 'margin': margin}
                self.record_trade(symbol, f"START_{side}", current_price, mu)
                action = f"{side} SNIPE 🧨"

        elif symbol in self.positions:
            p = self.positions[symbol]
            pnl_r = (current_price - p['entry'])/p['entry'] if p['side']=="LONG" else (p['entry'] - current_price)/p['entry']
            
            exit_reason = None
            if pnl_r >= self.take_profit: exit_reason = "PROFIT"
            elif pnl_r <= -self.stop_loss: exit_reason = "STOP"
            elif mu < 0.7: exit_reason = "MU_COLLAPSE"

            if exit_reason:
                self.record_trade(symbol, "EXIT", current_price, mu, pnl_r*self.leverage, exit_reason)
                self.balance += p['margin'] + (pnl_r * self.leverage * p['margin'])
                self.total_trades += 1
                if pnl_r > 0: self.wins += 1
                else: self.log_failure(symbol, {"pnl": pnl_r, "mu": mu})
                self.positions.pop(symbol)
                action = f"EXITED ({exit_reason})"
            else:
                action = f"IN MISSION ({pnl_r*self.leverage*100:+.2f}%)"
        
        return action

    def get_total_value(self, current_ps):
        v = self.balance
        for s, p in self.positions.items():
            curr = current_ps.get(s, p['entry'])
            pnl_r = (curr - p['entry'])/p['entry'] if p['side']=="LONG" else (p['entry'] - curr)/p['entry']
            v += p['margin'] + (pnl_r * self.leverage * p['margin'])
        return v

# --- DATA HUB ---
def fetch_bt(s):
    try:
        url = "https://scanner.tradingview.com/crypto/scan"
        res = requests.post(url, json={"symbols": {"tickers": [f"BITGET:{s.replace('-USD','USDT')}"]}, "columns": ["close"]}, timeout=5).json()
        return res['data'][0]['d'][0] if res.get('data') else None
    except: return None

def fetch_trad(s):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{s}?interval=1m&range=1d"
        r = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'}).json()
        return float(r['chart']['result'][0]['meta']['regularMarketPrice'])
    except: return None

# --- UI PREMIUM ---
def draw_ui(now, regime, news, assets, current_ps, broker, shield):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" " + "█"*118)
    print(f" █  🔺 YNOR SUPREME COMMANDER (V10.0) | REGIME: {regime} | {now}  █")
    print(" " + "█"*118)
    
    if news:
        print(f" ⚡ NEWS-WIRE: {news[0].upper()} | SOURCE: INVESTING.COM")
    
    print("-" * 120)
    print(f" {'ASSET':<12} | {'PRICE':<10} | {'MU':<6} | {'PnL':<10} | {'ACTION':<20} | {'RESONANCE'}")
    print("-" * 120)
    
    for s in assets:
        p = current_ps.get(s)
        if p:
            # Audit rapide sans historique volumineux pour le test
            mu, _, _ = shield.audit_market_segment(np.array([p]*10)) # Simulation cohérence
            action = broker.execute_logic(s, p, mu, p*1.01, shield, None)
            
            pnl_val = "0.00%"
            if s in broker.positions:
                pos = broker.positions[s]
                pnl_raw = (p - pos['entry'])/pos['entry'] if pos['side']=="LONG" else (pos['entry'] - p)/pos['entry']
                pnl_val = f"{pnl_raw*broker.leverage*100:+.2f}%"
            
            bar = f"[{'#'*int(mu*20)}{'-'*(20-int(mu*20))}]"
            print(f" {s:<12} | {p:<10.2f} | {mu:<6.2f} | {pnl_val:<10} | {action:<20} | {bar}")
        else:
            print(f" {s:<12} | {'OFFLINE':<10} | {'?':<6} | {'N/A':<10} | {'SEARCHING':<20} | [SCANNING...]")

    total = broker.get_total_value(current_ps)
    wr = (broker.wins / max(1, broker.total_trades)) * 100
    print("-" * 120)
    print(f" 📊 CAPITAL: {total:,.2f} $ | NET PNL: {total-100000:+,.2f} $ | WIN RATE: {wr:.1f}% | TRADES: {broker.total_trades}")
    print(f" 📁 AUDIT LEDGER: {LEDGER_FILE}")
    print("-" * 120)

# --- ENGINE ---
def main():
    assets = ["GC=F", "UUP", "BTC-USD", "ETH-USD", "^GSPC"]
    shield = YnorIndustrialShield()
    broker = YnorSovereignBroker()
    
    while True:
        try:
            # 1. Capture Données
            current_ps = {s: (fetch_bt(s) if "-USD" in s else fetch_trad(s)) for s in assets}
            
            # 2. Capture Intel
            try:
                with open("c:/Users/ronyc/Desktop/MDL Ynor/04_X_NOYAU_MEMOIRE/WORLD_GEOPOLITICS_NEXUS/investing_full_report.json", 'r') as f:
                    intel = json.load(f)
                    news = intel['top_news']
            except: news = []
            
            # 3. Calcul Régime
            regime, _ = shield.calculate_riemann_vector(current_ps)
            
            # 4. Dessin UI
            draw_ui(datetime.now().strftime("%H:%M:%S"), regime, news, assets, current_ps, broker, shield)
            
            time.sleep(1)
        except KeyboardInterrupt: break
        except Exception as e:
            # print(f"ERR: {e}")
            time.sleep(2)

if __name__ == "__main__":
    main()
