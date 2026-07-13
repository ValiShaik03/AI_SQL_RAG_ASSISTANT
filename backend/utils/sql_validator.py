import re

FORBIDDEN_KEYWORDS = [
    "insert",
    "update",
    "delete",
    "drop",
    "alter",
    "truncate",
    "create",
    "replace",
    "grant",
    "revoke",
    "commit",
    "rollback",
    "merge",
    "call",
    "execute",
    "exec"
]


def validate_sql(query: str):

    # Normalize SQL
    query = query.strip().lower()

    # Only SELECT / WITH queries are allowed
    if not (query.startswith("select") or query.startswith("with")):
        return False, "Only SELECT queries are allowed."

    # Allow only one SQL statement
    # (ignore the final semicolon)
    if ";" in query[:-1]:
        return False, "Multiple SQL statements are not allowed."

    # Block dangerous SQL keywords
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", query):
            return False, f"Operation '{keyword}' is not allowed."

    return True, "Valid SQL"