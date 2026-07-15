from fastapi import APIRouter, Depends
from pydantic import BaseModel
from services.user_service import update_user
from utils.roles import require_admin
from services.user_service import update_user_status
from services.user_service import (
    get_all_users,
    create_user
)
from services.user_service import (
    get_all_users,
    create_user,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/api/admin",
    tags=["Admin"]
)


class CreateUserRequest(BaseModel):
    full_name: str
    email: str
    password: str
    role: str

class UpdateUserRequest(BaseModel):
    full_name: str
    email: str
    role: str

class UpdateStatusRequest(BaseModel):
    is_active: bool

@router.get("/users")
def users(
    current_user=Depends(require_admin)
):

    return {
        "status": "success",
        "users": get_all_users()
    }


@router.post("/users")
def add_user(
    request: CreateUserRequest,
    current_user=Depends(require_admin)
):

    return create_user(
        request.full_name,
        request.email,
        request.password,
        request.role
    )

@router.put("/users/{user_id}")
def edit_user(
    user_id: int,
    request: UpdateUserRequest,
    current_user=Depends(require_admin)
):

    return update_user(
        user_id,
        request.full_name,
        request.email,
        request.role
    )

@router.delete("/users/{user_id}")
def remove_user(
    user_id: int,
    current_user=Depends(require_admin)
):

    return delete_user(
        user_id,
        current_user["user_id"]
    )

@router.patch("/users/{user_id}/status")
def change_user_status(
    user_id: int,
    request: UpdateStatusRequest,
    current_user=Depends(require_admin)
):

    return update_user_status(
        user_id=user_id,
        is_active=request.is_active,
        current_user_id=current_user["user_id"]
    )