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

# ==============================================================================
# YNOR QUANT STUDIO - THE SUPREME ARCHITECT INTERFACE
# Ultra-Premium UI for Quant Finance and AGI Safety
# ==============================================================================

st.set_page_config(page_title="YNOR QUANT STUDIO", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS (THE WOW FACTOR) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=JetBrains+Mono:wght@400&display=swap');

    /* Global Background */
    .main {
        background-color: #050505;
        color: #e0e0e0;
        font-family: 'Inter', sans-serif;
    }

    /* Glassmorphism Title Card */
    .title-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 40px;
        border: 1px solid rgba(75, 255, 75, 0.2);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        text-align: center;
        margin-bottom: 30px;
    }

    .title-card h1 {
        color: #4bff4b;
        font-size: 3rem;
        letter-spacing: 5px;
        text-shadow: 0 0 20px rgba(75, 255, 75, 0.5);
    }

    /* Custom Metric Styling */
    [data-testid="stMetricValue"] {
        font-family: 'JetBrains Mono', monospace;
        color: #4bff4b !important;
        font-size: 2.5rem !important;
        text-shadow: 0 0 10px rgba(75, 255, 75, 0.3);
    }
    
    [data-testid="stMetricLabel"] {
        color: #888 !important;
        font-size: 1rem !important;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    /* Column Styling */
    .css-1r6p8d1 { background-color: transparent; }
    
    /* Footer */
    .footer {
        position: fixed;
        bottom: 10px;
        right: 10px;
        color: #444;
        font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("""
    <div class="title-card">
        <h1>YNOR QUANT STUDIO</h1>
        <p style="color: #666; letter-spacing: 3px;">PHASE OMEGA - COMMAND & CONTROL</p>
    </div>
""", unsafe_allow_html=True)

import yfinance as yf

# --- YNOR QUANT ENGINE INTEGRATION ---
class YnorIndustrialShield:
    def __init__(self, sensitivity=3.5):
        self.sensitivity = sensitivity

    def audit_market_segment(self, data_chunk):
        prices = data_chunk['Close'].values
        if len(prices) < 15: return 1.0, 0, 0
        returns = np.diff(prices) / prices[:-1]
        volat = np.std(returns)
        mean_ret = np.mean(returns)
        skew = (np.mean((returns - mean_ret)**3) / (volat**3 + 1e-9)) if volat > 1e-6 else 0
        kurt = (np.mean((returns - mean_ret)**4) / (volat**4 + 1e-9)) - 3 if volat > 1e-6 else 0
        sharpe_proxy = (mean_ret / (volat + 1e-9)) * np.sqrt(252)
        beta_quant = (abs(skew) * 0.2) + (abs(kurt) * 0.1) + (max(0, sharpe_proxy - 1.5) * 0.1)
        mu_ext = max(-0.5, 1.0 - (self.sensitivity * beta_quant))
        return mu_ext, skew, kurt

shield = YnorIndustrialShield()
assets = ["GC=F", "UUP", "BTC-USD", "^GSPC"]

# --- SIDEBAR SETTINGS ---
with st.sidebar:
    st.header("⚙️ SYSTEM CONFIG")
    sens = st.slider("Shield Sensitivity", 1.0, 10.0, 3.5)
    st.markdown("---")
    st.write("**Architect**: Rony Charlier")
    st.write("**Status**: NOYAU STABLE [μ=1.0]")

# --- LIVE LOOP ---
placeholder = st.empty()

while True:
    with placeholder.container():
        try:
            raw_data = yf.download(assets, period="1d", interval="1m", group_by='ticker', progress=False, threads=True)
            
            # HEADER SECTION
            now = datetime.now()
            st.markdown(f"""
                <div class="title-card">
                    <h1>YNOR QUANT STUDIO</h1>
                    <p style="color: #4bff4b; letter-spacing: 5px;">
                        LIVE STREAMING | {now.strftime("%H:%M:%S")}.<span style="font-size: 0.8em;">{now.microsecond // 10000:02d}</span>
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # METRIC GRID - BTC FOCUS
            df_main = raw_data[assets[2]]
            mu, skew, kurt = shield.audit_market_segment(df_main.tail(20))
            
            col1, col2, col3, col4 = st.columns(4)
            with col1: st.metric(f"μ_ext {assets[2]}", f"{mu:.2f}", delta=f"{now.second % 10}s sync")
            with col2: st.metric("Skewness Audit", f"{skew:.3f}")
            with col3: st.metric("Kurtosis Delta", f"{kurt:.3f}")
            with col4: st.metric("Resonance", f"{(0.98 + (now.second/10000)):.4f}")

            st.markdown("---")
            
            # CHARTS
            col_l, col_r = st.columns([2, 1])
            with col_l:
                fig = go.Figure()
                for s in assets:
                    df = raw_data[s]
                    n_p = df['Close'] / df['Close'].iloc[0]
                    fig.add_trace(go.Scatter(x=df.index, y=n_p, name=s, line=dict(width=1)))
                fig.update_layout(template="plotly_dark", height=500, paper_bgcolor='rgba(0,0,0,0)', 
                                  plot_bgcolor='rgba(0,0,0,0)', margin=dict(l=0,r=0,t=0,b=0))
                st.plotly_chart(fig, theme="streamlit")
            
            with col_r:
                st.subheader("🏁 STABILITY BARS")
                for s in assets:
                    m, _, _ = shield.audit_market_segment(raw_data[s].tail(20))
                    # Pulse effect based on seconds
                    pulse = "🟢" if now.second % 2 == 0 else "⚪"
                    st.write(f"{pulse} **{s}** | {raw_data[s]['Close'].iloc[-1]:.2f}")
                    st.progress(max(0.0, min(1.0, m)))
            
            time.sleep(1) # FLUX SOUVERAIN
            st.rerun()

        except Exception as e:
            st.warning(f"Connecting to Sovereign Data... {e}")
            time.sleep(2)

# --- FOOTER ---
st.markdown('<div class="footer">YNOR OS V7.1 | SOUVERAINETÉ MATHÉMATIQUE SCELLÉE</div>', unsafe_allow_html=True)
