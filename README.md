# MLOps LLM Pipeline

A FastAPI text-generation example with a Prometheus request counter, a Docker
image definition, and a retraining scaffold.

## Try the API without a model download

```bash
python -m pip install fastapi uvicorn prometheus-client
LLM_FIXTURE_MODE=1 python -m uvicorn src.app:app --host 127.0.0.1 --port 8000
```

In a second terminal:

```bash
curl 'http://127.0.0.1:8000/generate?text=Hello'
curl 'http://127.0.0.1:8000/metrics'
```

The first request returns `[{"generated_text":"Hello [fixture]"}]`. The
metrics output includes `request_count_total`.

## Run the automated smoke test

From the repository root:

```bash
python -m pip install fastapi prometheus-client httpx
LLM_FIXTURE_MODE=1 python -m scripts.smoke_test
```

In PowerShell, set `$env:LLM_FIXTURE_MODE = "1"` before running the Python
command. The same check runs in GitHub Actions on pull requests.

## Run the GPT-2 adapter

Install the full dependencies with `python -m pip install -r requirements.txt`,
then start the server without `LLM_FIXTURE_MODE`. The first generation
request loads GPT-2, which may require downloading model files.

The Dockerfile installs the full model dependencies. The retraining script
still needs a training dataset and data preprocessing before it can run.
The deployment workflow also requires a configured Render environment.
