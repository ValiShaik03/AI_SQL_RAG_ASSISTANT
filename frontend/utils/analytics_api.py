import requests

BASE_URL = "http://127.0.0.1:8000"


# ---------------------------------------
# Dashboard KPI
# ---------------------------------------

def get_dashboard_metrics():

    response = requests.get(
        f"{BASE_URL}/analytics/dashboard"
    )

    response.raise_for_status()

    return response.json()


# ---------------------------------------
# Department Chart
# ---------------------------------------

def get_department_data():

    response = requests.get(
        f"{BASE_URL}/analytics/departments"
    )

    response.raise_for_status()

    return response.json()["departments"]


# ---------------------------------------
# Salary Distribution
# ---------------------------------------

def get_salary_data():

    response = requests.get(
        f"{BASE_URL}/analytics/salary"
    )

    response.raise_for_status()

    return response.json()["salary"]


# ---------------------------------------
# Hiring Trend
# ---------------------------------------

def get_hiring_data():

    response = requests.get(
        f"{BASE_URL}/analytics/hiring"
    )

    response.raise_for_status()

    return response.json()["hiring"]


# ---------------------------------------
# AI Insights
# ---------------------------------------

def get_dashboard_insights():

    response = requests.get(
        f"{BASE_URL}/analytics/insights"
    )

    response.raise_for_status()

    return response.json()