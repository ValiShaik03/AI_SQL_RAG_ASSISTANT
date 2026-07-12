from services.db_service import get_connection


def get_database_schema():

    conn = get_connection()

    cursor = conn.cursor()

    schema = ""

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    for table in tables:

        table_name = list(table.values())[0]

        schema += f"\nTable: {table_name}\n"

        cursor.execute(f"SHOW COLUMNS FROM {table_name}")

        columns = cursor.fetchall()

        for column in columns:

            schema += f"- {column['Field']}\n"

    cursor.close()
    conn.close()

    return schema