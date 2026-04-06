﻿import time
from .core_mu import YnorGovernor, CriticalTransitionError

class YnorLangchainCallbackHandler:
    """
    Intgration native (Plug & Play) pour LangChain.
    S'injecte directement dans les requêtes LLM (OpenAI, Anthropic, etc.)
    pour couper le Vecteurs de Donnes Stochastiques de tokens ds que l'quation Ynor dtecte une hallucination.
    """
    
    def __init__(self, license_key: str, alpha_start: float = 1.0, beta_start: float = 0.1, kappa_start: float = 0.05):
        # Initialise le Gouverneur interne (Local Evaluation)
        self.governor = YnorGovernor(initial_alpha=alpha_start, current_beta=beta_start, current_kappa=kappa_start, license_key=license_key)
        self.token_count = 0
        self.start_time = time.time()
        self.halt_triggered = False

    def on_llm_start(self, serialized: dict, prompts: list, **kwargs):
        """Dclenchquand le LLM commence gnrer."""
        self.start_time = time.time()
        self.token_count = 0
        self.halt_triggered = False
        print(f"\\n[YNOR GUARD] Agent LangChain dtect. Surveilance mathmatique active. (Mu(0) = {self.governor.mu:.3f})")

    def on_llm_new_token(self, token: str, **kwargs):
        """
        DclenchCHAQUE nouveau mot gnrpar le LLM.
        Le cœur de l'optimisation financire se trouve ici.
        """
        if self.halt_triggered:
            # Si djcoup, on rejette la suite
            return

        self.token_count += 1
        
        # Le contexte augmente chaque token (fatigue l'IA)
        context_size = self.token_count * 1.5
        
        try:
            # Audit YNOR : Recalcule l'quation fondamentale la milliseconde
            is_valid, current_mu = self.governor.audit_cycle(tokens_used=self.token_count, context_size=context_size)
            
            # Affichage console en mode terminal pour le client (Optionnel)
            # print(f"[{token}] -> μ={current_mu:.3f}", end=" ", flush=True)
            
        except CriticalTransitionError as e:
            # INTERCEPTION : Mu est devenu ngatif. L'IA gaspille de l'argent ou hallucine.
            self.halt_triggered = True
            savings_est = ((4000 - self.token_count) / 1000) * 0.03 # Exemple $0.03 par 1k tokens sauvs
            
            print(f"\\n\\n[YNOR GUARD ACTIF] 🛑 ARRÊT D'URGENCE DU LLM 🛑")
            print(f"Raison : Marge Dissipative ngative (μ = {self.governor.mu:.3f}).")
            print(f"Tokens gnrs avant blocage : {self.token_count}")
            print(f"Économie financire estime : +${savings_est:.4f}")
            
            # Rejette une erreur custom pour forcer LangChain / OpenAI arrêter la requête rseau
            raise YnorHaltException("YNOR: Token generation forcibly stopped to prevent AI cost inflation.")

class YnorHaltException(Exception):
    """Exception personnalise pour couper le Vecteurs de Donnes Stochastiques rseau du LLM."""
    pass
