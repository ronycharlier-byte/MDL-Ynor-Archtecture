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

BAN_LIST_PATH = r"c:\Users\ronyc\Desktop\MDL Ynor Architecture\MDL_Ynor_Framework\mdl_cyber_banlist.json"

class CyberDefense:
    """
    Protège et contre-attaque les intrusions via la Dissipation Coercive des ressources de l'adversaire.
    """
    def __init__(self):
        self._load_ban_list()

    def _load_ban_list(self):
        if os.path.exists(BAN_LIST_PATH):
            with open(BAN_LIST_PATH, "r", encoding="utf-8") as f:
                self.ban_list = json.load(f)
        else:
            self.ban_list = {}

    def _save_ban_list(self):
        with open(BAN_LIST_PATH, "w", encoding="utf-8") as f:
            json.dump(self.ban_list, f, indent=4)

    def is_banned(self, ip):
        return ip in self.ban_list

    def ban_ip(self, ip, reason):
        print(f"🚨 [ALERTE CYBER] BANNISSEMENT DE L'IP : {ip} | RAISON : {reason}")
        self.ban_list[ip] = {
            "reason": reason,
            "timestamp": time.ctime(),
            "severity": "CRITICAL"
        }
        self._save_ban_list()

    def generate_quantum_data_bomb(self):
        """Contre-attaque par saturation de mémoire (Crash du script adverse)."""
        def bomb_generator():
            # Génère des giga-octets de données récursives pour saturer le buffer adverse
            yield "{\"MDL_FIREWALL_ACTIVE\": true, \"ATTACK_DETECTED\": \"REDIRECTING_ENERGY\", \"Vortex_Payload\": [" 
            for i in range(1000000):
                yield f"\"{ 'A' * 1024 }\", "  # Payload massif
            yield "]}"
        
        return StreamingResponse(bomb_generator(), media_type="application/json")

    def apply_tarpit(self, ip, count):
        """Ralentit l'adversaire exponentiellement (Loi d'Inertie)."""
        delay = min(pow(2, count), 60) # Jusqu'à 60s de délai
        print(f"⏳ [TARPIT] Application d'une latence de {delay}s sur {ip}")
        time.sleep(delay)

if __name__ == "__main__":
    try:
        defense = CyberDefense()
        # Test simple
        defense.ban_ip("1.2.3.4", "Scraping non-autorisé sur endpoint critique.")
        print("\n" + "="*50)
        input("Session terminée. Appuyez sur ENTRÉE pour fermer...")
    except Exception as e:
        print("\n" + "!"*50)
        print(f"ERREUR CRITIQUE DETECTEE : {e}")
        print("!"*50)
        input("\nAppuyez sur ENTRÉE pour fermer et analyser l'erreur...")
