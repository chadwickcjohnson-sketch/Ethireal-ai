from __future__ import annotations

import uuid
from typing import Any, Dict, List

from app.models import WorkflowInstance, WorkflowStep

WORKFLOW_LIBRARY: Dict[str, Dict[str, Any]] = {
    "executive_brief": {
        "description": "Generate a concise executive briefing for key business priorities.",
        "steps": [
            {"name": "collect_priorities", "action": "Collect strategic priorities and business signals."},
            {"name": "assess_risk", "action": "Identify operational risks and blockers."},
            {"name": "build_summary", "action": "Create a leadership summary and next-step list."},
        ],
    },
    "sales_pipeline": {
        "description": "Score, route, and prioritize sales leads.",
        "steps": [
            {"name": "qualify_lead", "action": "Assess lead fit and urgency."},
            {"name": "assign_owner", "action": "Assign ownership to the proper team."},
            {"name": "schedule_followup", "action": "Generate the follow-up cadence and next action."},
        ],
    },
    "support_triage": {
        "description": "Triage incoming support requests and route them appropriately.",
        "steps": [
            {"name": "classify_issue", "action": "Classify severity and issue type."},
            {"name": "determine_owner", "action": "Assign ownership for resolution."},
            {"name": "draft_response", "action": "Prepare the response and next action plan."},
        ],
    },
    "ops_coordination": {
        "description": "Coordinate requests across internal teams and operations.",
        "steps": [
            {"name": "capture_request", "action": "Capture the operational request and requirements."},
            {"name": "route_team", "action": "Identify the right team or owner."},
            {"name": "estimate_timeline", "action": "Generate a realistic timeline and execution path."},
        ],
    },
}


def list_workflows() -> List[Dict[str, Any]]:
    return [
        {
            "name": name,
            "description": definition["description"],
            "steps": [step["name"] for step in definition["steps"]],
        }
        for name, definition in WORKFLOW_LIBRARY.items()
    ]


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
        workflow_id=f"{workflow_name}-{owner}-{uuid.uuid4().hex[:8]}",
        workflow_name=workflow_name,
        owner=owner,
        status="queued",
        context=context,
        steps=steps,
        result=None,
    )
