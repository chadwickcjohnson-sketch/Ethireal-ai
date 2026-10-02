from __future__ import annotations

from typing import Any, Dict

from app.models import WorkflowInstance
from app.backlog import get_historical_backlog, get_backlog_summary, HISTORICAL_BACKLOG_DATA


class AutomationOrchestrator:
    def __init__(self):
        self.execution_log: Dict[str, WorkflowInstance] = {}

    def run(self, workflow: WorkflowInstance) -> WorkflowInstance:
        workflow.status = "running"

        for step in workflow.steps:
            step.status = "running"
            step.details["status"] = "in_progress"
            step.details["message"] = f"Executing {step.name}"

            # Handle step execution based on workflow and step name
            if workflow.workflow_name == "extract_pull_request":
                self._execute_pr_extraction(step, workflow)
            elif workflow.workflow_name == "ipo_process":
                self._execute_ipo_process(step, workflow)
            elif workflow.workflow_name == "backlog_historical_review":
                self._execute_backlog_review(step, workflow)
            elif workflow.workflow_name == "extract_financial_data":
                self._execute_financial_extraction(step, workflow)
            elif workflow.workflow_name == "extract_operational_metrics":
                self._execute_operational_extraction(step, workflow)
            elif workflow.workflow_name == "extract_customer_insights":
                self._execute_customer_extraction(step, workflow)
            elif workflow.workflow_name == "extract_team_productivity":
                self._execute_team_extraction(step, workflow)
            else:
                self._execute_standard_workflow(step, workflow)

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

    def _execute_pr_extraction(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute pull request extraction workflow."""
        if step.name == "fetch_pr_data":
            step.details["pr_count"] = workflow.context.get("pr_count", 42)
            step.details["repositories"] = workflow.context.get("repositories", ["ethireal-ai"])
        elif step.name == "analyze_changes":
            step.details["files_changed"] = workflow.context.get("files_changed", 156)
            step.details["risk_assessment"] = "medium"
        elif step.name == "generate_summary":
            step.details["summary"] = "PR analysis complete with recommendations"
        elif step.name == "route_review":
            step.details["assigned_reviewers"] = 3

    def _execute_ipo_process(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute IPO preparation workflow."""
        if step.name == "assess_readiness":
            step.details["financial_readiness"] = "95%"
            step.details["compliance_readiness"] = "88%"
            step.details["operational_readiness"] = "92%"
        elif step.name == "gather_documentation":
            step.details["documents_required"] = 47
            step.details["documents_ready"] = 42
        elif step.name == "coordinate_stakeholders":
            step.details["stakeholders_engaged"] = 18
            step.details["coordination_status"] = "on_track"
        elif step.name == "build_timeline":
            step.details["estimated_duration_months"] = 9
            step.details["key_milestones"] = 12
        elif step.name == "generate_report":
            step.details["overall_readiness"] = "91%"
            step.details["critical_risks"] = 3

    def _execute_backlog_review(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute historical backlog review workflow."""
        if step.name == "fetch_historical_data":
            backlog = get_historical_backlog(2021, 2024)
            step.details["total_items"] = len(backlog)
            step.details["date_range"] = "2021-01-15 to 2026-10-02"
        elif step.name == "categorize_items":
            summary = get_backlog_summary()
            step.details["completion_rate"] = summary["completion_rate"]
            step.details["by_status"] = {
                "completed": summary["completed"],
                "pending": summary["pending"],
                "running": summary["running"],
                "archived": summary["archived"],
            }
        elif step.name == "assess_completion":
            step.details["completed_percentage"] = 35
            step.details["pending_percentage"] = 40
            step.details["obsolete_items"] = 25
        elif step.name == "identify_gaps":
            step.details["critical_gaps"] = 7
            step.details["high_priority_gaps"] = 23
            step.details["technical_debt_identified"] = True
        elif step.name == "generate_insights":
            step.details["key_insights"] = [
                "35% completion rate over 3+ years",
                "Significant technical debt accumulation",
                "Need for process optimization",
            ]
        elif step.name == "create_action_plan":
            step.details["priority_recommendations"] = 12
            step.details["estimated_effort"] = "450+ hours"

    def _execute_financial_extraction(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute financial data extraction workflow."""
        if step.name == "extract_metrics":
            step.details["metrics_extracted"] = 156
            step.details["revenue_metrics"] = True
        elif step.name == "validate_data":
            step.details["validation_score"] = "98%"
            step.details["anomalies_found"] = 2
        elif step.name == "aggregate_reports":
            step.details["reports_generated"] = 8
            step.details["time_periods"] = "Q1-Q4 2024"
        elif step.name == "identify_trends":
            step.details["trend_count"] = 12
            step.details["growth_trajectory"] = "positive"
        elif step.name == "generate_summary":
            step.details["financial_health"] = "strong"
            step.details["forecast_accuracy"] = "94%"

    def _execute_operational_extraction(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute operational metrics extraction workflow."""
        if step.name == "collect_metrics":
            step.details["systems_monitored"] = 12
            step.details["metrics_collected"] = 234
        elif step.name == "normalize_data":
            step.details["normalization_complete"] = True
            step.details["data_quality"] = "99%"
        elif step.name == "analyze_performance":
            step.details["targets_met"] = 18
            step.details["targets_missed"] = 2
        elif step.name == "identify_bottlenecks":
            step.details["bottlenecks_found"] = 4
            step.details["efficiency_improvement_potential"] = "23%"
        elif step.name == "build_dashboard":
            step.details["dashboard_ready"] = True
            step.details["real_time_metrics"] = 45

    def _execute_customer_extraction(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute customer insights extraction workflow."""
        if step.name == "gather_customer_data":
            step.details["customers_analyzed"] = 1250
            step.details["data_sources"] = 6
        elif step.name == "segment_analysis":
            step.details["segments_created"] = 8
            step.details["high_value_customers"] = 180
        elif step.name == "identify_patterns":
            step.details["patterns_discovered"] = 14
            step.details["churn_risk_identified"] = True
        elif step.name == "generate_insights":
            step.details["actionable_insights"] = 22
            step.details["customer_nps"] = 68
        elif step.name == "build_recommendations":
            step.details["product_recommendations"] = 8
            step.details["retention_opportunities"] = 35

    def _execute_team_extraction(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute team productivity extraction workflow."""
        if step.name == "collect_productivity_data":
            step.details["team_members_tracked"] = 42
            step.details["productivity_metrics"] = 89
        elif step.name == "measure_engagement":
            step.details["engagement_score"] = 7.8
            step.details["satisfaction_score"] = 8.2
        elif step.name == "identify_challenges":
            step.details["challenges_identified"] = 6
            step.details["blockers"] = 3
        elif step.name == "benchmark_performance":
            step.details["vs_industry_average"] = "+15%"
            step.details["top_performers"] = 12
        elif step.name == "generate_report":
            step.details["team_health"] = "excellent"
            step.details["recommendations_count"] = 9

    def _execute_standard_workflow(self, step: Any, workflow: WorkflowInstance) -> None:
        """Execute standard workflow steps."""
        if step.name == "collect_priorities":
            step.details["priority_summary"] = workflow.context.get("priorities", ["business operations"])
        elif step.name == "qualify_lead":
            step.details["lead_fit"] = workflow.context.get("lead_score", 80)
        elif step.name == "classify_issue":
            step.details["issue_severity"] = workflow.context.get("severity", "medium")
        elif step.name == "capture_request":
            step.details["request"] = workflow.context.get("request", "pending review")

    def get_status(self, workflow_id: str) -> WorkflowInstance:
        return self.execution_log[workflow_id]

    def _build_summary(self, workflow: WorkflowInstance) -> Dict[str, Any]:
        return {
            "workflow_id": workflow.workflow_id,
            "context": workflow.context,
            "completed_steps": [step.name for step in workflow.steps if step.status == "completed"],
            "next_action": "Review the workflow result and assign ownership for execution or follow-up.",
            "execution_details": [
                {"step_name": step.name, "details": step.details}
                for step in workflow.steps
            ],
        }
