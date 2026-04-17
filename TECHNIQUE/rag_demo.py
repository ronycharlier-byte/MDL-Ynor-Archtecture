# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
# **Position Chiastique :** E
# **Rôle du Fichier :** Chaine RAG
# **Centre Doctrinal Local :** AI Manager garde chaine rag en limitant le bruit local et la friction structurelle.
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

# Load environment variables (OPENAI_API_KEY)
load_dotenv()

def main():
    """
    Demonstration of the upgraded RAG system with source attribution 
    and strict context enforcement.
    """
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set.")
        return

    # 1. Initialize logic
    memory = VectorMemory(model="text-embedding-3-small")
    pipeline = IngestionPipeline(memory, chunk_size=500)
    engine = RagEngine(memory)

    # 2. Setup demonstration corpus
    corpus_zip = "production_corpus.zip"
    if not os.path.exists(corpus_zip):
        import zipfile
        print(f"Generating {corpus_zip}...")
        with zipfile.ZipFile(corpus_zip, 'w') as zf:
            zf.writestr("engine_specs.md", "The Zenith Engine v16.0 utilizes a recursive Fourier transform for market prediction. It operates with a latency of 5ms.")
            zf.writestr("safety_protocols.txt", "In case of high volatility (>40%), the 'Flash-Crash' protocol triggers an automatic position liquidation to protect capital.")
            zf.writestr("governance.json", '{"policy": "The system must maintain a 10/10 integrity score.", "auditor": "MDL Ynor"}')

    # 3. Ingest documents
    print("Starting ingestion...")
    pipeline.run(corpus_zip)

    # 4. Test Queries
    
    # Query 1: Information present in context
    print("\n" + "="*50)
    print("QUERY 1: What is the Zenith Engine?")
    print("="*50)
    response_1 = engine.answer_question("What is the Zenith Engine?")
    print(response_1)

    # Query 2: Information NOT in context (should trigger "I don't know")
    print("\n" + "="*50)
    print("QUERY 2: Who is the CEO of Apple?")
    print("="*50)
    response_2 = engine.answer_question("Who is the CEO of Apple?")
    print(response_2)

    # Query 3: Multi-source attribution
    print("\n" + "="*50)
    print("QUERY 3: How does the system handle high volatility and what is its goal?")
    print("="*50)
    response_3 = engine.answer_question("How does the system handle high volatility and what is its goal?")
    print(response_3)

if __name__ == "__main__":
    main()
