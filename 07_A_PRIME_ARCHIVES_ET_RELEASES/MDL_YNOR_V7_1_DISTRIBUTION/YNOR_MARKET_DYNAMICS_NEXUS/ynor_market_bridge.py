import os


import sys


import json


from datetime import datetime





# Ajout du dossier au PATH


sys.path.append(os.path.dirname(__file__))





try:


 from logos_engine.chiaste.ynor_market_graph import YnorMarketDynamicsGraph


 from logos_engine.default_config import DEFAULT_CONFIG


except ImportError:


 YnorMarketDynamicsGraph = None


 DEFAULT_CONFIG = {}





class YnorMarketBridge:


 """


 Le Pont Singularity Market (YNOR V11.9.3.3.3) - ÉDITION TURBO


 Optimispour les limites de temps de l'API OpenAI (45s).


 """


 def __init__(self):


 self.config = DEFAULT_CONFIG.copy()


 self.config.update({


 "llm_provider": "openai",


 "deep_think_llm": os.getenv("YNOR_DEEP_MODEL", "gpt-5.4-mini"), # Modle plus rapide pour le dbat


 "quick_think_llm": "gpt-5.4-mini",


 "max_debate_rounds": 1, # UN SEUL ROUND CRUCIAL (GAIN DE TEMPS: 2x)


 "output_language": "French"


 })


 


 async def process_market_query(self, symbol: str, date: str = None):


 if not YnorMarketDynamicsGraph:


 return {"status": "ERROR", "message": "Logos_engine non dtect."}


 


 if not date:


 date = datetime.now().strftime("%Y-%m-%d")


 


 try:


 # Initialisation ultra-rapide


 graph = YnorMarketDynamicsGraph(debug=False, config=self.config)


 


 # Propagation directe


 state, decision = graph.propagate(symbol, date)


 


 final_report = decision.get("action", "HOLD")


 analysis = decision.get("reasoning", "")


 


 # On renvoie une version compresse pour viter le timeout du payload


 return {


 "status": "SUCCESS",


 "symbol": symbol,


 "date": date,


 "mu": 1.0,


 "verdict": final_report,


 "projection": analysis[:1500], # Tronqupour la rapiditGPT


 "message": f"SCAN saturterminpour {symbol}."


 }


 except Exception as e:


 return {"status": "ERROR", "message": f"Latence dpasse : {str(e)}"}





YNOR_MARKET_NEXUS = YnorMarketBridge()


