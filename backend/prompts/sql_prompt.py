RELATIONSHIPS = """
employees.employee_id = attendance.employee_id
employees.employee_id = employee_projects.employee_id
projects.project_id = employee_projects.project_id
employees.employee_id = salary_history.employee_id
employees.employee_id = leave_requests.employee_id
employees.employee_id = performance_reviews.employee_id
employees.employee_id = assets.employee_id
employees.employee_id = training_records.employee_id
employees.department = departments.department_name
"""


def build_sql_prompt(schema: str, question: str):

    return f"""
You are an expert MySQL SQL generator.

Database:
ai_sql_rag

Schema:

{schema}

Relationships:

{RELATIONSHIPS}

Rules:

Generate optimized MySQL queries.

Never use SELECT * unless the user explicitly requests all columns.

Return only the columns required.

Use JOIN whenever information exists across multiple tables.

Use table aliases.

employees e
departments d
attendance a
projects p
employee_projects ep
salary_history sh
leave_requests lr
performance_reviews pr
assets ast
training_records tr

Use DISTINCT whenever duplicate records may occur.

Use GROUP BY whenever aggregation is required.

Use LOWER() for status comparisons.

Examples:

LOWER(status)='completed'

LOWER(status)='approved'

LOWER(status)='in progress'

If a person's name is mentioned, search using employees.first_name and employees.last_name.

Generate optimized MySQL syntax only.

Question:

{question}

SQL:
"""