# MLOps LLM Pipeline

A local inference API with a deterministic fixture and Prometheus metrics. Set MLOPS_GPT2=1 and install the optional model dependencies to try GPT-2. CI uses the offline fixture. The retraining script is an unfinished experiment.

## Run the example

```sh
python -m pip install -c requirements.lock -r requirements.txt
python -m uvicorn src.app:app --host 127.0.0.1 --port 8000
```

In another terminal:

```sh
curl 'http://127.0.0.1:8000/generate?text=hello'
```

Expected result: a JSON list containing `generated_text` with `hello [fixture]`.
Metrics are available at `/metrics`. To try the optional model path, install `requirements-model.txt` in a separate environment, then start with `MLOPS_GPT2=1`. That path can download model files and needs separate verification.

## Deployment verification

Use Python 3.12 on Linux. CI and the container use the checked-in dependency constraints.

```sh
python -m pip install -c requirements.lock -r requirements-dev.txt
python -m pytest -q
docker build -t reviewer-smoke .
docker run --rm -p 127.0.0.1:8000:8000 reviewer-smoke
```

The container serves the API docs at `http://127.0.0.1:8000/docs`. Use the local example above to exercise its main route. Use synthetic inputs. Shared deployment requires authentication, resource limits, and operational verification.
