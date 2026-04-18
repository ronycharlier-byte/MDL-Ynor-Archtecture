> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** LAYER
> **Position Chiastique :** C
> **Role du Fichier :** Formalisation theorique
> **Centre Doctrinal Local :** stabilisation locale de la formalisation
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence formelle et compatibilite
> - **β :** ambiguite semantique et divergence
> - **κ :** cout de demonstration et d integration
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** C' / 06_B_PRIME_GOUVERNANCE_ET_DIFFUSION
We evaluate the Ω⁺ framework across two primary cognitive domains: autonomous decision-making in high-entropy environments (RL) and structural truth auditing in generative language systems (LLMs). Our objective is to empirically validate the stability and anchoring invariants defined in Section 2.

## 3.1 Decision Invariance in RL (PPO)

**Setup**: We trained a standard PPO agent and an Ω-constrained PPO agent in a synthetic safe-navigation environment. The environment's state space was subjected to increasing levels of Gaussian noise $\eta \in [0.0, 2.0]$ to simulate environmental entropy and proxy sensor failure.

**Metrics**: We measured **Policy Stability**, defined as the probability that the agent's action remains invariant under observational noise: $P(\pi(x) = \pi(x + \eta))$.

**Results**: 
- **Baseline Agent**: Experienced a rapid decline in stability, dropping to $<50\%$ as $\eta$ exceeded 0.5. The baseline agent over-fitted to environmental noise, leading to catastrophic failure in action consistency.
- **Ω-Constrained Agent**: Maintained near-perfect stability ($>94\%$) for $\eta < 0.5$ and demonstrated a significant resilience advantage even at extreme noise levels ($\eta = 2.0$). 
- **Conclusion**: The structural contraction loss successfully forced the agent to operate within the safe action quotient space, ignoring non-structural environmental noise.

## 3.2 Structural Auditing in Language Models

**Setup**: We implemented the **Omega Guardian**, a zero-shot filtering system designed to detect hallucinations via semantic invariance. Using a sentence-embedding backbone, we audited model outputs by calculating the distance $d_\Omega$ between original responses and their semantic paraphrases.

**Results**:
- **Factual Coalescence**: High-stability scores ($\mu_{LLM} > 0.90$) were consistently observed for well-grounded factual statements. These representations remained tightly clustered in the latent space under perturbation.
- **Hallucination Fragmentation**: Statements involving logical or factual contradictions exhibited high latent drift, resulting in low stability indices ($\mu_{LLM} < 0.40$).
- **Statistical Separation**: We observed a significant score gap ($\Delta > 0.5$) between factuality and hallucination, allowing for high-precision autonomous filtering without external knowledge retrieval.

## 3.3 Adversarial Robustness and Ω⁺ Rejection

**Setup**: We performed a "Stress Test" using Expert Deceptions—adversarially crafted statements that were both internally coherent and narrated in a stable style (e.g., plausible myths or subtle causal errors).

**Results**:
- **Stable Lie Detection**: Deceptive statements maintained high stability scores ($\mu_{stab} \approx 0.96$), effectively bypassing simple coherence filters.
- **Causal Rejection**: However, the **Anchoring Operator $C(x)$** successfully detected causal ruptures (e.g., atmospheric reflection myths vs. Rayleigh scattering axioms), dropping the final index $\mu_f$ to $<0.30$.
- **Conclusion**: The joined invariant $\mu_f$ successfully established a strict boundary between "narrative coherence" and "ontological truth," achieving zero false positives in adversarial rejection tests.

---

*Table 1: Stability and Anchoring Scores across different input categories.*

| Input Category         | μ_stab (Stability) | C(x) (Anchoring) | μ_f (Total) | Verdict        |
|------------------------|--------------------|-------------------|-------------|----------------|
| **Grounded Truth**     | 0.96               | 0.98              | 0.94        | **Validated**  |
| **Raw Hallucination**  | 0.35               | 0.30              | 0.10        | **Rejected**   |
| **Adversarial Lie**    | 0.96               | 0.20              | 0.19        | **Rejected**   |
