# **[◬] MATRICE FRACTALE MDL YNOR V2.0**
# **Corpus :** MDL YNOR
# **Position Structurelle :** NODE
# **Position Chiastique :** E
# **Rôle du Fichier :** Audit structurel et controle d'integrite
# **Centre Doctrinal Local :** AI Manager garde audit structurel et controle d'integrite en limitant le bruit local et la friction structurelle.
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

from fastapi.testclient import TestClient

from _04_DEPLOYMENT_AND_API import ynor_api_server as api


def configure_isolated_storage(tmp_path: Path):
    api.USAGE_FILE = tmp_path / "usage_stats.json"
    api.MU_AUDIT_FILE = tmp_path / "mu_audit_history.json"
    api.REVOCATION_FILE = tmp_path / "revocation_list.json"
    api.SHARED_AUDITS_FILE = tmp_path / "shared_audits.json"
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
    payload = response.json()
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
    events = events_response.json()
    event_names = [event["event"] for event in events]
    assert "share_link_created" in event_names
    assert "share_page_viewed" in event_names
