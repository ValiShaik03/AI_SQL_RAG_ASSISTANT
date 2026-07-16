from typing import Optional

from fastapi import APIRouter, Depends, Query

from services.audit_service import (
    get_audit_logs,
    get_audit_logs_count
)
from utils.roles import require_admin
from fastapi import Query

router = APIRouter(
    prefix="/api/admin",
    tags=["Audit Logs"]
)


@router.get("/audit-logs")
def audit_logs(

    action: str = Query(None),

    user_id: int = Query(None),

    page: int = Query(1, ge=1),

    page_size: int = Query(10, ge=1, le=100),

    current_user=Depends(require_admin)

):

    logs = get_audit_logs(
        action=action,
        user_id=user_id,
        page=page,
        page_size=page_size
    )

    total = get_audit_logs_count(
        action=action,
        user_id=user_id
    )

    return {
        "status": "success",
        "page": page,
        "page_size": page_size,
        "total_records": total,
        "total_pages": (total + page_size - 1) // page_size,
        "returned_records": len(logs),
        "logs": logs
    }