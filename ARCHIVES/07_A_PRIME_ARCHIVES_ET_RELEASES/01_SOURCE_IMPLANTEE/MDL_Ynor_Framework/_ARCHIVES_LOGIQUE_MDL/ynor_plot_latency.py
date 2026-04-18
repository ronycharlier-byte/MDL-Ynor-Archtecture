# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** B'
# **Rôle du Fichier :** Visualisation et cartographie
# **Centre Doctrinal Local :** AI Manager garde visualisation et cartographie en limitant le bruit local et la friction structurelle.
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

def plot_latency_benchmark():
    file_path = "mdl_openai_stress_benchmark.json"
    
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Erreur : Fichier de benchmark introuvable. Lancez d'abord le stress test.")
        return

    details = data.get("details", [])
    if not details:
        print("Aucune intervention enregistrée dans le benchmark.")
        return

    nodes = [d["node"] for d in details]
    latencies = [d["latency_ms"] for d in details]
    mutations = [d["mutation_suggested"] for d in details]

    # Création du Graphique
    plt.figure(figsize=(10, 6))
    bars = plt.bar(nodes, latencies, color='skyblue', edgecolor='navy', alpha=0.8)
    
    # Ajout des étiquettes (Latence et Taux de mutation)
    for bar, mut in zip(bars, mutations):
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 50, 
                 f"{yval:.0f}ms\n(Mut: +{mut*100:.0f}%)", 
                 ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.title("BENCHMARK IA : INDICE DE DIFFICULTÉ PAR NŒUD MDL YNOR")
    plt.ylabel("Temps de Réflexion OpenAI (ms)")
    plt.xlabel("Nœuds de l'Architecture")
    plt.ylim(0, max(latencies) * 1.3)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    output_file = "mdl_latency_benchmark_chart.png"
    plt.savefig(output_file)
    print(f"\n[OK] Graphique de benchmarking généré : {output_file}")
    
    # Rapport textuel
    hardest_node = nodes[np.argmax(latencies)]
    print(f"\n[ANALYSE] Le nœud le plus complexe à stabiliser pour l'IA est : {hardest_node}")

if __name__ == "__main__":
    try:
        plot_latency_benchmark()
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
