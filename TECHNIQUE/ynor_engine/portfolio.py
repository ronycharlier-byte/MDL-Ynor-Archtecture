import numpy as np

class YnorPortfolioEngine:
    def __init__(self, max_total_exposure=0.70, max_asset_allocation=0.30):
        self.max_total_exposure = max_total_exposure
        self.max_asset_allocation = max_asset_allocation

    def allocate(self, balance, signals):
        """
        Calcul de l'allocation pondérée par le score.
        signals: list of dicts [{"symbol": "...", "score": 85, "action": "buy"}]
        """
        # 1. Filtrage des opportunités réelles
        active_signals = [s for s in signals if s["action"].upper() != "HOLD"]
        
        if not active_signals:
            return {}

        # 2. Top 3 Assets (Risque limité)
        active_signals = sorted(active_signals, key=lambda x: x["score"], reverse=True)[:3]
        
        # 3. Calcul du poids relatif
        total_score = sum([s["score"] for s in active_signals])
        if total_score == 0: return {}

        allocations = {}
        for s in active_signals:
            symbol = s["symbol"]
            score = s["score"]
            
            # Poids relatif
            weight = score / total_score
            
            # Allocation cible
            allocation = balance * weight
            
            # Application du plafond par asset (30%)
            allocation = min(allocation, balance * self.max_asset_allocation)
            
            allocations[symbol] = allocation

        # 4. Vérification de l'exposition globale (70%)
        total_allocated = sum(allocations.values())
        max_allowed = balance * self.max_total_exposure
        
        if total_allocated > max_allowed:
            reduction_ratio = max_allowed / total_allocated
            allocations = {k: v * reduction_ratio for k, v in allocations.items()}

        return allocations
