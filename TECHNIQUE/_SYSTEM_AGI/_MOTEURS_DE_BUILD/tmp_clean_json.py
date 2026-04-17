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

def remove_emojis(text):
    if not isinstance(text, str):
        return text
    # This regex covers a wide range of emojis
    emoji_pattern = re.compile(
        "["
        "\U0001f600-\U0001f64f"  # emoticons
        "\U0001f300-\U0001f5ff"  # symbols & pictographs
        "\U0001f680-\U0001f6ff"  # transport & map symbols
        "\U0001f1e0-\U0001f1ff"  # flags (iOS)
        "\U00002702-\U000027b0"
        "\U000024c2-\U0001f251"
        "\U0001f900-\U0001f9ff"  # Supplemental Symbols and Pictographs
        "\U0001fa70-\U0001faff"  # Symbols and Pictographs Extended-A
        "\U0001f170-\U0001f19a"  # Enclosed Alphanumeric Supplement
        "\U0001f200-\U0001f2ff"  # Enclosed Ideographic Supplement
        "\U00002600-\U000026ff"  # Miscellaneous Symbols
        "\U00002300-\U000023ff"  # Miscellaneous Technical
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

def process_node(node):
    for key, value in node.items():
        if isinstance(value, str):
            node[key] = remove_emojis(value)
        elif isinstance(value, dict):
            process_node(value)
        elif isinstance(value, list):
            node[key] = [process_node(item) if isinstance(item, dict) else remove_emojis(item) if isinstance(item, str) else item for item in value]
    return node

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Process meta
    if 'system_meta' in data:
        process_node(data['system_meta'])
    
    # Process nodes
    if 'knowledge_nodes' in data:
        for node in data['knowledge_nodes']:
            process_node(node)

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("Emojis successfully removed from JSON.")
except Exception as e:
    print(f"Error: {e}")
