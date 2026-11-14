from functools import lru_cache
import os

from fastapi import FastAPI, Query, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest

app = FastAPI()
REQUEST_COUNT = Counter("request_count", "Total LLM requests")


@lru_cache(maxsize=1)
def load_model():
    from transformers import pipeline

    return pipeline("text-generation", model="gpt2")


@app.get("/generate")
def generate(text: str = Query(min_length=1, max_length=1000)):
    REQUEST_COUNT.inc()
    if os.environ.get("MLOPS_GPT2") == "1":
        return load_model()(text, max_new_tokens=32)
    return [{"generated_text": f"{text} [fixture]"}]


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
