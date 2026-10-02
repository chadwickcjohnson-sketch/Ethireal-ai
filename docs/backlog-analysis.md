# Ethireal AI Workflow Guide

## Available Workflows

### 1. Executive Brief
Generates a concise executive briefing for key business priorities.
- Steps: collect_priorities → assess_risk → build_summary
- Use case: Daily leadership briefings, strategic reviews

### 2. Sales Pipeline
Scores, routes, and prioritizes sales leads.
- Steps: qualify_lead → assign_owner → schedule_followup
- Use case: Lead management, sales workflow automation

### 3. Support Triage
Triages incoming support requests and routes them appropriately.
- Steps: classify_issue → determine_owner → draft_response
- Use case: Customer support automation, ticket routing

### 4. Operations Coordination
Coordinates requests across internal teams and operations.
- Steps: capture_request → route_team → estimate_timeline
- Use case: Internal task coordination, project management

### 5. Extract Pull Request ⭐ NEW
Extracts, validates, and processes pull request data for operational review.
- Steps: fetch_pr_data → analyze_changes → generate_summary → route_review
- Use case: GitHub PR analysis, code review automation, team coordination
- Supports multiple repositories and change analysis

### 6. IPO Process ⭐ NEW
Manages IPO preparation workflow including regulatory, financial, and operational readiness.
- Steps: assess_readiness → gather_documentation → coordinate_stakeholders → build_timeline → generate_report
- Use case: IPO preparation, readiness assessment, stakeholder coordination
- Tracks compliance, financial, and operational readiness

### 7. Backlog Historical Review ⭐ NEW
Processes and reviews historical backlog items from 2021 to current date.
- Steps: fetch_historical_data → categorize_items → assess_completion → identify_gaps → generate_insights → create_action_plan
- Use case: Backlog analysis, technical debt assessment, historical trend review
- Analyzes 200+ items spanning 3+ years of work

### 8. Extract Financial Data ⭐ NEW
Extracts and aggregates financial data for business analysis and reporting.
- Steps: extract_metrics → validate_data → aggregate_reports → identify_trends → generate_summary
- Use case: Financial reporting, business analytics, forecasting
- Extracts 156+ financial metrics and KPIs

### 9. Extract Operational Metrics ⭐ NEW
Extracts and analyzes operational metrics and performance indicators.
- Steps: collect_metrics → normalize_data → analyze_performance → identify_bottlenecks → build_dashboard
- Use case: Operational monitoring, performance tracking, efficiency optimization
- Monitors 12+ systems with 234+ metrics

### 10. Extract Customer Insights ⭐ NEW
Extracts and synthesizes customer data for business intelligence.
- Steps: gather_customer_data → segment_analysis → identify_patterns → generate_insights → build_recommendations
- Use case: Customer intelligence, retention strategy, product roadmap
- Analyzes 1250+ customers across 6 data sources

### 11. Extract Team Productivity ⭐ NEW
Extracts and analyzes team productivity and engagement metrics.
- Steps: collect_productivity_data → measure_engagement → identify_challenges → benchmark_performance → generate_report
- Use case: Team health assessment, resource planning, engagement tracking
- Tracks 42+ team members with 89 productivity metrics

## API Endpoints

### Run a Workflow

```bash
curl -X POST http://localhost:8000/workflows/{workflow_name} \
  -H "Content-Type: application/json" \
  -d '{
    "owner": "team_name",
    "context": {
      "key": "value"
    }
  }'
```

### Get Workflow Status

```bash
curl http://localhost:8000/workflows/{workflow_id}/status
```

### Backlog Endpoints

```bash
# Get backlog summary
curl http://localhost:8000/backlog

# Get backlog items
curl http://localhost:8000/backlog/items?year_start=2021&year_end=2024&status=pending

# Get detailed backlog analysis
curl http://localhost:8000/backlog/analysis
```

## Example Workflows

### Pull Request Analysis

```bash
curl -X POST http://localhost:8000/workflows/extract_pull_request \
  -H "Content-Type: application/json" \
  -d '{
    "owner": "engineering_lead",
    "context": {
      "repositories": ["ethireal-ai", "platform-api"],
      "pr_count": 42,
      "files_changed": 156
    }
  }'
```

### IPO Readiness Assessment

```bash
curl -X POST http://localhost:8000/workflows/ipo_process \
  -H "Content-Type: application/json" \
  -d '{
    "owner": "cfo",
    "context": {
      "current_status": "pre_planning",
      "target_timeline": "9_months"
    }
  }'
```

### Historical Backlog Review

```bash
curl -X POST http://localhost:8000/workflows/backlog_historical_review \
  -H "Content-Type: application/json" \
  -d '{
    "owner": "product_lead",
    "context": {
      "review_depth": "comprehensive",
      "include_analysis": true
    }
  }'
```

### Financial Data Extraction

```bash
curl -X POST http://localhost:8000/workflows/extract_financial_data \
  -H "Content-Type: application/json" \
  -d '{
    "owner": "finance_team",
    "context": {
      "periods": ["Q1_2024", "Q2_2024", "Q3_2024"],
      "include_forecasting": true
    }
  }'
```

## Backlog Data (2021-Present)

The system includes historical backlog data spanning:
- **2021**: 50+ items (archived, completed, pending)
- **2022**: 52+ items (mixed status)
- **2023**: 52+ items (ongoing work)
- **2024**: 53+ items (current initiatives)

Total: 200+ backlog items with full categorization by:
- Status: completed, pending, running, archived, in_review
- Priority: high, medium, low
- Business Impact: critical, high, medium
- Category: infrastructure, feature, optimization, security, debt

## Running Workflows

Each workflow execution returns:
- `workflow_id`: Unique identifier for tracking
- `status`: Current execution status (queued, running, completed, failed)
- `summary`: Detailed results with step-by-step output and recommendations
