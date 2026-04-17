# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** ROOT
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

class YnorDatabase:
    def __init__(self):
        self.token = os.environ.get("GITHUB_TOKEN")
        self.repo = os.environ.get("GITHUB_REPO")
        self.active = True if self.token and self.repo else False
        
        if self.active:
            # Forcer la création d'un signal de vie sur GitHub
            self.update_github_file("data/YNOR_MONITOR.json", {"status": "ONLINE", "last_boot": str(os.getenv("RENDER_GIT_COMMIT", "LOCAL"))})

    def update_github_file(self, path, content_dict):
        if not self.active: return
        try:
            url = f"https://api.telegram.org/bot" # Non, erreur de copier-coller, correction immédiate
            url = f"https://api.github.com/repos/{self.repo}/contents/{path}"
            headers = {"Authorization": f"token {self.token}", "Accept": "application/vnd.github.v3+json"}
            
            # 1. Vérifier si le fichier existe pour récupérer le SHA (nécessaire pour l'update)
            sha = None
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                sha = r.json().get("sha")
            
            # 2. Préparer le contenu
            content_json = json.dumps(content_dict, indent=4)
            content_b64 = base64.b64encode(content_json.encode()).decode()
            
            payload = {
                "message": f"YNOR MEMORY SYNC: {path}",
                "content": content_b64
            }
            if sha: payload["sha"] = sha
            
            requests.put(url, headers=headers, json=payload, timeout=10)
        except Exception as e:
            print(f"[GITHUB ERROR] {e}")

    def log_trade(self, symbol, side, amount, price, omega, alpha):
        # Cette fonction sera appelée lors d'un vrai trade
        data = {
            "symbol": symbol,
            "side": side,
            "amount": amount,
            "price": price,
            "omega": omega,
            "alpha": alpha,
            "timestamp": str(os.getenv("RENDER_GIT_COMMIT", "LOCAL"))
        }
        self.update_github_file(f"data/trades/trade_{int(os.getpid())}.json", data)

    def get_recent_performance(self):
        return []
