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

    query = query.strip().lower()

    query = query.strip()
    if not (
        query.lower().startswith("select")
        or
        query.lower().startswith("with")):
        return False, "Only SELECT queries are allowed."
    # Only one SQL statement
    if ";" in query[:-1]:
        return False, "Multiple SQL statements are not allowed."
    # Block dangerous keywords
    for keyword in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{keyword}\b", query):
            return False, f"Forbidden SQL keyword detected: {keyword}"

    return True, "Valid SQL"