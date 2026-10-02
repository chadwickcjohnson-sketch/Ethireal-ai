# Ethireal AI Operations Guide

## Local startup

```bash
python scripts/start.sh
```

## Service health

```bash
curl http://localhost:8000/health
```

## Workflow test

```bash
curl -X POST http://localhost:8000/workflows/executive_brief \
  -H "Content-Type: application/json" \
  -d '{"owner":"ceo","context":{"team":"leadership","priorities":["pipeline","operations"]}}'
```

## Fail-safe

The self-healing script and startup script are designed to recover service faults automatically during startup or unexpected exits.
