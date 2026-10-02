# Ethireal AI

Automation in full.

Ethireal AI is an AI-powered business operating system built to help founders, executives, and teams automate the real work of running a business. It combines AI orchestration, workflow automation, business context, reporting, and operational intelligence into one execution layer.

This repository is now structured as a real operational workflow foundation for an AI-driven business platform.

## Product vision

Ethireal AI turns fragmented work into a coordinated system. It supports:
- executive briefings and strategic review workflows
- sales pipeline coordination and follow-up automation
- customer support triage and response workflows
- internal operations task routing and execution
- reporting, summaries, and action tracking
- business process automation across multiple teams

## Platform concept

The platform is designed as a layered business operating system:
- orchestration layer
- AI reasoning and planning layer
- workflow execution engine
- integration layer
- memory and context layer
- reporting and analytics layer

## Operational workflow model

The project includes reusable workflow patterns such as:
- executive brief workflow
- sales pipeline workflow
- customer support triage workflow
- operations coordination workflow

## Repository structure

```text
app/
  __init__.py
  config.py
  main.py
  models.py
  workflows.py
  services/
    __init__.py
    automation.py
    reporting.py

docs/
  architecture.md
  roadmap.md
  monetization.md
  operations.md

requirements.txt
Dockerfile
compose.yaml
.env.example
Makefile
LICENSE
README.md
```

## Quick start

### 1) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

### 3) Run the API

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4) Test the health endpoint

```bash
curl http://localhost:8000/health
```

## API endpoints

### Health

```bash
GET /health
```

### List workflows

```bash
GET /workflows
```

### Run workflow

```bash
POST /workflows/executive_brief
{
  "owner": "ceo",
  "context": {
    "team": "leadership",
    "business_focus": "growth and efficiency",
    "priorities": ["pipeline", "operations", "retention"]
  }
}
```

### Workflow status

```bash
GET /workflows/{workflow_id}/status
```

### Dashboard summary

```bash
GET /dashboard
```

## Business model

Ethireal AI is designed to scale through a practical monetization mix:
- hosted SaaS subscriptions
- premium enterprise deployment
- custom workflow design and onboarding
- white-label automation for agencies and consultants
- implementation services for founder-led businesses

## License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).

## Summary

Ethireal AI is now structured as an operational AI automation system with a runnable backend, workflow engine, environment config, and business-ready architecture that can evolve into a real product.

Built for automation. Built for scale. Built for execution.
