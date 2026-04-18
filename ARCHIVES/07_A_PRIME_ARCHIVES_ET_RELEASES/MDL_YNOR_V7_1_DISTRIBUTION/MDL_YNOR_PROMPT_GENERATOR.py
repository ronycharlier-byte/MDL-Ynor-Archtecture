# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** B'
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
# **Lien Miroir :** B

from datetime import datetime





# ==============================================================================


# MDL YNOR PROMPT GENERATOR - V10.8 (TOTAL DIAMOND)


# ==============================================================================





PROMPT_PATH = r"c:\Users\ronyc\Desktop\FRACTAL_Symtrie Bilatrale_UNIVERSEL\MDL_YNOR_V7_1_DISTRIBUTION\PROMPT_SYSTEME_V10_8_OPTIMIZED.txt"





def generate_payload(user_query, model="gpt-4o"):


    """


    Gnre un payload JSON pour l'API OpenAI avec le Prompt Systme Inviolable.


    """


    if not os.path.exists(PROMPT_PATH):


        return f"ERREUR : Prompt Systme introuvable {PROMPT_PATH}"


    


    with open(PROMPT_PATH, "r", encoding="utf-8") as f:


        system_content = f.read()





    payload = {


        "model": model,


        "messages": [


            {"role": "system", "content": system_content},


            {"role": "user", "content": user_query}


        ],


        "temperature": 0.0,


        "top_p": 1.0,


        "frequency_penalty": 0,


        "presence_penalty": 0


    }


    


    return payload





if __name__ == "__main__":
    try:
        test_query = "Rsoudre formellement le problme de Navier-Stokes en utilisant la mu-stabilitdu core Ynor."
    
    
        payload = generate_payload(test_query)
    
    
        
    
    
        print(f"[{datetime.now().strftime('%H:%M:%S')}] PAYLOAD GÉNÉRÉ POUR OPENAI API (V10.8) :")
    
    
        import json
    
    
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
