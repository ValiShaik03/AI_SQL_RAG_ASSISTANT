import math

from services.sql_service import get_connection


# -------------------------------------------------
# Internal Helper
# -------------------------------------------------

def _validate_table(table_name: str):
    """
    Ensure the table exists before using it in SQL.
    """
    tables = get_tables()

    if table_name not in tables:
        raise ValueError(f"Invalid table name: {table_name}")


# -------------------------------------------------
# Get All Tables
# -------------------------------------------------

def get_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [list(row.values())[0] for row in rows]


# -------------------------------------------------
# Get Schema
# -------------------------------------------------

def get_schema(table_name):

    _validate_table(table_name)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"DESCRIBE `{table_name}`")

    schema = cursor.fetchall()

    cursor.close()
    conn.close()

    return schema


# -------------------------------------------------
# Row Count
# -------------------------------------------------

def get_row_count(table_name):

    _validate_table(table_name)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT COUNT(*) AS total
        FROM `{table_name}`
        """
    )

    total = cursor.fetchone()["total"]

    cursor.close()
    conn.close()

    return total


# -------------------------------------------------
# Column Count
# -------------------------------------------------

def get_column_count(table_name):

    return len(get_schema(table_name))


# -------------------------------------------------
# Primary Key
# -------------------------------------------------

def get_primary_key(table_name):

    schema = get_schema(table_name)

    for column in schema:

        if column["Key"] == "PRI":

            return column["Field"]

    return None


# -------------------------------------------------
# Table Information
# -------------------------------------------------

def get_table_info(table_name):

    return {

        "table": table_name,

        "rows": get_row_count(table_name),

        "columns": get_column_count(table_name),

        "primary_key": get_primary_key(table_name)

    }


# -------------------------------------------------
# Preview Table (Pagination)
# -------------------------------------------------

def get_preview(
    table_name,
    page=1,
    page_size=10
):

    _validate_table(table_name)

    total_rows = get_row_count(table_name)

    total_pages = max(1, math.ceil(total_rows / page_size))

    if page < 1:
        page = 1

    if page > total_pages:
        page = total_pages

    offset = (page - 1) * page_size

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT *
        FROM `{table_name}`
        LIMIT %s OFFSET %s
        """,
        (page_size, offset)
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {

        "rows": rows,

        "page": page,

        "page_size": page_size,

        "total_rows": total_rows,

        "total_pages": total_pages

    }


# -------------------------------------------------
# Database Statistics
# -------------------------------------------------

def get_database_stats():

    tables = get_tables()

    total_rows = 0
    total_columns = 0

    table_stats = []

    for table in tables:

        rows = get_row_count(table)

        columns = get_column_count(table)

        total_rows += rows

        total_columns += columns

        table_stats.append({

            "table": table,

            "rows": rows,

            "columns": columns

        })

    return {

        "database": "MySQL",

        "total_tables": len(tables),

        "total_rows": total_rows,

        "total_columns": total_columns,

        "tables": table_stats

    }


# -------------------------------------------------
# Schema Summary
# -------------------------------------------------

def get_schema_summary(table_name):

    schema = get_schema(table_name)

    numeric = 0
    text = 0
    dates = 0

    for col in schema:

        dtype = col["Type"].lower()

        if any(x in dtype for x in [
            "int",
            "decimal",
            "float",
            "double",
            "bigint",
            "smallint"
        ]):

            numeric += 1

        elif any(x in dtype for x in [
            "date",
            "datetime",
            "timestamp",
            "time"
        ]):

            dates += 1

        else:

            text += 1

    return {

        "columns": len(schema),

        "primary_key": get_primary_key(table_name),

        "numeric_columns": numeric,

        "text_columns": text,

        "date_columns": dates

    }


# -------------------------------------------------
# Relationships
# -------------------------------------------------

def get_relationships():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT

            TABLE_NAME,

            COLUMN_NAME,

            REFERENCED_TABLE_NAME,

            REFERENCED_COLUMN_NAME

        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE

        WHERE

            TABLE_SCHEMA = DATABASE()

            AND REFERENCED_TABLE_NAME IS NOT NULL
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows