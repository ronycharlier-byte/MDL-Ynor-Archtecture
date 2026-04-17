# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** LAYER
# **Position Chiastique :** E
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
# **Lien Miroir :** E

file_path = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\_00_DISTS_AND_RELEASES\MDL_YNOR_GPT_ULTIMATE_UPLOAD_V17\mdl_global_knowledge.json"
paypal_link = "https://www.paypal.com/ncp/payment/BDTWYYEN8XMML"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace the placeholder with the real link
    new_content = content.replace("[VOTRE_LIEN_PAYPAL_ME]", paypal_link)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("Real PayPal link successfully injected into JSON.")
except Exception as e:
    print(f"Error: {e}")
