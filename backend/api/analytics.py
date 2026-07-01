from fastapi import APIRouter

from services.analytics_service import (
    get_dashboard_metrics,
    employees_by_department,
    salary_distribution,
    hiring_trend,
    get_dashboard_insights
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/dashboard")
def dashboard():

    return get_dashboard_metrics()


@router.get("/departments")
def departments():

    return {
        "departments": employees_by_department()
    }


@router.get("/salary")
def salary():

    return {
        "salary": salary_distribution()
    }


@router.get("/hiring")
def hiring():

    return {
        "hiring": hiring_trend()
    }
    
@router.get("/insights")
def insights():

    return get_dashboard_insights()