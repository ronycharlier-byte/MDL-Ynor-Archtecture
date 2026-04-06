import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import ccxt
import pandas as pd
from dotenv import load_dotenv

from feature_engine import compute_market_features
from strategy_engine import load_strategy_profile, score_market


load_dotenv()


@dataclass
class BotConfig:
    api_key: str = field(default_factory=lambda: os.getenv("BITGET_API_KEY", "YOUR_API_KEY"))
    secret: str = field(default_factory=lambda: os.getenv("BITGET_SECRET", "YOUR_SECRET"))
    passphrase: str = field(default_factory=lambda: os.getenv("BITGET_PASSPHRASE", "YOUR_PASSPHRASE"))
    live_trading: bool = field(default_factory=lambda: os.getenv("LIVE_TRADING", "false").lower() == "true")
    margin_mode: str = "isolated"
    default_type: str = "spot"


@dataclass
class BotState:
    symbols: List[str]
    positions: Dict[str, float] = field(default_factory=dict)
    entry_price: Dict[str, float] = field(default_factory=dict)
    peak_price: Dict[str, float] = field(default_factory=dict)
    last_action: str = "idle"
    last_error: str = ""

    def __post_init__(self) -> None:
        for symbol in self.symbols:
            self.positions.setdefault(symbol, 0.0)
            self.entry_price.setdefault(symbol, 0.0)
            self.peak_price.setdefault(symbol, 0.0)


@dataclass
class StrategyConfig:
    timeframe: str = "1m"
    breakout: Dict[str, float] = field(default_factory=lambda: {"BTC/USDT": 70000, "ETH/USDT": 2200})
    sweep: Dict[str, float] = field(default_factory=lambda: {"BTC/USDT": 65000, "ETH/USDT": 2000})
    usdt_per_trade: Dict[str, float] = field(default_factory=lambda: {"BTC/USDT": 50.0, "ETH/USDT": 25.0})
    profile_path: str = "03_C_MOTEURS_ET_DEPLOIEMENT/strategy_profile.json"


def create_exchange(config: BotConfig) -> ccxt.Exchange:
    return ccxt.bitget(
        {
            "apiKey": config.api_key,
            "secret": config.secret,
            "password": config.passphrase,
            "enableRateLimit": True,
            "options": {
                "defaultType": config.default_type,
            },
        }
    )


def fetch_ohlcv_df(exchange: ccxt.Exchange, symbol: str, timeframe: str, limit: int = 50) -> pd.DataFrame:
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    if not ohlcv:
        return pd.DataFrame()

    df = pd.DataFrame(ohlcv, columns=["time", "open", "high", "low", "close", "volume"])
    df["time"] = pd.to_datetime(df["time"], unit="ms")
    return df


def trailing_stop(state: BotState, symbol: str, price: float) -> Optional[float]:
    if state.positions[symbol] <= 0:
        return None

    state.peak_price[symbol] = max(state.peak_price[symbol], price)
    profit_run = state.peak_price[symbol] - state.entry_price[symbol]
    if profit_run <= 0:
        return None

    return state.entry_price[symbol] + profit_run * 0.5


def _market_buy(
    exchange: ccxt.Exchange,
    state: BotState,
    strategy: StrategyConfig,
    config: BotConfig,
    symbol: str,
    price: float,
) -> str:
    quote_amount = strategy.usdt_per_trade[symbol]
    base_amount = quote_amount / price
    base_amount = float(exchange.amount_to_precision(symbol, base_amount))

    if base_amount <= 0:
        return f"[BUY] {symbol}: amount invalide"

    params = {"marginMode": config.margin_mode}

    if config.live_trading:
        order = exchange.create_order(symbol, "market", "buy", base_amount, None, params)
        message = f"[BUY] {symbol} order_id={order.get('id')} amount={base_amount}"
    else:
        message = f"[DRY RUN BUY] {symbol} amount={base_amount} marginMode={config.margin_mode}"

    state.positions[symbol] = base_amount
    state.entry_price[symbol] = price
    state.peak_price[symbol] = price
    state.last_action = message
    return message


def _market_sell(
    exchange: ccxt.Exchange,
    state: BotState,
    config: BotConfig,
    symbol: str,
    amount: float,
    price: float,
) -> str:
    amount = float(exchange.amount_to_precision(symbol, amount))
    if amount <= 0:
        return f"[SELL] {symbol}: amount invalide"

    params = {"marginMode": config.margin_mode}

    if config.live_trading:
        order = exchange.create_order(symbol, "market", "sell", amount, None, params)
        message = f"[SELL] {symbol} order_id={order.get('id')} amount={amount}"
    else:
        message = f"[DRY RUN SELL] {symbol} amount={amount} marginMode={config.margin_mode}"

    state.positions[symbol] = 0.0
    state.entry_price[symbol] = 0.0
    state.peak_price[symbol] = 0.0
    state.last_action = f"{message} | exit @ {price}"
    return message


def check_signals(
    exchange: ccxt.Exchange,
    state: BotState,
    strategy: StrategyConfig,
    config: BotConfig,
    symbol: str,
    df: pd.DataFrame,
) -> Tuple[List[str], Optional[dict]]:
    events: List[str] = []
    snapshot: Optional[dict] = None

    if df.empty:
        event = f"[INFO] Aucune donnée pour {symbol}"
        state.last_action = event
        return [event], snapshot

    last = df.iloc[-1]
    price = float(last["close"])
    low = float(last["low"])
    trail = None

    features = compute_market_features(df)
    profile = load_strategy_profile(strategy.profile_path)
    quant_view = score_market(features, profile) if features else {"score": 0.0, "decision": "hold", "components": {}}

    if state.positions[symbol] == 0.0:
        if features and quant_view["decision"] == "buy":
            events.append(_market_buy(exchange, state, strategy, config, symbol, price))
        elif not features and price > strategy.breakout[symbol]:
            events.append(_market_buy(exchange, state, strategy, config, symbol, price))
        elif not features and low < strategy.sweep[symbol] and price > strategy.sweep[symbol]:
            events.append(_market_buy(exchange, state, strategy, config, symbol, price))
        else:
            state.last_action = f"[HOLD] {symbol} score={quant_view['score']:.2f}"
            events.append(state.last_action)
    else:
        trail = trailing_stop(state, symbol, price)
        if features and quant_view["decision"] == "sell":
            events.append(_market_sell(exchange, state, config, symbol, state.positions[symbol], price))
        elif trail is not None and price < trail:
            events.append(_market_sell(exchange, state, config, symbol, state.positions[symbol], price))
        else:
            state.last_action = f"[HOLD] {symbol} price={price} trail={trail} score={quant_view['score']:.2f}"
            events.append(state.last_action)

    snapshot = {
        "symbol": symbol,
        "price": price,
        "low": low,
        "trail": trail,
        "position": state.positions[symbol],
        "entry_price": state.entry_price[symbol],
        "peak_price": state.peak_price[symbol],
        "breakout": strategy.breakout[symbol],
        "sweep": strategy.sweep[symbol],
        "score": quant_view["score"],
        "decision": quant_view["decision"],
    }
    return events, snapshot
