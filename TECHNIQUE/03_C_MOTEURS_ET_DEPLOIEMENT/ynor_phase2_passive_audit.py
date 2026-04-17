# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** C
# **Rôle du Fichier :** Audit structurel et controle d'integrite
# **Centre Doctrinal Local :** AI Manager garde audit structurel et controle d'integrite en limitant le bruit local et la friction structurelle.
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

# =================================================================================
# MDL YNOR - PHASE 2 : PASSIVE REAL-WORLD AUDIT (24-72H)
# Objectif : Mesurer epsilon_q_real et la Stabilité Hors-Distribution
# =================================================================================

class YnorObserver(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.Tanh(),
            nn.Linear(32, 16)
        )
        
    def forward(self, x: torch.Tensor):
        features = self.backbone(x)
        sigma = torch.norm(features[:, :8], dim=1)
        theta_raw = features[:, 8:]
        theta = theta_raw / (torch.norm(theta_raw, dim=1, keepdim=True) + 1e-6)
        return sigma, theta

def get_psi_reg_real(prices: list, imbalance: float) -> int:
    """ Polarité Directionnelle active """
    if len(prices) < 2: return 0
    dx_dt = (prices[-1] - prices[-2]) / prices[-2]
    sentiment = dx_dt * 1000 + (imbalance - 1.0)
    return 1 if sentiment > 0.05 else (-1 if sentiment < -0.05 else 0)

async def start_phase2_worker(duration_hours=24):
    exchange = ccxt.bitget()
    
    # 1. Chargement Structurel (V1.4)
    observer = YnorObserver(64)
    try:
        observer.load_state_dict(torch.load("ynor_observer_v1_4.pth"))
        observer.eval()
        print("[SOUVERAIN] Moteur q V1.4 pret pour Phase 2.")
    except:
        print("[ERROR] Échec chargement q. Audit compromis.")
        return

    symbol = "BTC/USDT"
    log_file = f"ynor_passive_audit_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jsonl"
    
    # Historique pour evaluation post-scan
    history = [] 
    avg_x = None # Moving centroid for OOD detection
    
    print(f"\n[PHASE 2] Lancement de l'audit long-terme sur {symbol}...")
    print(f"[LOG] Fichier : {log_file}")
    
    while True:
        try:
            ticker = exchange.fetch_ticker(symbol)
            price = ticker['last']
            ob = exchange.fetch_order_book(symbol, limit=20)
            imb = sum([b[1] for b in ob['bids']]) / sum([a[1] for a in ob['asks']])
            
            # Vecteur d'état x(t)
            prices = [h['price'] for h in history[-20:]] + [price]
            x_t = np.zeros(64)
            x_t[0] = price / 70000.0
            x_t[1] = imb
            x_t[2] = (price - prices[0]) / prices[0] if len(prices) > 1 else 0
            x_t[3:] = np.random.randn(61) * 0.1 # Entropy conforme
            
            x_tensor = torch.FloatTensor(x_t).unsqueeze(0)
            
            # --- DETECTEUR OOD (Strangeness Score) ---
            if avg_x is None: avg_x = x_tensor
            else: avg_x = 0.99 * avg_x + 0.01 * x_tensor
            strangeness = torch.norm(x_tensor - avg_x).item()

            with torch.no_grad():
                sigma, theta = observer(x_tensor)
                psi = get_psi_reg_real(prices, imb)
                phi = (torch.cat([sigma.unsqueeze(1), theta, torch.tensor([[psi]])], dim=1) * 5).round() / 5
            
            # --- EVALUATION DE LA VERITE TERRAIN (t+60s) ---
            now = time.time()
            for h in history:
                if not h['validated'] and (now - h['timestamp'] > 60):
                    move = (price - h['price']) / h['price']
                    h['correct'] = (h['psi'] == 1 and move > 0) or (h['psi'] == -1 and move < 0) or (h['psi'] == 0)
                    h['validated'] = True
                    h['real_move'] = move
            
            entry = {
                "timestamp": now,
                "price": price,
                "phi": phi[0].tolist(),
                "psi": int(psi),
                "imb": round(imb, 4),
                "strangeness": round(strangeness, 4),
                "validated": False,
                "correct": None
            }
            history.append(entry)
            if len(history) > 1000: history.pop(0)
            
            with open(log_file, "a") as f:
                f.write(json.dumps(entry) + "\n")
            
            validated_entries = [h for h in history if h['validated'] and h['psi'] != 0]
            epsilon_q_real = 1.0 - (sum([1 for h in validated_entries if h['correct']]) / len(validated_entries)) if validated_entries else 0.0
            
            # Alerte OOD si étrangeté > 2.0 (seuil arbitraire pour monitoring)
            ood_tag = " [OOD!]" if strangeness > 2.0 else ""
            print(f"[{datetime.now().strftime('%H:%M:%S')}] P: {price} | ψ: {psi:2d} | ε_q: {epsilon_q_real:.4f} | S: {strangeness:.2f}{ood_tag}", end="\r")
            
            time.sleep(3)
            
        except KeyboardInterrupt:
            print("\n[STOP] Audit Phase 2 interrompu par l'utilisateur.")
            break
        except Exception as e:
            print(f"\n[ERROR] API/Cycle failed: {e}")
            time.sleep(10)

if __name__ == "__main__":
    import asyncio
    asyncio.run(start_phase2_worker())
