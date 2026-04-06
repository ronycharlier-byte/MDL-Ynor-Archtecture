# ARCHITECTURE YNOR V11.13 - SOVEREIGN ENVIRONMENT
FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy essential corpus layers (Canonical only)
COPY 00_EDITION_CANONIQUE_FINALE /app/00_CANONICAL
COPY 01_A_FONDATION /app/01_FONDATION
COPY 02_B_THEORIE_ET_PREUVES /app/02_THEORIE
COPY 03_C_MOTEURS_ET_DEPLOIEMENT /app/03_MOTEUR
COPY 05_C_PRIME_VALIDATION_ET_TESTS /app/05_VALIDATION
COPY riemann_engine.py .
COPY check_chiastic_symmetry.py .

# Environment variables
ENV YNOR_STABILITY_INDEX=1.0
ENV PORT=8080

# Run stability benchmark by default
ENTRYPOINT ["python", "riemann_engine.py"]
