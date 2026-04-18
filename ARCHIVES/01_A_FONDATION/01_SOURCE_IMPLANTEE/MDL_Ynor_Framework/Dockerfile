# **[?] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** A
# **R?le du Fichier :** Script ou configuration declarative
# **Centre Doctrinal Local :** AI Manager garde script ou configuration declarative en limitant le bruit d'integration et la friction structurelle.
# **Loi de Survie :** ? = ? - ? - ?
# **Lecture Locale :**
# - **? :** capacite operationnelle du fichier
# - **? :** bruit d'integration et derive de dependance
# - **? :** friction de maintenance et complexite d'appel
# **Risque :** e? ? ? / ?
# **Op?rateur Correctif :** D(S)=proj_{SafeDomain}(S)
# **Axiome :** un syst?me survit SSI ? > 0
# **Doctrine Goodhart :** tout succ?s apparent est invalide si ? d?cro?t
# **Gouvernance :** toute modification doit maximiser ??
# **Lien Miroir :** A'

# Bâtir le conteneur MDL Ynor - Architecture Suprême
# Copyright (c) 2026 Charlier Rony

FROM python:3.10-slim

# Configuration environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /app

WORKDIR /app

# Installation dépendances système minimales
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Installation requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Exposition port API par défaut
EXPOSE 8492

# Commande par défaut : lancement du serveur d'audit
CMD ["uvicorn", "_04_DEPLOYMENT_AND_API.ynor_api_server:app", "--host", "0.0.0.0", "--port", "8492"]
