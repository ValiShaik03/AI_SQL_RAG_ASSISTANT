from fastapi import FastAPI

from services.sql_service import get_connection

from api.chat import router as chat_router
from api.database import router as database_router
from api.analytics import router as analytics_router

app = FastAPI(title="AI SQL RAG Assistant")

app.include_router(chat_router)
app.include_router(database_router)
app.include_router(analytics_router)

@app.get("/")
def home():
    return {
        "message": "AI SQL RAG Assistant Backend Running Successfully"
    }


@app.get("/employees")
def employees():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "employees": rows
    }