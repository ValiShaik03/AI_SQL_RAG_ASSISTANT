import pymysql
from utils.config import DB_CONFIG


def get_connection():
    return pymysql.connect(
        cursorclass=pymysql.cursors.DictCursor,
        **DB_CONFIG
    )


def execute_query(query):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    columns = []

    if rows:
        columns = list(rows[0].keys())

    cursor.close()
    conn.close()

    return columns, rows