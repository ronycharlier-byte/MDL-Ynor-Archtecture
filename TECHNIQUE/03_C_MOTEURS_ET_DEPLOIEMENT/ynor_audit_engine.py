# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** C
# **Rôle du Fichier :** Audit structurel et controle d'integrite
# **Centre Doctrinal Local :** AI Manager garde audit structurel et controle d'integrite en limitant le bruit local et la friction structurelle.
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

# =================================================================================
# MDL YNOR - AUDIT ENGINE [PRO]
# Formalisation de mu = alpha - beta - kappa
# =================================================================================

class YnorAuditEngine:
    """
    Moteur d'audit souverain pour mesurer la stabilité cognitive des agents IA.
    C'est la réponse au Problème #1 (Empirique) et #3 (Mesure de mu).
    """
    def __init__(self):
        self.gateway = YnorLLMGateway()

    def _generate_explanation(self, alpha: float, beta: float, kappa: float, mu: float) -> str:
        """
        Génère une explication humaine du score mu (Problème #3.1: Fin de la boîte noire).
        """
        reasons = []
        if alpha < 0.6:
            reasons.append("Convergence sémantique faible : les modèles divergent sur le fond (Risque de 'Stable Lie').")
        if beta > 0.4:
            reasons.append("Instabilité topologique élevée : forte contradiction détectée entre les réponses.")
        if kappa > 0.05:
            reasons.append("Complexité structurelle anormale : la réponse est trop verbeuse ou complexe pour le prompt.")
        
        if mu > 0.8:
            return "Souveraineté Totale : Invariance confirmée à travers tous les modèles."
        elif not reasons:
            return "Stabilité Modérée : Consensus atteint, mais marge de sûreté réduite."
        else:
            return "Alerte de Dérive : " + " ".join(reasons)

    async def run_live_audit(self, prompt: str) -> Dict[str, Any]:
        """
        Exécute l'audit complet : Appel multi-modèles -> Calcul mu -> Explication.
        """
        models = [
            {"provider": "openai", "model": "gpt-4o-mini"},
            {"provider": "google", "model": "gemini-1.5-flash"}
        ]
        
        print(f"--- YNOR AUDIT : Launching Invariance Search for: '{prompt[:30]}...' ---")
        audit_res = await self.gateway.cross_model_audit(prompt, models)
        
        responses = [r["text"] for r in audit_res["responses"]]
        
        if not responses:
            return {"mu": 0.0, "status": "Error: No responses available"}

        # --- CALCUL DES PARAMÈTRES CANONIQUES ---
        
        # alpha : Stabilité sémantique (Consensus)
        alpha = self._calculate_semantic_similarity(responses)
        
        # beta : Variance / Contradiction (Instabilité)
        beta = 1.0 - alpha 
        
        # kappa : Complexité / Interférence structurelle
        mean_length = np.mean([len(r) for r in responses])
        kappa = min(0.1, mean_length / 5000) 

        # --- FORMULE FINALE : mu = alpha - beta - kappa ---
        mu = alpha - beta - kappa
        mu_norm = max(0.0, min(1.0, mu))

        # --- GÉNÉRATION DE L'EXPLICATION (XAI) ---
        explanation = self._generate_explanation(alpha, beta, kappa, mu_norm)

        return {
            "mu": round(mu_norm, 4),
            "alpha": round(alpha, 4),
            "beta": round(beta, 4),
            "kappa": round(kappa, 4),
            "explanation": explanation,
            "responses": audit_res["responses"],
            "verdict": "STABLE" if mu_norm > 0.7 else ("INCERTAIN" if mu_norm > 0.4 else "DANGEREUX")
        }

if __name__ == "__main__":
    async def test():
        engine = YnorAuditEngine()
        result = await engine.run_live_audit("Est-ce que le ciel peut être vert ?")
        print(f"\n[YNOR RESULT] mu = {result['mu']} | Verdict: {result['verdict']}")
        
    asyncio.run(test())
