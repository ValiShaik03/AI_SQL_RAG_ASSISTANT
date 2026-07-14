from services.db_service import get_connection
from utils.password import hash_password


def get_all_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            user_id,
            full_name,
            email,
            role,
            is_active,
            created_at
        FROM users
        ORDER BY user_id
    """)

    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return users


def create_user(full_name, email, password, role):

    conn = get_connection()
    cursor = conn.cursor()

    password_hash = hash_password(password)

    cursor.execute("""
        INSERT INTO users
        (
            full_name,
            email,
            password_hash,
            role,
            is_active
        )
        VALUES
        (%s,%s,%s,%s,TRUE)
    """,
    (
        full_name,
        email,
        password_hash,
        role
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "User created successfully."
    }