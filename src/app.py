from functools import lru_cache
import os

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = FastAPI()
REQUEST_COUNT = Counter("request_count", "Total LLM requests")


@lru_cache(maxsize=1)
def get_model():
    from transformers import pipeline

    return pipeline("text-generation", model="gpt2")


@app.get("/generate")
def generate(text: str):
    REQUEST_COUNT.inc()
    if os.environ.get("LLM_FIXTURE_MODE") == "1":
        return [{"generated_text": text + " [fixture]"}]
    return get_model()(text)


@app.get("/metrics")
def metrics():
    return Response(content=generate_latest(), headers={"Content-Type": CONTENT_TYPE_LATEST})
