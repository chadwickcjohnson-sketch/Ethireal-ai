from __future__ import annotations

from typing import Any, Dict, List


class ReportingService:
    def dashboard_summary(self, workflow_history: List[Dict[str, Any]]) -> Dict[str, Any]:
        completed = sum(1 for item in workflow_history if item.get("status") == "completed")
        running = sum(1 for item in workflow_history if item.get("status") == "running")
        failed = sum(1 for item in workflow_history if item.get("status") == "failed")

        return {
            "total_workflows": len(workflow_history),
            "completed": completed,
            "running": running,
            "failed": failed,
            "business_health": "stable" if completed >= running else "watchlist",
        }
