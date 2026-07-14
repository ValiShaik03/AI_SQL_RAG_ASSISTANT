from fastapi import APIRouter
from pydantic import BaseModel

from services.auth_service import authenticate_user

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


class LoginRequest(BaseModel):
    email: str
    password: str


@router.post("/login")
def login(request: LoginRequest):

    result = authenticate_user(
        request.email,
        request.password
    )

    if result is None:
        return {
            "status": "failed",
            "message": "Invalid email or password."
        }

    return {
        "status": "success",
        **result
    }