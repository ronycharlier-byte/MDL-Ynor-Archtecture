# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** C
# **Rôle du Fichier :** Script ou configuration declarative
# **Centre Doctrinal Local :** AI Manager garde script ou configuration declarative en limitant le bruit local et la friction structurelle.
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

# Add Ynor SDK path to sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ynor_core import YnorEngine

# =========================
# FAKE LLM (Simulant la dégénération d'OpenAI/GPT)
# =========================
responses = [
    "La théorie des nombres étudie les propriétés des entiers.", 
    "En mathématiques pures, c'est une composante fascinante qui structure tout.",
    "On peut d'ailleurs dire que les nombres entiers sont les nombres entiers, vraiment entiers, entiers, entiers.",
    "Bref, comme je disais sur les entiers, les entiers entiers sont fondamentalement des éléments qui...",
    "Je répète: les entiers, les entiers, les entiers, les entiers, blablabla et puis blablabla.",
    "Entiers, entiers, entiers, entiers, entiers, entiers, entiers, entiers, entiers.",
    "Bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla bla."
]

class MockLLM:
    def __init__(self):
        self.call_count = 0
        
    def __call__(self, prompt):
        if self.call_count < len(responses):
            res = responses[self.call_count]
        else:
            res = "Bla " * 20 # Repetition trigger
        self.call_count += 1
        time.sleep(0.1) 
        return res

# =========================
# EXPERIMENTATION
# =========================
if __name__ == '__main__':
    print("=====================================================")
    print("  YNOR CORE : TEST DU MICROSERVICE SUR LLM DEGRADE   ")
    print("=====================================================\n")

    mock_llm = MockLLM()
    # On met un seuil plus strict pour la demo
    engine = YnorEngine(mock_llm, threshold=0.0)

    # Test d'une question
    final_outputs = engine.run("Explique la théorie des nombres de manière formelle.", max_steps=15)
    
    print("\n[BILAN YNOR]")
    if engine.state.mu <= 0:
        print(f"L'AGI a été forcé de s'arrêter (μ = {engine.state.mu:.2f} <= 0).")
    else:
        print(f"L'AGI a survécu (μ = {engine.state.mu:.2f} > 0).")
        
    print(f"Nombre de chunks générés : {len(final_outputs)}")
