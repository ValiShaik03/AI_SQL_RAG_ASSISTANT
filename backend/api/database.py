from fastapi import APIRouter, HTTPException, Query
from fastapi import APIRouter, HTTPException, Query, Depends
from utils.roles import require_admin
from services.database_service import (
    get_tables,
    get_schema,
    get_preview,
    get_database_stats,
    get_table_info,
    get_schema_summary,
    get_relationships
)

router = APIRouter(
    prefix="/database",
    tags=["Database Explorer"]
)


@router.get("/stats")
def database_stats(current_user=Depends(require_admin)):

    return get_database_stats()


@router.get("/tables")
def tables(current_user=Depends(require_admin)):

    return {

        "tables": get_tables()

    }


@router.get("/info/{table_name}")
def table_info(table_name: str,
current_user=Depends(require_admin)):

    try:

        return get_table_info(table_name)

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/schema/{table_name}")
def schema(table_name: str,
current_user=Depends(require_admin)):

    try:

        return {

            "schema": get_schema(table_name)

        }

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/schema-summary/{table_name}")
def schema_summary(table_name: str,
current_user=Depends(require_admin)):

    try:

        return get_schema_summary(table_name)

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/preview/{table_name}")
def preview(

    table_name: str,

    page: int = Query(
        1,
        ge=1
    ),

    page_size: int = Query(
        10,
        ge=1,
        le=100
    ),

    current_user=Depends(require_admin)

):

    try:

        return get_preview(

            table_name,

            page,

            page_size

        )

    except ValueError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


@router.get("/relationships")
def relationships(current_user=Depends(require_admin)):

    return {

        "relationships": get_relationships()

    }