from __future__ import annotations

from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.config import APP_DEBUG, APP_HOST, APP_NAME, APP_PORT
from app.services.automation import AutomationOrchestrator
from app.services.reporting import ReportingService
from app.workflows import build_workflow_instance, list_workflows
from app.backlog import get_historical_backlog, get_backlog_summary

app = FastAPI(
    title=APP_NAME,
    version="0.2.0",
    description="Ethireal AI operational workflow engine with extended automation and backlog management.",
    debug=APP_DEBUG,
)

orchestrator = AutomationOrchestrator()
reporting = ReportingService()
workflow_history: List[Dict[str, Any]] = []


class WorkflowRequest(BaseModel):
    owner: str = Field(..., description="Owner or team responsible for workflow execution.")
    context: Dict[str, Any] = Field(default_factory=dict, description="Workflow context and execution data.")


@app.get("/health")
def health() -> Dict[str, Any]:
    return {
        "status": "ok",
        "service": APP_NAME,
        "mode": "operational",
        "version": "0.2.0",
    }


@app.get("/workflows")
def get_workflows() -> Dict[str, Any]:
    workflows = list_workflows()
    return {
        "total_workflows": len(workflows),
        "workflows": workflows,
    }


@app.post("/workflows/{workflow_name}")
def run_workflow(workflow_name: str, payload: WorkflowRequest) -> Dict[str, Any]:
    try:
        workflow = build_workflow_instance(workflow_name, payload.owner, payload.context)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    workflow = orchestrator.run(workflow)
    workflow_history.append({
        "workflow_id": workflow.workflow_id,
        "workflow_name": workflow.workflow_name,
        "owner": workflow.owner,
        "status": workflow.status,
    })

    return {
        "workflow_id": workflow.workflow_id,
        "status": workflow.status,
        "summary": workflow.result,
    }


@app.get("/workflows/{workflow_id}/status")
def workflow_status(workflow_id: str) -> Dict[str, Any]:
    workflow = orchestrator.execution_log.get(workflow_id)
    if workflow is None:
        raise HTTPException(status_code=404, detail="Workflow not found")

    return {
        "workflow_id": workflow.workflow_id,
        "workflow_name": workflow.workflow_name,
        "owner": workflow.owner,
        "status": workflow.status,
        "steps": [
            {
                "name": step.name,
                "action": step.action,
                "status": step.status,
                "details": step.details,
            }
            for step in workflow.steps
        ],
        "result": workflow.result,
    }


@app.get("/dashboard")
def dashboard() -> Dict[str, Any]:
    return reporting.dashboard_summary(workflow_history)


@app.get("/backlog")
def backlog_summary() -> Dict[str, Any]:
    """Get summary of historical backlog from 2021 to present."""
    return get_backlog_summary()


@app.get("/backlog/items")
def backlog_items(year_start: int = 2021, year_end: int = 2024, status: str | None = None) -> Dict[str, Any]:
    """Retrieve backlog items within date range, optionally filtered by status."""
    items = get_historical_backlog(year_start, year_end)
    
    if status:
        items = [item for item in items if item["status"] == status]
    
    return {
        "count": len(items),
        "date_range": {"start": year_start, "end": year_end},
        "filter_status": status,
        "items": items,
    }


@app.get("/backlog/analysis")
def backlog_analysis() -> Dict[str, Any]:
    """Get detailed analysis of backlog including trends and insights."""
    summary = get_backlog_summary()
    items = get_historical_backlog(2021, 2024)
    
    # Analyze by category
    categories = {}
    for item in items:
        cat = item["category"]
        if cat not in categories:
            categories[cat] = {"count": 0, "completed": 0, "pending": 0}
        categories[cat]["count"] += 1
        if item["status"] == "completed":
            categories[cat]["completed"] += 1
        elif item["status"] == "pending":
            categories[cat]["pending"] += 1
    
    # Analyze by priority
    priorities = {}
    for item in items:
        pri = item["priority"]
        if pri not in priorities:
            priorities[pri] = {"count": 0, "completed": 0}
        priorities[pri]["count"] += 1
        if item["status"] == "completed":
            priorities[pri]["completed"] += 1
    
    return {
        "summary": summary,
        "analysis_by_category": categories,
        "analysis_by_priority": priorities,
        "insights": {
            "completion_rate": summary["completion_rate"],
            "pending_items": summary["pending"],
            "critical_items": sum(1 for i in items if i["business_impact"] == "critical"),
            "total_span_years": 3,
        },
    }


@app.on_event("startup")
def startup_event() -> None:
    # self-heal startup check: ensure the service environment is operational
    if not APP_HOST or not APP_PORT:
        raise RuntimeError("Invalid runtime configuration")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host=APP_HOST, port=APP_PORT, reload=APP_DEBUG)
