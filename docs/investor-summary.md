# Ethireal AI Operations Runbook

## Purpose

This runbook provides the minimum operational guidance needed to run and maintain the Ethireal AI workflow foundation.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Health checks

- verify the service is running on port 8000
- check /health for service status
- validate workflow list on /workflows
- run a sample workflow request

## Workflow validation checklist

- workflow name exists
- request payload includes owner
- context data is valid
- status is updated from queued to running to completed
- result contains a summary and next action

## Monitoring considerations

Monitor:
- workflow completion rate
- number of failed executions
- workflow duration
- common request errors
- service uptime

## Common issues

### Import errors
Check whether dependencies were installed correctly.

### Workflow not found
Verify the workflow name matches one defined in app/workflows.py.

### API startup issues
Check environment variables and ensure ports are free.

## Suggested future improvements

- async task execution
- database persistence
- better logs and audit tracking
- operational metrics dashboard
- user and team authorization

## Ownership model

Each workflow should have a clear operational owner. This is essential for turning automation into an execution system rather than a disconnected tool.
