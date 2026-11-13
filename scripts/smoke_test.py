import sys
from fastapi.testclient import TestClient
from src.app import app

with TestClient(app) as client:
    response = client.get("/generate", params={"text": "Hello"})
    assert response.status_code == 200
    assert response.json() == [{"generated_text": "Hello [fixture]"}]
    metrics = client.get("/metrics")
    assert metrics.status_code == 200
    assert "request_count_total 1.0" in metrics.text
    assert "transformers" not in sys.modules
