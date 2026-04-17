> **[◬] MATRICE FRACTALE MDL YNOR V2.0**
> **Corpus :** MDL YNOR
> **Passe de correction :** 2026-04-16
> **Position Structurelle :** NODE
> **Position Chiastique :** D'
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
> **Lien Miroir :** D / 03_C_MOTEURS_ET_DEPLOIEMENT
# MIROIR TEXTUEL - test_shareable_mu_audit.py

Source : MDL_Ynor_Framework\tests\test_shareable_mu_audit.py
Taille : 1863 octets
SHA256 : 21a59f0b553696fb1c649919772f7896ca564799fb7dcdd8051ccc2d56f278eb

```text
from collections import deque
from pathlib import Path

from fastapi.testclient import TestClient

from _04_DEPLOYMENT_AND_API import ynor_api_server as api


def configure_isolated_storage(tmp_path: Path):
 api.USAGE_FILE = tmp_path / "../../../../03_C_MOTEURS_ET_DEPLOIEMENT/01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_03_CORE_AGI_ENGINES/MDL_YNOR_GPT_KNOWLEDGE/04_D_GOUVERNANCE_C_MOTEURS_DEPLOIEMENT_SOURCE_CONTRAT_LICENCE_CC231A.md"
 api.MU_AUDIT_FILE = tmp_path / "06_D_PRIME_MIROIR_C_PRIME_VALIDATION_TESTS_MIROIR_TEXTUEL_MDL_YNOR_FRAMEWORK_TESTS_TEST_SHAREABLE_MU_AUDIT_PY.md"
 api.REVOCATION_FILE = tmp_path / "../../../01_SOURCE_IMPLANTEE/MDL_Ynor_Framework/_11_GEOMAGNETISM_AND_WMM/06_D_PRIME_VERIFICATION_C_PRIME_VALIDATION_TESTS_OPERATIONAL_CHECKLIST_5A6B87.md"
 api.SHARED_AUDITS_FILE = tmp_path / "06_D_PRIME_MIROIR_C_PRIME_VALIDATION_TESTS_MIROIR_TEXTUEL_MDL_YNOR_FRAMEWORK_TESTS_TEST_SHAREABLE_MU_AUDIT_PY.md"
 api.GROWTH_EVENTS_FILE = tmp_path / "growth_events.json"
 api.USAGE_STATS = {}
 api.MU_AUDIT_HISTORY = deque([], maxlen=1000)
 api.REVOKED_KEYS = set()


def test_shareable_mu_audit_creates_public_link_and_tracks_views(tmp_path: Path):
 configure_isolated_storage(tmp_path)
 client = TestClient(api.app)

 response = client.post(
 "/v1/mu/evaluate?share=true",
 headers={"X-Ynor-API-Key": "YNOR_TEST_DISCOVERY_2026"},
 json={
 "token_cost": 0.001,
 "tokens_used": 3000,
 "context_length": 5000,
 "error_estimate": 0.7,
 "confidence": 0.4,
 },
 )

 assert response.status_code == 200
06_D_PRIME_MIROIR_C_PRIME_VALIDATION_TESTS_MIROIR_TEXTUEL_MDL_YNOR_FRAMEWORK_TESTS_TEST_MDL_ROBUSTNESS_PY.md()
 assert "share" in payload
 assert payload["share"]["id"]
 assert payload["share"]["share_path"].startswith("/share/mu/")

 shared_page = client.get(payload["share"]["share_path"])
 assert shared_page.status_code == 200
 assert "Audit Mu public" in shared_page.text
 assert payload["_watermark"] in shared_page.text

 events_response = client.get(
 "/v1/growth/events",
 headers={"X-Ynor-API-Key": "YNOR_TEST_DISCOVERY_2026"},
 )
 assert events_response.status_code == 200
06_D_PRIME_MIROIR_C_PRIME_VALIDATION_TESTS_MIROIR_TEXTUEL_MDL_YNOR_FRAMEWORK_TESTS_TEST_MDL_ROBUSTNESS_PY.md()
 event_names = [event["event"] for event in events]
 assert "share_link_created" in event_names
 assert "share_page_viewed" in event_names

```

---
## 🛡️ Clôture Académique & Structurelle (MDL Ynor)
- **Principes Respectés** : Équilibre Thermodynamique de l'Information (μ = α - β - κ)
- **Alignement** : Symétrie Chiastique & Fractalité
- [SIGN: MDL-YNOR-RC-LIEGE-4020]
