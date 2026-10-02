from __future__ import annotations

from typing import Any, Dict

from app.models import WorkflowInstance, WorkflowStep


class AutomationOrchestrator:
    def __init__(self):
        self.execution_log: Dict[str, WorkflowInstance] = {}

    def run(self, workflow: WorkflowInstance) -> WorkflowInstance:
        workflow.status = "running"

        for step in workflow.steps:
            step.status = "running"
            step.details["status"] = "in_progress"
            step.details["message"] = f"Executing {step.name}"

            # Simulated operational step processing
            if step.name == "collect_priorities":
                step.details["priority_summary"] = workflow.context.get("priorities", ["business operations"])
            elif step.name == "qualify_lead":
                step.details["lead_fit"] = workflow.context.get("lead_score", 80)
            elif step.name == "classify_issue":
                step.details["issue_severity"] = workflow.context.get("severity", "medium")
            elif step.name == "capture_request":
                step.details["request"] = workflow.context.get("request", "pending review")

            step.status = "completed"
            step.details["status"] = "completed"
            step.details["message"] = f"Completed {step.name}"

        workflow.status = "completed"
        workflow.result = {
            "workflow_name": workflow.workflow_name,
            "owner": workflow.owner,
            "summary": self._build_summary(workflow),
            "status": workflow.status,
        }
        self.execution_log[workflow.workflow_id] = workflow
        return workflow

    def get_status(self, workflow_id: str) -> WorkflowInstance:
        return self.execution_log[workflow_id]

    def _build_summary(self, workflow: WorkflowInstance) -> Dict[str, Any]:
        return {
            "workflow_id": workflow.workflow_id,
            "context": workflow.context,
            "completed_steps": [step.name for step in workflow.steps if step.status == "completed"],
            "next_action": "Review outcome and assign execution owners as needed.",
        }
