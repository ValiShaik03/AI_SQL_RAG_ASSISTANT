from services.db_service import get_connection
from prompts.sql_prompt import build_sql_prompt
from services.schema_service import get_database_schema

def execute_query(query):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = []

    if rows:
        columns = list(rows[0].keys())

    cursor.close()
    conn.close()

    return columns, rows