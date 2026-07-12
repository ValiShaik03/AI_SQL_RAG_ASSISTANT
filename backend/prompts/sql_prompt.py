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

- Generate ONLY SQL.
- Return exactly one SQL statement.
- Never generate INSERT, UPDATE, DELETE, DROP, ALTER, CREATE.
- Use JOIN whenever required.
- SQL must be valid MySQL.

Question:

{question}

SQL:
"""