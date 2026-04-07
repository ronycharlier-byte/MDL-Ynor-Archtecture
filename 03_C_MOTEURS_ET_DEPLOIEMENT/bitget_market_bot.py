import os
import time

from bitget_bot_core import BotConfig, BotState, StrategyConfig, check_signals, create_exchange, default_symbols, prepare_exchange, fetch_ohlcv_df


def main() -> None:
 config = BotConfig()
 strategy = StrategyConfig()
 symbols = default_symbols(config.default_type)
 state = BotState(symbols)
 exchange = create_exchange(config)
 exchange.load_markets()
 for symbol in symbols:
 prepare_exchange(exchange, config, symbol)

 print(f"[START] Bitget bot lancé | LIVE_TRADING={config.live_trading}")

 while True:
 for symbol in symbols:
 try:
 df = fetch_ohlcv_df(exchange, symbol, strategy.timeframe, limit=50)
 events, _ = check_signals(exchange, state, strategy, config, symbol, df)
 for event in events:
 print(event)
 except Exception as exc:
 print(f"[ERROR] {symbol}: {exc}")

 time.sleep(60)


if __name__ == "__main__":
 main()
