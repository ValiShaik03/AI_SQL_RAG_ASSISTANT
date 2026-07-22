from fastapi import APIRouter, Depends, HTTPException, Query

from utils.roles import require_analyst

from services.database_service import (
    get_tables,
    get_schema,
    get_preview,
    get_database_stats,
    get_table_info,
    get_schema_summary,
    get_relationships,
)

router = APIRouter(
    prefix="/database",
    tags=["Database Explorer"],
)


# ---------------------------------------------------------
# Database Statistics
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/stats")
def database_stats(
    current_user=Depends(require_viewer),
):
    return get_database_stats()


# ---------------------------------------------------------
# List Database Tables
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/tables")
def tables(
    current_user=Depends(require_analyst),
):
    return {
        "tables": get_tables()
    }


# ---------------------------------------------------------
# Table Information
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/info/{table_name}")
def table_info(
    table_name: str,
    current_user=Depends(require_analyst),
):
    try:
        return get_table_info(table_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


# ---------------------------------------------------------
# Table Schema
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/schema/{table_name}")
def schema(
    table_name: str,
    current_user=Depends(require_analyst),
):
    try:
        return {
            "schema": get_schema(table_name)
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


# ---------------------------------------------------------
# Schema Summary
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/schema-summary/{table_name}")
def schema_summary(
    table_name: str,
    current_user=Depends(require_analyst),
):
    try:
        return get_schema_summary(table_name)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


# ---------------------------------------------------------
# Preview Table Data
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/preview/{table_name}")
def preview(
    table_name: str,
    page: int = Query(
        default=1,
        ge=1,
    ),
    page_size: int = Query(
        default=10,
        ge=1,
        le=100,
    ),
    current_user=Depends(require_analyst),
):
    try:
        return get_preview(
            table_name,
            page,
            page_size,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


# ---------------------------------------------------------
# Database Relationships
# Roles:
# Admin
# Manager
# Analyst
# ---------------------------------------------------------
@router.get("/relationships")
def relationships(
    current_user=Depends(require_analyst),
):
    return {
        "relationships": get_relationships()
    }