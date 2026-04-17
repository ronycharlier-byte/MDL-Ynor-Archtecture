from pathlib import Path
import asyncio
import sys
import threading

# Keep the repository root importable so TECHNIQUE can reach MONITORING.
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from MONITORING.dashboard.server import run_server
from config.settings import SAFE_MODE


def start_engine():
    """Launch the sovereign loop in the background."""
    print(f"[ENGINE] Starting MDL Ynor V1.6.1 (SAFE_MODE={SAFE_MODE})")
    # Simulated loop
    # while True:
    #     asyncio.run(agent.run_cycle())
    #     time.sleep(3)


if __name__ == "__main__":
    # 1. Launch the engine in a background thread.
    engine_thread = threading.Thread(target=start_engine)
    engine_thread.daemon = True
    engine_thread.start()

    # 2. Launch the dashboard (blocking).
    run_server()
