from fastapi import FastAPI
from transformers import pipeline
import prometheus_client

app = FastAPI()
llm = pipeline('text-generation', model='gpt2')
REQUEST_COUNT = prometheus_client.Counter('request_count', 'Total LLM requests')

@app.get('/generate')
def generate(text: str):
    REQUEST_COUNT.inc()
    return llm(text)
