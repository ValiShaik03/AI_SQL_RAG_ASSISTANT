from services.db_service import get_connection


def log_activity(
    user_id: int,
    action: str,
    description: str
):
    """
    Store a user activity in the audit_logs table.
    """

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO audit_logs
            (
                user_id,
                action,
                description
            )
            VALUES
            (
                %s,
                %s,
                %s
            )
            """,
            (
                user_id,
                action,
                description
            )
        )

        conn.commit()

    finally:

        cursor.close()
        conn.close()

def get_audit_logs():

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            SELECT
                log_id,
                user_id,
                action,
                description,
                created_at
            FROM audit_logs
            ORDER BY created_at DESC
            """
        )

        logs = cursor.fetchall()

        return logs

    finally:

        cursor.close()
        conn.close()