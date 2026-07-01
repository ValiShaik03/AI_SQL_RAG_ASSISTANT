import requests

BASE_URL = "http://127.0.0.1:8000"


# -------------------------------------------------
# AI SQL Assistant
# -------------------------------------------------

def ask_ai(question: str):

    try:

        response = requests.post(
            f"{BASE_URL}/api/chat",
            json={"question": question},
            timeout=60
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:

        return {
            "status": "failed",
            "error": str(e)
        }


# -------------------------------------------------
# Database Statistics
# -------------------------------------------------

def get_stats():

    response = requests.get(
        f"{BASE_URL}/database/stats"
    )

    response.raise_for_status()

    return response.json()


# -------------------------------------------------
# Tables
# -------------------------------------------------

def get_tables():

    response = requests.get(
        f"{BASE_URL}/database/tables"
    )

    response.raise_for_status()

    return response.json()["tables"]


# -------------------------------------------------
# Table Information
# -------------------------------------------------

def get_table_info(table_name):

    response = requests.get(
        f"{BASE_URL}/database/info/{table_name}"
    )

    response.raise_for_status()

    return response.json()


# -------------------------------------------------
# Schema
# -------------------------------------------------

def get_schema(table_name):

    response = requests.get(
        f"{BASE_URL}/database/schema/{table_name}"
    )

    response.raise_for_status()

    return response.json()["schema"]


# -------------------------------------------------
# Preview
# -------------------------------------------------

def get_preview(
    table_name,
    page=1,
    page_size=10
):

    response = requests.get(

        f"{BASE_URL}/database/preview/{table_name}",

        params={
            "page": page,
            "page_size": page_size
        }

    )

    response.raise_for_status()

    return response.json()


# -------------------------------------------------
# Schema Summary
# -------------------------------------------------

def get_schema_summary(table_name):

    response = requests.get(
        f"{BASE_URL}/database/schema-summary/{table_name}"
    )

    response.raise_for_status()

    return response.json()


# -------------------------------------------------
# Relationships
# -------------------------------------------------

def get_relationships():

    response = requests.get(
        f"{BASE_URL}/database/relationships"
    )

    response.raise_for_status()

    return response.json()["relationships"]