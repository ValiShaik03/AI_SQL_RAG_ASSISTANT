from fastapi import APIRouter, Depends, Query

from utils.roles import require_admin

from services.audit_service import (
    get_audit_logs,
    get_audit_logs_count,
)

router = APIRouter(
    prefix="/api/admin",
    tags=["Audit Logs"],
)


# ---------------------------------------------------------
# Audit Logs
# Roles:
# Admin Only
# ---------------------------------------------------------
@router.get("/audit-logs")
def audit_logs(
    action: str | None = Query(default=None),
    user_id: int | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    current_user=Depends(require_admin),
):
    logs = get_audit_logs(
        action=action,
        user_id=user_id,
        page=page,
        page_size=page_size,
    )

    total = get_audit_logs_count(
        action=action,
        user_id=user_id,
    )

    return {
        "status": "success",
        "page": page,
        "page_size": page_size,
        "total_records": total,
        "total_pages": (total + page_size - 1) // page_size,
        "returned_records": len(logs),
        "logs": logs,
    }