from services.db_service import get_connection
from utils.password import verify_password
from services.jwt_service import create_access_token


def authenticate_user(email: str, password: str):
    """
    Authenticate a user using email and password.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            user_id,
            full_name,
            email,
            password_hash,
            role,
            is_active
        FROM users
        WHERE email=%s
        """,
        (email,)
    )

    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return None

    if not user["is_active"]:
        return None

    if not verify_password(password, user["password_hash"]):
        return None

    token = create_access_token(
        {
            "user_id": user["user_id"],
            "email": user["email"],
            "role": user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "user_id": user["user_id"],
            "full_name": user["full_name"],
            "email": user["email"],
            "role": user["role"]
        }
    }