import os
import sys
from datetime import datetime

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

sys.path.append(os.path.abspath("."))
sys.path.append(os.path.abspath("./03_C_MOTEURS_ET_DEPLOIEMENT"))

from bitget_bot_core import BotConfig, BotState, StrategyConfig, check_signals, create_exchange, default_symbols, prepare_exchange, fetch_ohlcv_df


st.set_page_config(page_title="Bitget Margin Isolée", layout="wide")


def init_state() -> None:
 if "symbols" not in st.session_state:
 st.session_state.symbols = default_symbols(os.getenv("DEFAULT_TYPE", "swap"))
 if "bot_state" not in st.session_state:
 st.session_state.bot_state = BotState(st.session_state.symbols)
 if "strategy" not in st.session_state:
 st.session_state.strategy = StrategyConfig()
 if "last_scan" not in st.session_state:
 st.session_state.last_scan = None
 if "logs" not in st.session_state:
 st.session_state.logs = []
 if "bot_running" not in st.session_state:
 st.session_state.bot_running = False
 if "last_scan_at" not in st.session_state:
 st.session_state.last_scan_at = None


def log(message: str) -> None:
 stamp = datetime.now().strftime("%H:%M:%S")
 st.session_state.logs.insert(0, f"[{stamp}] {message}")
 st.session_state.logs = st.session_state.logs[:12]


def as_bool(label: str, default: bool) -> bool:
 return st.sidebar.checkbox(label, value=default)


init_state()

st.markdown(
 """
 <style>
 .block-container { padding-top: 1.5rem; padding-bottom: 2rem; }
 .title-line { font-size: 2.4rem; font-weight: 800; letter-spacing: -0.04em; margin-bottom: 0.25rem; }
 .subtitle { color: rgba(255,255,255,0.72); margin-bottom: 1rem; }
 .status-good { color: #7CFF9B; font-weight: 700; }
 .status-warn { color: #FFCC66; font-weight: 700; }
 .status-bad { color: #FF6B6B; font-weight: 700; }
 </style>
 """,
 unsafe_allow_html=True,
)

st.markdown('<div class="title-line">Bitget Margin Isolée</div>', unsafe_allow_html=True)
st.markdown(
 '<div class="subtitle">Tableau de bord opérationnel pour scanner le marché, surveiller les positions et sécuriser le mode live.</div>',
 unsafe_allow_html=True,
)

with st.sidebar:
 st.header("Connexion")
 api_key = st.text_input("API Key", value=os.getenv("BITGET_API_KEY", ""), type="password")
 secret = st.text_input("Secret", value=os.getenv("BITGET_SECRET", ""), type="password")
 passphrase = st.text_input("Passphrase", value=os.getenv("BITGET_PASSPHRASE", ""), type="password")
 live_trading = as_bool("LIVE_TRADING", os.getenv("LIVE_TRADING", "false").lower() == "true")
 live_confirmed = as_bool("LIVE_CONFIRMED", os.getenv("LIVE_CONFIRMED", "false").lower() == "true")
 max_usdt_per_trade = st.number_input("Max USDT/order", value=float(os.getenv("MAX_USDT_PER_TRADE", "10")))
 leverage = st.number_input("Leverage", value=float(os.getenv("LEVERAGE", "1")))
 default_type = st.selectbox("Type de marché", ["spot", "swap"], index=1 if os.getenv("DEFAULT_TYPE", "swap") == "swap" else 0)
 margin_mode = st.selectbox("Margin mode", ["isolated", "cross"], index=0)

 st.header("Stratégie")
 timeframe = st.selectbox("Timeframe", ["1m", "5m", "15m"], index=0)
 symbol_options = ["BTC/USDT:USDT"] if default_type == "swap" else ["BTC/USDT", "ETH/USDT"]
 selected_symbols = st.multiselect(
 "Symbols",
 symbol_options,
 default=st.session_state.symbols if st.session_state.symbols else symbol_options,
 )
 breakout_btc = st.number_input("BTC breakout", value=float(st.session_state.strategy.breakout["BTC/USDT:USDT" if default_type == "swap" else "BTC/USDT"]))
 sweep_btc = st.number_input("BTC sweep", value=float(st.session_state.strategy.sweep["BTC/USDT:USDT" if default_type == "swap" else "BTC/USDT"]))
 breakout_eth = st.number_input("ETH breakout", value=float(st.session_state.strategy.breakout.get("ETH/USDT", 2200)))
 sweep_eth = st.number_input("ETH sweep", value=float(st.session_state.strategy.sweep.get("ETH/USDT", 2000)))
 usdt_btc = st.number_input("BTC USDT/trade", value=float(st.session_state.strategy.usdt_per_trade["BTC/USDT:USDT" if default_type == "swap" else "BTC/USDT"]))
 usdt_eth = st.number_input("ETH USDT/trade", value=float(st.session_state.strategy.usdt_per_trade.get("ETH/USDT", 25.0)))
 profile_path = st.text_input("Strategy profile", value=st.session_state.strategy.profile_path)

 st.header("Contrôle")
 col_a, col_b = st.columns(2)
 start_button = col_a.button("Start", type="primary", use_container_width=True)
 stop_button = col_b.button("Stop", use_container_width=True)
 scan_button = st.button("Run scan once", use_container_width=True)
 reset_button = st.button("Reset state", use_container_width=True)

if selected_symbols:
 if selected_symbols != st.session_state.symbols:
 st.session_state.symbols = selected_symbols
 st.session_state.bot_state = BotState(st.session_state.symbols)
else:
 st.session_state.symbols = symbol_options[:1]
 st.session_state.bot_state = BotState(st.session_state.symbols)

st.session_state.strategy = StrategyConfig(
 timeframe=timeframe,
 breakout={"BTC/USDT": breakout_btc, "BTC/USDT:USDT": breakout_btc, "ETH/USDT": breakout_eth},
 sweep={"BTC/USDT": sweep_btc, "BTC/USDT:USDT": sweep_btc, "ETH/USDT": sweep_eth},
 usdt_per_trade={"BTC/USDT": usdt_btc, "BTC/USDT:USDT": usdt_btc, "ETH/USDT": usdt_eth},
 profile_path=profile_path,
)

if reset_button:
 st.session_state.bot_state = BotState(st.session_state.symbols)
 st.session_state.logs = []
 st.session_state.last_scan = None
 st.session_state.last_scan_at = None
 st.session_state.bot_running = False
 log("State reset")

if start_button:
 st.session_state.bot_running = True
 log("Bot started")

if stop_button:
 st.session_state.bot_running = False
 log("Bot stopped")

config = BotConfig(
 api_key=api_key,
 secret=secret,
 passphrase=passphrase,
 live_trading=live_trading,
 live_confirmed=live_confirmed,
 margin_mode=margin_mode,
 default_type=default_type,
 max_usdt_per_trade=max_usdt_per_trade,
 leverage=leverage,
)

if not api_key or not secret or not passphrase:
 st.warning("Renseigne les clés Bitget avant d'activer le live.")

status_col1, status_col2, status_col3, status_col4 = st.columns(4)
status_col1.metric("Mode", "LIVE" if live_trading else "DRY RUN")
status_col2.metric("Market", default_type)
status_col3.metric("Margin", margin_mode)
status_col4.metric("State", "RUNNING" if st.session_state.bot_running else "STOPPED")

profile_col1, profile_col2, profile_col3 = st.columns(3)
profile_col1.markdown(f"**Strategy profile:** `{st.session_state.strategy.profile_path}`")
profile_col2.markdown("**Quant engine:** `enabled`")
profile_col3.markdown(f"**Live confirmed:** `{'yes' if live_confirmed else 'no'}`")

try:
 exchange = create_exchange(config)
 exchange.load_markets()
 for symbol in st.session_state.symbols:
 prepare_exchange(exchange, config, symbol)
 exchange_ready = True
except Exception as exc:
 exchange_ready = False
 st.error(f"Impossible de préparer l'échange Bitget: {exc}")
 exchange = None

if scan_button and exchange_ready:
 st.session_state.last_scan_at = datetime.now()
 snapshots = []
 for symbol in st.session_state.symbols:
 try:
 df = fetch_ohlcv_df(exchange, symbol, st.session_state.strategy.timeframe, limit=50)
 events, snapshot = check_signals(
 exchange,
 st.session_state.bot_state,
 st.session_state.strategy,
 config,
 symbol,
 df,
 )
 for event in events:
 log(event)
 if snapshot:
 snapshots.append(snapshot)
 except Exception as exc:
 message = f"[ERROR] {symbol}: {exc}"
 st.session_state.bot_state.last_error = message
 log(message)

 st.session_state.last_scan = {
 "at": datetime.now(),
 "snapshots": snapshots,
 }

if st.session_state.bot_running and exchange_ready:
 st.session_state.last_scan_at = datetime.now()
 snapshots = []
 for symbol in st.session_state.symbols:
 try:
 df = fetch_ohlcv_df(exchange, symbol, st.session_state.strategy.timeframe, limit=50)
 events, snapshot = check_signals(
 exchange,
 st.session_state.bot_state,
 st.session_state.strategy,
 config,
 symbol,
 df,
 )
 for event in events:
 log(event)
 if snapshot:
 snapshots.append(snapshot)
 except Exception as exc:
 message = f"[ERROR] {symbol}: {exc}"
 st.session_state.bot_state.last_error = message
 log(message)

 st.session_state.last_scan = {
 "at": datetime.now(),
 "snapshots": snapshots,
 }

 components.html(
 "<script>setTimeout(() => window.location.reload(), 60000);</script>",
 height=0,
 )

left, right = st.columns([1.2, 0.8])

with left:
 st.subheader("État du bot")
 if st.session_state.last_scan and st.session_state.last_scan["snapshots"]:
 latest = pd.DataFrame(st.session_state.last_scan["snapshots"])
 st.dataframe(latest, use_container_width=True, hide_index=True)
 else:
 st.info("Lance un scan pour voir le dernier snapshot de marché.")

 st.subheader("Positions")
 positions_df = pd.DataFrame(
 [
 {
 "symbol": s,
 "position": st.session_state.bot_state.positions.get(s, 0.0),
 "entry_price": st.session_state.bot_state.entry_price.get(s, 0.0),
 "peak_price": st.session_state.bot_state.peak_price.get(s, 0.0),
 }
 for s in st.session_state.symbols
 ]
 )
 st.dataframe(positions_df, use_container_width=True, hide_index=True)

with right:
 st.subheader("Logs")
 if st.session_state.logs:
 st.code("\n".join(st.session_state.logs), language="text")
 else:
 st.caption("Aucun événement pour l'instant.")

 st.subheader("Sécurité")
 if live_trading:
 st.markdown('<div class="status-bad">LIVE_TRADING activé</div>', unsafe_allow_html=True)
 else:
 st.markdown('<div class="status-good">Dry run actif</div>', unsafe_allow_html=True)

 st.subheader("Run")
 st.write("Dernier scan:", st.session_state.last_scan_at or "jamais")

 if st.session_state.bot_state.last_error:
 st.error(st.session_state.bot_state.last_error)
