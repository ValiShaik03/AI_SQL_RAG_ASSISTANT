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

# Questions outside the employee database domain
NON_DATABASE_TOPICS = [
    "prime minister",
    "president",
    "capital",
    "country",
    "india",
    "china",
    "america",
    "usa",
    "cricket",
    "football",
    "weather",
    "temperature",
    "movie",
    "actor",
    "actress",
    "song",
    "youtube",
    "instagram",
    "facebook",
    "ipl",
    "bitcoin",
    "crypto",
    "stock market",
    "news",
    "politics"
    # "science",
    # "physics",
    # "chemistry",
    # "mathematics"
]


def validate_question(question: str):
    """
    Validate the user's natural language question.
    """

    # -----------------------------
    # Empty Question
    # -----------------------------

    if question is None:
        return False, "Question cannot be empty."

    question = question.strip()

    if len(question) == 0:
        return False, "Question cannot be empty."

    if len(question) < 3:
        return False, "Please enter a meaningful question."

    question_lower = question.lower()

    # -----------------------------
    # Forbidden SQL Operations
    # -----------------------------

    for word in FORBIDDEN_INTENTS:

        if word in question_lower:

            return (
                False,
                f"Operation '{word}' is not allowed."
            )

    # -----------------------------
    # Non-Database Questions
    # -----------------------------

    for topic in NON_DATABASE_TOPICS:
        if topic in question_lower:
            return (
            False,
            "This assistant only answers questions related to the connected employee database."
            )

    return True, "OK"