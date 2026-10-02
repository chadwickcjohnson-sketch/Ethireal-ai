from __future__ import annotations

from typing import Any, Dict, List

from app.models import WorkflowInstance, WorkflowStep

WORKFLOW_LIBRARY: Dict[str, Dict[str, Any]] = {
    "executive_brief": {
        "description": "Generate a concise executive briefing for priority business items.",
        "steps": [
            {"name": "collect_priorities", "action": "Collect strategic priorities and internal signals."},
            {"name": "assess_risk", "action": "Identify operational risk and blocker areas."},
            {"name": "build_summary", "action": "Create a concise leadership summary and action list."},
        ],
    },
    "sales_pipeline": {
        "description": "Score and route sales leads through a pipeline workflow.",
        "steps": [
            {"name": "qualify_lead", "action": "Assess lead quality and fit."},
            {"name": "assign_owner", "action": "Assign the lead to a sales owner."},
            {"name": "schedule_followup", "action": "Plan the follow-up cadence and next action."},
        ],
    },
    "support_triage": {
        "description": "Route incoming customer issues through triage and ownership.",
        "steps": [
            {"name": "classify_issue", "action": "Classify the issue urgency and type."},
            {"name": "determine_owner", "action": "Assign team ownership for response."},
            {"name": "draft_response", "action": "Generate a response strategy and action plan."},
        ],
    },
    "ops_coordination": {
        "description": "Coordinate internal team tasks across departments.",
        "steps": [
            {"name": "capture_request", "action": "Collect the task or operational request."},
            {"name": "route_team", "action": "Identify the right team responsible for execution."},
            {"name": "estimate_timeline", "action": "Create a timeline and execution plan."},
        ],
    },
}


def list_workflows() -> List[Dict[str, Any]]:
    workflows: List[Dict[str, Any]] = []
    for name, definition in WORKFLOW_LIBRARY.items():
        workflows.append({
            "name": name,
            "description": definition["description"],
            "steps": [step["name"] for step in definition["steps"]],
        })
    return workflows


def build_workflow_instance(workflow_name: str, owner: str, context: Dict[str, Any]) -> WorkflowInstance:
    if workflow_name not in WORKFLOW_LIBRARY:
        raise ValueError(f"Unknown workflow: {workflow_name}")

    steps = [
        WorkflowStep(
            name=step["name"],
            action=step["action"],
            details={"context": context},
        )
        for step in WORKFLOW_LIBRARY[workflow_name]["steps"]
    ]

    return WorkflowInstance(
        workflow_id=f"{workflow_name}-{owner}-{len(steps)}",
        workflow_name=workflow_name,
        owner=owner,
        status="queued",
        context=context,
        steps=steps,
        result=None,
    )
