FORBIDDEN_INTENTS = [
    "delete",
    "drop",
    "truncate",
    "remove",
    "erase",
    "update",
    "insert",
    "create",
    "alter",
    "modify"
]

def validate_question(question: str):
    question = question.lower()

    for word in FORBIDDEN_INTENTS:
        if word in question:
            return False, f"Operation '{word}' is not allowed."

    return True, "OK"