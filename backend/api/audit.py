from fastapi import APIRouter, Depends

from services.audit_service import get_audit_logs
from utils.roles import require_admin

router = APIRouter(
    prefix="/api/admin",
    tags=["Audit Logs"]
)


@router.get("/audit-logs")
def audit_logs(
    current_user=Depends(require_admin)
):

    return {
        "status": "success",
        "count": len(get_audit_logs()),
        "logs": get_audit_logs()
    }