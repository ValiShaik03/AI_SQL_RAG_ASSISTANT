from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from utils.auth import get_current_user
from pydantic import BaseModel
from typing import List, Dict, Any
from services.export_service import (
    export_to_csv,
    export_to_excel
)

router = APIRouter(
    prefix="/api/export",
    tags=["Export"]
)

class ExportRequest(BaseModel):
    columns: List[str]
    data: List[Dict[str, Any]]

@router.post("/csv")
def export_csv(
    payload: ExportRequest,
    current_user=Depends(get_current_user)
):

    columns = payload.columns
    data = payload.data

    csv_file = export_to_csv(
        columns,
        data
    )

    return StreamingResponse(
        csv_file,
        media_type="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=query_results.csv"
        }
    )

@router.post("/excel")
def export_excel(
    payload: ExportRequest,
    current_user=Depends(get_current_user)
):

    excel_file = export_to_excel(
        payload.columns,
        payload.data
    )

    return StreamingResponse(
        excel_file,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition":
            "attachment; filename=query_results.xlsx"
        }
    )