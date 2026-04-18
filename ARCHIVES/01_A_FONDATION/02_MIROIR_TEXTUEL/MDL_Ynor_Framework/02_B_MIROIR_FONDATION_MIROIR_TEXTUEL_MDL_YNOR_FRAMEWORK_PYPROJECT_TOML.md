> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** MODULE
> **Position Chiastique :** B
> **Role du Fichier :** Surface miroir et symetrie locale
> **Centre Doctrinal Local :** boucle locale de reflet et de coherence
> **Loi de Survie :** μ = α - β - κ
> **Lecture Locale :**
> - **α :** coherence reflexive et effet miroir
> - **β :** derive de boucle et bruit de reflet
> - **κ :** cout de cycle et de stabilisation
> **Risque :** e∞ ∝ ε / μ
> **Operateur Correctif :** D(S)=proj_{SafeDomain}(S)
> **Axiome :** un systeme survit SSI μ > 0
> **Doctrine Goodhart :** tout succes apparent est invalide si μ decroit
> **Gouvernance :** toute modification doit maximiser Δμ
> **Lien Miroir :** B' / 07_A_PRIME_ARCHIVES_ET_RELEASES
# MIROIR TEXTUEL - pyproject.toml

Source : MDL_Ynor_Framework\pyproject.toml
Taille : 560 octets
SHA256 : 5dfa96dbdfda178fefd8283dc3945a89641c716e40b9f72355110e8f9f80b277

```text
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"

[project]
name = "mdl-ynor-framework"
version = "0.1.0"
description = "Operational packaging for the MDL Ynor core runtime and API surface."
readme = "02_B_MIROIR_FONDATION_MIROIR_TEXTUEL_MDL_YNOR_FRAMEWORK_ENV.md"
requires-python = ">=3.10"

[tool.setuptools]
include-package-data = true

[tool.setuptools.packages.find]
include = ["_04_DEPLOYMENT_AND_API*"]

[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]

[tool.ruff]
target-version = "py310"
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I"]

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
