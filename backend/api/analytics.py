from fastapi import APIRouter, Depends

from utils.roles import require_viewer

from services.analytics_service import (
    get_dashboard_metrics,
    employees_by_department,
    salary_distribution,
    hiring_trend,
    get_dashboard_insights,
    get_system_summary,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


# ---------------------------------------------------------
# Dashboard Overview
# Roles:
# Admin
# Manager
# Analyst
# Viewer
# ---------------------------------------------------------
@router.get("/dashboard")
def dashboard(
    current_user=Depends(require_viewer),
):
    return {
        "status": "success",
        "metrics": get_dashboard_metrics(),
        "insights": get_dashboard_insights(),
        "system": get_system_summary(),
    }


# ---------------------------------------------------------
# Employees by Department
# Roles:
# Admin
# Manager
# Analyst
# Viewer (Read Only)
# ---------------------------------------------------------
@router.get("/departments")
def departments(
    current_user=Depends(require_viewer),
):
    return {
        "departments": employees_by_department()
    }


# ---------------------------------------------------------
# Salary Distribution
# Roles:
# Admin
# Manager
# Analyst
# Viewer (Read Only)
# ---------------------------------------------------------
@router.get("/salary")
def salary(
    current_user=Depends(require_viewer),
):
    return {
        "salary": salary_distribution()
    }


# ---------------------------------------------------------
# Hiring Trend
# Roles:
# Admin
# Manager
# Analyst
# Viewer (Read Only)
# ---------------------------------------------------------
@router.get("/hiring")
def hiring(
    current_user=Depends(require_viewer),
):
    return {
        "hiring": hiring_trend()
    }


# ---------------------------------------------------------
# Dashboard Insights
# Roles:
# Admin
# Manager
# Analyst
# Viewer (Read Only)
# ---------------------------------------------------------
@router.get("/insights")
def insights(
    current_user=Depends(require_viewer),
):
    return get_dashboard_insights()