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
# MDL YNOR - BITGET PASSIVE AUDIT V1.4
# Confrontation du Quotient q à la Réalité de Marché
# =================================================================================

class YnorObserver(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.Tanh(),
            nn.Linear(32, 16)
        )
        
    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, torch.Tensor]:
        features = self.backbone(x)
        sigma = torch.norm(features[:, :8], dim=1)
        theta_raw = features[:, 8:]
        theta = theta_raw / (torch.norm(theta_raw, dim=1, keepdim=True) + 1e-6)
        return sigma, theta

def get_psi_reg_real(prices: list, imbalance: float) -> float:
    """
    Polarité de Régime Réelle (ψ_reg)
    Orientée par le Trend (dx/dt) et la Pression Orderbook (P).
    """
    if len(prices) < 2: return 0.0
    dx_dt = (prices[-1] - prices[-2]) / prices[-2]
    # Sentiment : Combinaison de la dynamique de prix et du carnet d'ordre
    sentiment = dx_dt * 1000 + (imbalance - 1.0)
    return 1.0 if sentiment > 0 else -1.0

def run_bitget_audit():
    print("--- MDL YNOR : DEMARRAGE AUDIT BITGET (CONFRONTATION) ---")
    exchange = ccxt.bitget()
    
    # 1. Chargement de la structure géométrique q (V1.4)
    input_dim = 64
    observer = YnorObserver(input_dim)
    try:
        observer.load_state_dict(torch.load("ynor_observer_v1_4.pth"))
        observer.eval()
        print("[SOUVERAIN] Quotient q V1.4 charge avec succes.")
    except:
        print("[ERCH] Échec du chargement du modele q. Signature brute utilisee.")

    symbol = "BTC/USDT"
    phi_history = []
    prices_history = []
    
    print(f"\n[SCAN] Debut du tracking structurel sur {symbol}...")
    
    for i in range(10): # 10 scans pour demo (Phase 1: 24-72h prevue)
        try:
            # A. Ingestion X_real (Vecteur de 64 dimensions)
            ticker = exchange.fetch_ticker(symbol)
            ob = exchange.fetch_order_book(symbol, limit=20)
            
            last_price = ticker['last']
            prices_history.append(last_price)
            if len(prices_history) > 20: prices_history.pop(0)
            
            imbalance = sum([b[1] for b in ob['bids']]) / sum([a[1] for a in ob['asks']])
            
            # Reconstruction du vecteur d'état x(t)
            x_t = np.zeros(64)
            x_t[0] = last_price / 70000.0 # Normalisation arbitraire pour l'observer
            x_t[1] = imbalance
            x_t[2] = (last_price - prices_history[0]) / prices_history[0] if len(prices_history) > 1 else 0
            # Padding avec bruit blanc (entropy conforme à X_test)
            x_t[3:] = np.random.randn(61) * 0.1
            
            x_tensor = torch.FloatTensor(x_t).unsqueeze(0)
            
            # B. Calcul de la Projection Phi'
            with torch.no_grad():
                sigma, theta = observer(x_tensor)
                psi = get_psi_reg_real(prices_history, imbalance)
                
                # Signature Phi' = (sigma, Theta, psi)
                # On arrondit pour detecter les transitions discrétisées
                phi_current = (torch.cat([sigma.unsqueeze(1), theta, torch.tensor([[psi]])], dim=1) * 5).round() / 5
            
            # C. Tracking des Transitions
            status = "STABLE"
            if len(phi_history) > 0:
                if not torch.equal(phi_current, phi_history[-1]):
                    status = "TRANSITION DETECTEE"
            
            phi_history.append(phi_current)
            
            print(f"[AUDIT {i:02d}] Price: {last_price} | Imb: {imbalance:.2f} | Status: {status}")
            print(f"  > Signature Phi': {phi_current[0, :3].tolist()}... [psi: {psi}]")
            
            time.sleep(3) # Throttle pour l'API
            
        except Exception as e:
            print(f"[ERROR] Scan failed: {e}")
            break

    print("\n--- SYNTHESE PRELIMINAIRE ---")
    transitions = sum([1 for i in range(1, len(phi_history)) if not torch.equal(phi_history[i], phi_history[i-1])])
    print(f"Total Scans: {len(phi_history)} | Transitions: {transitions}")
    print("[SYSTEM] Fin de l'audit de confrontation initiale.")

if __name__ == "__main__":
    run_bitget_audit()
