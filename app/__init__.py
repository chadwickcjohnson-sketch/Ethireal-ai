# Ethireal AI Operations Guide

## Local execution

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Docker

```bash
docker build -t ethireal-ai .
docker run -p 8000:8000 ethireal-ai
```

## Workflow execution flow

1. Define a workflow name
2. Pass owner and context payload
3. Orchestrator executes steps
4. Status and summary are returned
5. Dashboard can summarize operational health

## Operational principles

- keep workflows clear and modular
- assign ownership to each business task
- treat automation as an execution layer, not just a prompt wrapper
- measure success using workflow completion and business impact

## Business use

Useful for tasks like:
- internal daily briefings
- lead routing
- issue prioritization
- project operations oversight
- recurring business tasks
