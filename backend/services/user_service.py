from services.db_service import get_connection
from utils.password import hash_password

# ----------------------------------------
# Allowed Roles
# ----------------------------------------

ALLOWED_ROLES = [
    "Admin",
    "Manager",
    "Analyst",
    "Viewer"
]


# ----------------------------------------
# Get All Users
# ----------------------------------------

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


# ----------------------------------------
# Create User
# ----------------------------------------

def create_user(
    full_name: str,
    email: str,
    password: str,
    role: str
):

    # -----------------------------
    # Validate Role
    # -----------------------------

    if role not in ALLOWED_ROLES:
        return {
            "status": "failed",
            "message": f"Invalid role. Allowed roles: {', '.join(ALLOWED_ROLES)}"
        }

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # -----------------------------
        # Check Duplicate Email
        # -----------------------------

        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE email = %s
            """,
            (email,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            return {
                "status": "failed",
                "message": "Email already exists."
            }

        # -----------------------------
        # Hash Password
        # -----------------------------

        password_hash = hash_password(password)

        # -----------------------------
        # Insert User
        # -----------------------------

        cursor.execute(
            """
            INSERT INTO users
            (
                full_name,
                email,
                password_hash,
                role,
                is_active
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                TRUE
            )
            """,
            (
                full_name,
                email,
                password_hash,
                role
            )
        )

        conn.commit()

        return {
            "status": "success",
            "message": "User created successfully."
        }

    finally:

        cursor.close()
        conn.close()

def update_user(
    user_id: int,
    full_name: str,
    email: str,
    role: str
):

    if role not in ALLOWED_ROLES:
        return {
            "status": "failed",
            "message": f"Invalid role. Allowed roles: {', '.join(ALLOWED_ROLES)}"
        }

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # Check if user exists
        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE user_id=%s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        if not user:
            return {
                "status": "failed",
                "message": "User not found."
            }

        # Check duplicate email
        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE email=%s
            AND user_id<>%s
            """,
            (
                email,
                user_id
            )
        )

        duplicate = cursor.fetchone()

        if duplicate:
            return {
                "status": "failed",
                "message": "Email already exists."
            }

        cursor.execute(
            """
            UPDATE users
            SET
                full_name=%s,
                email=%s,
                role=%s
            WHERE user_id=%s
            """,
            (
                full_name,
                email,
                role,
                user_id
            )
        )

        conn.commit()

        return {
            "status": "success",
            "message": "User updated successfully."
        }

    finally:

        cursor.close()
        conn.close()

def delete_user(
    user_id: int,
    current_user_id: int
):

    conn = get_connection()
    cursor = conn.cursor()

    try:

        # ----------------------------------
        # Check if user exists
        # ----------------------------------

        cursor.execute(
            """
            SELECT user_id
            FROM users
            WHERE user_id=%s
            """,
            (user_id,)
        )

        user = cursor.fetchone()

        if not user:
            return {
                "status": "failed",
                "message": "User not found."
            }

        # ----------------------------------
        # Prevent self deletion
        # ----------------------------------

        if user_id == current_user_id:

            return {
                "status": "failed",
                "message": "You cannot delete your own account."
            }

        # ----------------------------------
        # Delete user
        # ----------------------------------

        cursor.execute(
            """
            DELETE FROM users
            WHERE user_id=%s
            """,
            (user_id,)
        )

        conn.commit()

        return {
            "status": "success",
            "message": "User deleted successfully."
        }

    finally:

        cursor.close()
        conn.close()