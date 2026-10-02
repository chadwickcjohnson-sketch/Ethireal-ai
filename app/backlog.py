from __future__ import annotations

import uuid
from datetime import datetime, timedelta
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
    "extract_pull_request": {
        "description": "Extract, validate, and process pull request data for operational review.",
        "steps": [
            {"name": "fetch_pr_data", "action": "Retrieve pull request details from repository."},
            {"name": "analyze_changes", "action": "Analyze code changes, impact, and risk level."},
            {"name": "generate_summary", "action": "Create a structured PR summary with recommendations."},
            {"name": "route_review", "action": "Assign to appropriate reviewers based on expertise."},
        ],
    },
    "ipo_process": {
        "description": "Manage IPO preparation workflow including regulatory, financial, and operational readiness.",
        "steps": [
            {"name": "assess_readiness", "action": "Evaluate financial, operational, and compliance readiness."},
            {"name": "gather_documentation", "action": "Compile required regulatory and financial documentation."},
            {"name": "coordinate_stakeholders", "action": "Coordinate with legal, auditors, underwriters, and leadership."},
            {"name": "build_timeline", "action": "Create detailed IPO timeline and milestone tracking."},
            {"name": "generate_report", "action": "Generate comprehensive IPO readiness report."},
        ],
    },
    "backlog_historical_review": {
        "description": "Process and review historical backlog items from 2021 to current date.",
        "steps": [
            {"name": "fetch_historical_data", "action": "Retrieve all backlog items from 2021 onwards."},
            {"name": "categorize_items", "action": "Categorize by priority, status, and business impact."},
            {"name": "assess_completion", "action": "Determine which items are complete, pending, or obsolete."},
            {"name": "identify_gaps", "action": "Identify critical gaps and unresolved technical debt."},
            {"name": "generate_insights", "action": "Generate actionable insights and recommendations."},
            {"name": "create_action_plan", "action": "Build prioritized action plan for remaining work."},
        ],
    },
    "extract_financial_data": {
        "description": "Extract and aggregate financial data for business analysis and reporting.",
        "steps": [
            {"name": "extract_metrics", "action": "Extract key financial metrics and KPIs."},
            {"name": "validate_data", "action": "Validate data accuracy and consistency."},
            {"name": "aggregate_reports", "action": "Aggregate data into financial reports."},
            {"name": "identify_trends", "action": "Identify financial trends and anomalies."},
            {"name": "generate_summary", "action": "Create executive financial summary."},
        ],
    },
    "extract_operational_metrics": {
        "description": "Extract and analyze operational metrics and performance indicators.",
        "steps": [
            {"name": "collect_metrics", "action": "Collect operational metrics from all systems."},
            {"name": "normalize_data", "action": "Normalize data for consistent analysis."},
            {"name": "analyze_performance", "action": "Analyze performance against targets."},
            {"name": "identify_bottlenecks", "action": "Identify operational bottlenecks and inefficiencies."},
            {"name": "build_dashboard", "action": "Build real-time operational dashboard."},
        ],
    },
    "extract_customer_insights": {
        "description": "Extract and synthesize customer data for business intelligence.",
        "steps": [
            {"name": "gather_customer_data", "action": "Gather customer feedback, usage, and churn data."},
            {"name": "segment_analysis", "action": "Segment customers by value, churn risk, and growth potential."},
            {"name": "identify_patterns", "action": "Identify patterns in customer behavior and satisfaction."},
            {"name": "generate_insights", "action": "Generate actionable customer insights."},
            {"name": "build_recommendations", "action": "Build product and retention recommendations."},
        ],
    },
    "extract_team_productivity": {
        "description": "Extract and analyze team productivity and engagement metrics.",
        "steps": [
            {"name": "collect_productivity_data", "action": "Collect productivity metrics from work systems."},
            {"name": "measure_engagement", "action": "Measure team engagement and satisfaction."},
            {"name": "identify_challenges", "action": "Identify productivity challenges and constraints."},
            {"name": "benchmark_performance", "action": "Benchmark against industry standards."},
            {"name": "generate_report", "action": "Generate team productivity and health report."},
        ],
    },
}

# Historical backlog data from 2021 to current
HISTORICAL_BACKLOG_DATA = [
    {
        "id": f"BACKLOG-2021-{i:04d}",
        "title": f"Historical initiative {i} from 2021",
        "date_created": datetime(2021, 1, 15) + timedelta(days=i*7),
        "status": "completed" if i % 3 == 0 else "pending" if i % 3 == 1 else "archived",
        "priority": "high" if i % 5 == 0 else "medium" if i % 5 == 1 else "low",
        "business_impact": "critical" if i % 7 == 0 else "high" if i % 7 == 1 else "medium",
        "category": ["infrastructure", "feature", "optimization", "security", "debt"][i % 5],
    }
    for i in range(1, 157)  # ~3 years of weekly items from 2021 to Oct 2023
]

# Additional backlog items from 2024 to present
for i in range(157, 210):
    HISTORICAL_BACKLOG_DATA.append({
        "id": f"BACKLOG-2024-{i:04d}",
        "title": f"Current initiative {i} from 2024",
        "date_created": datetime(2024, 1, 15) + timedelta(days=(i-157)*7),
        "status": "running" if i % 4 == 0 else "pending" if i % 4 == 1 else "in_review",
        "priority": "high" if i % 6 == 0 else "medium" if i % 6 == 1 else "low",
        "business_impact": "critical" if i % 8 == 0 else "high" if i % 8 == 1 else "medium",
        "category": ["infrastructure", "feature", "optimization", "security", "debt"][i % 5],
    })


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


def get_historical_backlog(start_year: int = 2021, end_year: int = 2024) -> List[Dict[str, Any]]:
    """Retrieve historical backlog items within the specified date range."""
    filtered_backlog = [
        item for item in HISTORICAL_BACKLOG_DATA
        if start_year <= item["date_created"].year <= end_year
    ]
    return sorted(filtered_backlog, key=lambda x: x["date_created"], reverse=True)


def get_backlog_summary() -> Dict[str, Any]:
    """Get a summary of the historical backlog."""
    total_items = len(HISTORICAL_BACKLOG_DATA)
    completed = sum(1 for item in HISTORICAL_BACKLOG_DATA if item["status"] == "completed")
    pending = sum(1 for item in HISTORICAL_BACKLOG_DATA if item["status"] == "pending")
    running = sum(1 for item in HISTORICAL_BACKLOG_DATA if item["status"] == "running")
    archived = sum(1 for item in HISTORICAL_BACKLOG_DATA if item["status"] == "archived")

    return {
        "total_items": total_items,
        "completed": completed,
        "pending": pending,
        "running": running,
        "archived": archived,
        "completion_rate": round(completed / total_items * 100, 2) if total_items > 0 else 0,
        "date_range": {
            "start": "2021-01-15",
            "end": datetime.now().strftime("%Y-%m-%d"),
        },
    }
