# Ethireal AI API Contract

## Base URL

Local development:
http://localhost:8000

## Endpoints

### GET /health
Returns service health status.

Example response:
{
  "status": "ok",
  "service": "Ethireal AI",
  "mode": "operational"
}

### GET /workflows
Returns available workflow definitions.

Example response:
{
  "workflows": [
    {
      "name": "executive_brief",
      "description": "Generate a concise executive briefing for key business priorities.",
      "steps": ["collect_priorities", "assess_risk", "build_summary"]
    }
  ]
}

### POST /workflows/{workflow_name}
Starts a workflow execution.

Request body:
{
  "owner": "ceo",
  "context": {
    "team": "leadership",
    "business_focus": "growth and efficiency",
    "priorities": ["pipeline", "operations", "retention"]
  }
}

Example response:
{
  "workflow_id": "executive_brief-ceo-abc12345",
  "status": "completed",
  "summary": {
    "workflow_name": "executive_brief",
    "owner": "ceo",
    "summary": {
      "workflow_id": "executive_brief-ceo-abc12345",
      "context": {
        "team": "leadership"
      },
      "completed_steps": ["collect_priorities", "assess_risk", "build_summary"],
      "next_action": "Review the workflow result and assign ownership for execution or follow-up."
    },
    "status": "completed"
  }
}

### GET /workflows/{workflow_id}/status
Returns workflow execution status and steps.

### GET /dashboard
Returns operational summary metrics.

Example response:
{
  "total_workflows": 10,
  "completed": 7,
  "running": 1,
  "failed": 2,
  "business_health": "stable"
}

## Error handling

Expected HTTP errors:
- 404: workflow not found or invalid workflow name
- 422: invalid request data format

## Future API additions

Planned additions:
- user authentication
- workflow templates management
- team-level dashboards
- external integration endpoints
- workflow event subscriptions
- audit/log retrieval APIs
