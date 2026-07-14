from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from services.sql_service import get_connection

from api.chat import router as chat_router
from api.database import router as database_router
from api.analytics import router as analytics_router
from api.auth import router as auth_router
from fastapi import Depends
from utils.roles import require_role

app = FastAPI(
    title="AI SQL RAG Assistant",
    version="1.0.0"
)

# -----------------------------------------
# CORS Configuration
# -----------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Restrict to your frontend domain later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------
# Register Routers
# -----------------------------------------

app.include_router(chat_router)
app.include_router(database_router)
app.include_router(analytics_router)
app.include_router(auth_router)

# -----------------------------------------
# Home
# -----------------------------------------

@app.get("/")
def home():

    return {
        "status": "success",
        "message": "AI SQL RAG Assistant Backend Running Successfully",
        "version": "1.0.0"
    }


# -----------------------------------------
# Health Check
# -----------------------------------------

@app.get("/health")
def health():

    try:

        conn = get_connection()

        cursor = conn.cursor()

        cursor.execute("SELECT 1")

        cursor.fetchone()

        cursor.close()
        conn.close()

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }


# -----------------------------------------
# Employees
# -----------------------------------------

@app.get("/employees")
def employees(current_user=Depends(require_role(["Admin","User"]))):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {
        "employees": rows
    }