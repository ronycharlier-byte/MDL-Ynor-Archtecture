import asyncio
import threading
from dashboard.server import run_server
from config.settings import SAFE_MODE

def start_engine():
    """ Lance la boucle souveraine en arriere-plan """
    print(f"🚀 [ENGINE] Starting MDL Ynor V1.6.1 (SAFE_MODE={SAFE_MODE})")
    # Boucle simulée
    # while True:
    #     asyncio.run(agent.run_cycle())
    #     time.sleep(3)

if __name__ == "__main__":
    # 1. Lancer l'engine dans un thread separe
    engine_thread = threading.Thread(target=start_engine)
    engine_thread.daemon = True
    engine_thread.start()

    # 2. Lancer le dashboard (bloquant)
    run_server()
