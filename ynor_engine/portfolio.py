import numpy as np

class YnorPortfolioEngine:
    def __init__(self, max_total_exposure=0.05):
        self.max_total_exposure = max_total_exposure

    def allocate(self, balance, assets_scores):
        """
        Calcule l'allocation optimale pour une liste d'assets.
        assets_scores: dict { "BTC": 85, "ETH": 40, ... }
        """
        # Filtrage des signaux faibles
        candidates = {k: v for k, v in assets_scores.items() if v > 70 or v < 30}
        
        if not candidates:
            return {}

        # Calcul du poids relatif basé sur la confiance (Confidence-Weighted Allocation)
        total_purity = sum(candidates.values())
        allocations = {}
        
        for asset, score in candidates.items():
            # Allocation de base : 1% du capital par opportunité
            # Pondérée par la force du signal
            purity_factor = score / 100.0
            share = (balance * 0.01) * purity_factor
            
            # Limite de sécurité individuelle
            allocations[asset] = share

        # Vérification de l'exposition globale
        total_allocated = sum(allocations.values())
        if total_allocated > (balance * self.max_total_exposure):
            # Réduction proportionnelle si dépassement du plafond
            reduction_ratio = (balance * self.max_total_exposure) / total_allocated
            allocations = {k: v * reduction_ratio for k, v in allocations.items()}

        return allocations

    def detect_correlations(self, returns_matrix):
        """ Suppression des doublons de risque (Anti-correlation) """
        # À implémenter avec numpy pour les versions futures
        pass
