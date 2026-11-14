from fastapi.testclient import TestClient

from src.app import app


def test_offline_generation_and_metrics(monkeypatch):
    monkeypatch.delenv("MLOPS_GPT2", raising=False)
    client = TestClient(app)
    assert client.get("/generate", params={"text": "hello"}).json() == [
        {"generated_text": "hello [fixture]"}
    ]
    assert client.get("/generate", params={"text": ""}).status_code == 422
    assert "request_count_total" in client.get("/metrics").text
