from typing import Any, Dict, List

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from utils.auth import get_current_user

from services.export_service import (
    export_to_csv,
    export_to_excel,
)

router = APIRouter(
    prefix="/api/export",
    tags=["Export"],
)


# ---------------------------------------------------------
# Request Model
# ---------------------------------------------------------
class ExportRequest(BaseModel):
    columns: List[str]
    data: List[Dict[str, Any]]


# ---------------------------------------------------------
# Export Query Result to CSV
# Roles:
# Admin
# Manager
# Analyst
# Viewer
# ---------------------------------------------------------
@router.post("/csv")
def export_csv(
    payload: ExportRequest,
    current_user=Depends(get_current_user),
):
    csv_file = export_to_csv(
        payload.columns,
        payload.data,
    )

    return StreamingResponse(
        csv_file,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=query_results.csv"
        },
    )


# ---------------------------------------------------------
# Export Query Result to Excel
# Roles:
# Admin
# Manager
# Analyst
# Viewer
# ---------------------------------------------------------
@router.post("/excel")
def export_excel(
    payload: ExportRequest,
    current_user=Depends(get_current_user),
):
    excel_file = export_to_excel(
        payload.columns,
        payload.data,
    )

    return StreamingResponse(
        excel_file,
        media_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        ),
        headers={
            "Content-Disposition": "attachment; filename=query_results.xlsx"
        },
    )