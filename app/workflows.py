from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Literal, Optional

WorkflowStatus = Literal["queued", "running", "completed", "failed"]
StepStatus = Literal["pending", "running", "completed", "failed"]


@dataclass
class WorkflowStep:
    name: str
    action: str
    status: StepStatus = "pending"
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowInstance:
    workflow_id: str
    workflow_name: str
    owner: str
    status: WorkflowStatus = "queued"
    context: Dict[str, Any] = field(default_factory=dict)
    steps: List[WorkflowStep] = field(default_factory=list)
    result: Optional[Dict[str, Any]] = None
