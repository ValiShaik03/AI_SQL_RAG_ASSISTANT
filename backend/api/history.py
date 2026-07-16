from fastapi import APIRouter, Depends

from utils.auth import get_current_user
from services.history_service import (
    get_user_history,
    delete_history
)

router = APIRouter(
    prefix="/api/history",
    tags=["Query History"]
)


@router.get("")
def history(
    current_user=Depends(get_current_user)
):

    history = get_user_history(
        current_user["user_id"]
    )

    return {
        "status": "success",
        "count": len(history),
        "history": history
    }


@router.delete("/{history_id}")
def delete(
    history_id: int,
    current_user=Depends(get_current_user)
):

    return delete_history(
        history_id,
        current_user["user_id"]
    )