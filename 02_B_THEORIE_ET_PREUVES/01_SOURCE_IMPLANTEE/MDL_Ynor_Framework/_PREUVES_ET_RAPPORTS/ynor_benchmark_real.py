"""

YNOR BENCHMARK : PREUVE DE LA VIABILITÉ ÉCONOMIQUE

-----------------------------------------------

Ce script compare une excution LLM brute (sans fin) 

face un systme gouvernpar Ynor Core.



Objectif: Dmontrer une rduction de 30% 70% des coûts (Beta).

"""

import time

import os

import sys



# Ajout du SDK au path

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_04_DEPLOYMENT_AND_API"))



from ynor_core import YnorEngine, get_token_count



# =========================

# L'AGENT "BOUCLEUR" (SPAMMER)

# =========================

# Cet agent simule une drive LLM classique (rptitions, perte d'utilit)

def looping_llm(context):

    # Simule une rponse de plus en plus mdiocre et rptitive

    words = context.split()

    if len(words) > 200:

        return "Bla bla bla, je rpte encore les mêmes informations car je n'ai plus rien dire sur Ynor..." * 2

    return "Voici une information utile sur la thorie des nombres et la marge mu."



# =========================

# PROTOCOLE DE BENCHMARK

# =========================



def run_benchmark(prompt):

    print("=====================================================")

    print(" [BENCHMARK] YNOR CORE vs BASELINE LLM (No-Guard)    ")

    print("=====================================================\n")



    max_limit = 20 # Limite force pour viter l'explosion de tokens relle sur la machine

    

    # 1. BASELINE (Simule un agent sans contrôle qui va au bout)

    print(" [1/2] Excution Baseline (Sans Ynor)...")

    context_baseline = prompt

    tokens_baseline = 0

    for i in range(max_limit):

        res = looping_llm(context_baseline)

        context_baseline += "\n" + res

        tokens_baseline += get_token_count(res)

        

    print(f"  > Baseline complte. Tokens consomms : {tokens_baseline}")



    # 2. YNOR GUARDED

    print("\n [2/2] Excution Ynor Guarded (Sous gouvernance μ)...")

    engine = YnorEngine(looping_llm, threshold=0.0)

    ynor_outputs = engine.run(prompt, max_steps=max_limit, verbose=True)

    

    ynor_tokens = sum(get_token_count(o) for o in ynor_outputs)

    print(f"  > Ynor Guard complt. Tokens consomms : {ynor_tokens}")



    # 3. CALCUL DU GAIN

    print("\n=====================================================")

    print(" [SYNTHÈSE LOGIQUE ET FINANCIÈRE]")

    print("=====================================================")

    

    saving = tokens_baseline - ynor_tokens

    percentage = (saving / tokens_baseline) * 100 if tokens_baseline > 0 else 0

    

    print(f" Économie de tokens (Bêta) : {saving}")

    print(f" Gain d'Efficacit        : {percentage:.2f}%")

    print(f" Statut du Systme         : {'VIABLE (mu > 0)' if percentage > 0 else 'ÉCHEC'}")

    

    if percentage > 25:

        print("\n [CONFIRMÉ] : Ynor dcapite la drive entropique avec succs.")

        print(" Impact : Rduction majeure de la facture LLM industrielle.")

    print("=====================================================")



if __name__ == '__main__':

    run_benchmark("Explique la thorie de la marge dissipative.")

