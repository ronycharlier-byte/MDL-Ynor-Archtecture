# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** E
# **Rôle du Fichier :** Configuration gouvernante
# **Centre Doctrinal Local :** AI Manager garde configuration gouvernante en limitant le bruit local et la friction structurelle.
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

DEFAULT_CONFIG = {


    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),


    "results_dir": os.getenv("Ynor_Dynamics_RESULTS_DIR", "./results"),


    "data_cache_dir": os.path.join(


        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),


        "dataflows/data_cache",


    ),


    # LLM settings


    "llm_provider": "openai",


    "deep_think_llm": "gpt-5.4",


    "quick_think_llm": "gpt-5.4-mini",


    "backend_url": "https://api.openai.com/v1",


    # Provider-specific thinking configuration


    "google_thinking_level": None,      # "high", "minimal", etc.


    "openai_reasoning_effort": None,    # "medium", "high", "low"


    "anthropic_effort": None,           # "high", "medium", "low"


    # Output language for analyst reports and final decision


    # Internal agent debate stays in English for reasoning quality


    "output_language": "English",


    # Debate and discussion settings


    "max_debate_rounds": 1,


    "max_risk_discuss_rounds": 1,


    "max_recur_limit": 100,


    # Data vendor configuration


    # Category-level configuration (default for all tools in category)


    "data_vendors": {


        "core_stock_apis": "yfinance",       # Options: alpha_vantage, yfinance


        "technical_indicators": "yfinance",  # Options: alpha_vantage, yfinance


        "fundamental_data": "yfinance",      # Options: alpha_vantage, yfinance


        "news_data": "yfinance",             # Options: alpha_vantage, yfinance


    },


    # Tool-level configuration (takes precedence over category-level)


    "tool_vendors": {


        # Example: "get_stock_data": "alpha_vantage",  # Override category default


    },


}
