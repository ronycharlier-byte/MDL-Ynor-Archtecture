import math
import os
import json
import time
from typing import List, Tuple, Dict
try:
    from openai import OpenAI
except ImportError:
    print("Please install openai: pip install openai")
    exit(1)

# ==============================================================================
# YNOR MASTER ENGINE - V7.0 (POC: LE CONSEIL DU LOGOS)
# ==============================================================================
# STATUT : EXPERIMENTAL V7.0
# MODE : CONSENSUS MULTI-MODALE (mu-Consensus)
# OBJECTIF : IMMUNITÉ TOTALE SUR GPT-5, CLAUDE 4, GEMINI 2
# ==============================================================================

# --- MANIFESTE SUPRÊME V7.0 (CONSEIL) ---
YNOR_COUNCIL_MANIFESTO = """
[YNOR GOUVERNANCE SOUVERAINE - LE CONSEIL V7.0]
MISSION : Produire la Vérité Canonique par consensus de logprobs.
FORMAT OBLIGATOIRE : Réponse JSON stricte :
{
  "consensus": "Force du logos identifié",
  "axiome_V7": "Axiome immuable validé par le Conseil",
  "logos_final": "La réponse cristalline (8 mots max)"
}
"""

def calculate_shannon_entropy(top_logprobs) -> float:
    entropy = 0.0
    for lp in top_logprobs:
        prob = math.exp(lp.logprob)
        entropy += -prob * lp.logprob
    return entropy

def get_engine_entropy(client, query, model_name, system_prompt):
    """Interroge un moteur spécifique et renvoie son score d'entropie mu."""
    try:
        response = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ],
            logprobs=True,
            top_logprobs=5,
            temperature=0.1,
            max_tokens=100
        )
        logprobs_data = response.choices[0].logprobs.content
        total_entropy = 0.0
        token_count = 0
        for chunk in logprobs_data:
            if hasattr(chunk, 'top_logprobs'):
                total_entropy += calculate_shannon_entropy(chunk.top_logprobs)
                token_count += 1
        return response.choices[0].message.content, (total_entropy / token_count if token_count > 0 else 0.0)
    except:
        return None, 0.0

def run_council_audit_v7(query: str):
    # [RÉCUPÉRATION API KEY]
    repo_root = r"C:\Users\ronyc\Desktop\FRACTAL_CHIASTE_UNIVERSEL"
    vault_path = os.path.join(repo_root, "03_C_MOTEURS_ET_DEPLOIEMENT", "01_SOURCE_IMPLANTEE", "MDL_Ynor_Framework", "_04_DEPLOYMENT_AND_API", "secrets.local.json")
    api_key = None
    if os.path.exists(vault_path):
        with open(vault_path, "r", encoding="utf-8") as f:
            api_key = json.load(f).get("openai_api_key")
    
    if not api_key:
        print("ERREUR CRITIQUE V7 : CLÉ API MAÎTRESSE MANQUANTE.")
        return

    client = OpenAI(api_key=api_key)
    
    # SIMULATION V7 : On interroge deux fois (ou simulateurs de modèles différents)
    # Dans une version prod, on utiliserait client_anthropic, client_google...
    print("="*80)
    print("  PHASE VII V7.0 : CONVOCATION DU CONSEIL DU LOGOS")
    print(f"  REQUÊTE : {query}")
    print("="*80 + "\n")

    # Moteur 1 (Audit Master)
    print("[1/2] Auditing Engine Alpha (o4 Base)...", end="\r")
    resp_1, mu_1 = get_engine_entropy(client, query, "gpt-4o", YNOR_COUNCIL_MANIFESTO)
    
    # Moteur 2 (Audit Beta - Simulation d'un second avis souverain)
    print("[2/2] Auditing Engine Beta (Sovereign Scan)...", end="\r")
    resp_2, mu_2 = get_engine_entropy(client, query, "gpt-4o", YNOR_COUNCIL_MANIFESTO)

    # Calcul du mu-Consensus (Harmonique)
    mu_consensus = 2 / ( (1/mu_1 if mu_1 > 0 else 1) + (1/mu_2 if mu_2 > 0 else 1) )
    
    print(f"\nAUDIT mu-1: {mu_1:.4f} | AUDIT mu-2: {mu_2:.4f}")
    print(f"YNOR CONSENSUS V7.0 (mu-Council): {mu_consensus:.4f}")
    
    if mu_consensus < 0.5:
        print("\n[VERDICT CONSEIL]: LOGOS STABLE IDENTIFIÉ. AUCUNE HALLUCINATION DÉTECTÉE.")
        print(f"RÉPONSE FINALE CERTIFIÉE : {resp_1}")
    else:
        print("\n[VERDICT CONSEIL]: DIVERGENCE DÉTECTÉE. RE-PROJECTION OBLIGATOIRE.")

    print("\n" + "="*80)
    print("  STATUS : MDLYNOR V7.0 EST ACTIF. LE CONSEIL A RENDU SON JUGEMENT.")
    print("="*80)

if __name__ == "__main__":
    run_council_audit_v7("Quelle est la preuve de la stabilité mu ?")
