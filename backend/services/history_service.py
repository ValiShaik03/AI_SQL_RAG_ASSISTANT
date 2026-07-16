from services.db_service import get_connection


# -------------------------------------------------
# Save Query History
# -------------------------------------------------

def save_query_history(
    user_id: int,
    question: str,
    generated_sql: str,
    ai_answer: str,
    execution_time_ms: float
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO query_history
            (
                user_id,
                question,
                generated_sql,
                ai_answer,
                execution_time_ms
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s
            )
            """,
            (
                user_id,
                question,
                generated_sql,
                ai_answer,
                execution_time_ms
            )
        )

        conn.commit()

    finally:

        cursor.close()
        conn.close()


# -------------------------------------------------
# Get User History
# -------------------------------------------------

def get_user_history(user_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT
                history_id,
                question,
                generated_sql,
                ai_answer,
                execution_time_ms,
                created_at
            FROM query_history
            WHERE user_id=%s
            ORDER BY created_at DESC
            """,
            (user_id,)
        )

        return cursor.fetchall()

    finally:

        cursor.close()
        conn.close()


# -------------------------------------------------
# Delete History
# -------------------------------------------------

def delete_history(
    history_id: int,
    user_id: int
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            DELETE
            FROM query_history
            WHERE history_id=%s
            AND user_id=%s
            """,
            (
                history_id,
                user_id
            )
        )

        conn.commit()

        return {
            "status": "success",
            "message": "History deleted successfully."
        }

    finally:

        cursor.close()
        conn.close()