# Operations Runbook

## Startup

```bash
python scripts/start.sh
```

## Validate

- check /health
- test /workflows
- run a workflow
- inspect /dashboard

## Recovery

The self-healing startup layer will retry the app when the runtime is unstable.
