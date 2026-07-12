import pymysql
from utils.config import DB_CONFIG


def get_connection():
    return pymysql.connect(
        cursorclass=pymysql.cursors.DictCursor,
        **DB_CONFIG
    )