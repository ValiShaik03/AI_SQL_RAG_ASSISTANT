from fastapi import APIRouter
from fastapi import Depends
from utils.roles import require_admin
from services.analytics_service import (
    get_dashboard_metrics,
    employees_by_department,
    salary_distribution,
    hiring_trend,
    get_dashboard_insights,
    get_system_summary
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/dashboard")
def dashboard(
    current_user=Depends(require_admin)
):

    return {
        "status": "success",
        "metrics": get_dashboard_metrics(),
        "insights": get_dashboard_insights(),
        "system": get_system_summary()
    }

@router.get("/departments")
def departments(current_user=Depends(require_admin)):

    return {
        "departments": employees_by_department()
    }


@router.get("/salary")
def salary(current_user=Depends(require_admin)):

    return {
        "salary": salary_distribution()
    }


@router.get("/hiring")
def hiring(current_user=Depends(require_admin)):

    return {
        "hiring": hiring_trend()
    }
    
@router.get("/insights")
def insights(current_user=Depends(require_admin)):

    return get_dashboard_insights()