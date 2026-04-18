# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
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

directory = "."
files = [f for f in os.listdir(directory) if f.endswith('.pdf')]
files.sort()

for file in files:
    try:
        with open(file, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            if len(reader.pages) > 0:
                text = reader.pages[0].extract_text()
                print(f"--- {file} ---")
                print(text[:1000]) # Print first 1000 characters
                print("\n")
    except Exception as e:
        print(f"Error reading {file}: {e}")
