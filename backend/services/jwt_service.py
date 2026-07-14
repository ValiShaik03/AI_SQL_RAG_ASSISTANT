import os
from datetime import datetime, timedelta, timezone

from dotenv import load_dotenv
from jose import JWTError, jwt

# ---------------------------------------------------
# Load Environment Variables
# ---------------------------------------------------

load_dotenv()


SECRET_KEY = os.getenv("JWT_SECRET_KEY")

ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60")
)

# ---------------------------------------------------
# Create Access Token
# ---------------------------------------------------

def create_access_token(data: dict):

    print("Creating JWT...")
    print("SECRET_KEY:", repr(SECRET_KEY), type(SECRET_KEY))
    print("ALGORITHM:", repr(ALGORITHM), type(ALGORITHM))
    print("Payload:", data)

    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode["exp"] = expire

    try:
        token = jwt.encode(
            to_encode,
            SECRET_KEY,
            algorithm=ALGORITHM
        )

        print("JWT created successfully")
        return token

    except Exception:
        import traceback
        traceback.print_exc()
        raise


# ---------------------------------------------------
# Verify Token
# ---------------------------------------------------

def verify_token(token: str):

    """
    Verify JWT Token
    """

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        return None


# ---------------------------------------------------
# Get User ID
# ---------------------------------------------------

def get_user_id(token: str):

    """
    Extract User ID from JWT
    """

    payload = verify_token(token)

    if payload is None:
        return None

    return payload.get("user_id")


# ---------------------------------------------------
# Get User Role
# ---------------------------------------------------

def get_user_role(token: str):

    """
    Extract User Role from JWT
    """

    payload = verify_token(token)

    if payload is None:
        return None

    return payload.get("role")


# ---------------------------------------------------
# Check Token Validity
# ---------------------------------------------------

def is_token_valid(token: str):

    """
    Returns True if token is valid.
    """

    return verify_token(token) is not None