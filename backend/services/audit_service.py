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

def get_audit_logs(
    action=None,
    user_id=None,
    page=1,
    page_size=10
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        query = """
                SELECT
                    a.log_id,
                    a.user_id,
                    u.full_name,
                    u.email,
                    a.action,
                    a.description,
                    a.created_at
                FROM audit_logs a
                LEFT JOIN users u
                    ON a.user_id = u.user_id
                WHERE 1=1
            """

        params = []

        if action:
            query += " AND a.action=%s"
            params.append(action)

        if user_id:
            query += " AND a.user_id=%s"
            params.append(user_id)

        query += " ORDER BY a.created_at DESC"

        offset = (page - 1) * page_size

        query += " LIMIT %s OFFSET %s"

        params.extend([page_size, offset])

        cursor.execute(query, tuple(params))

        logs = cursor.fetchall()

        return logs

    finally:

        cursor.close()
        conn.close()

def get_audit_logs_count(
    action=None,
    user_id=None
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        query = """
            SELECT COUNT(*) AS total
            FROM audit_logs
            WHERE 1=1
        """

        params = []

        if action:
            query += " AND action=%s"
            params.append(action)

        if user_id:
            query += " AND user_id=%s"
            params.append(user_id)

        cursor.execute(query, tuple(params))

        result = cursor.fetchone()

        return result["total"]

    finally:

        cursor.close()
        conn.close()