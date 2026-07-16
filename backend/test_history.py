from services.history_service import save_query_history

save_query_history(
    user_id=1,
    question="Show all employees",
    generated_sql="SELECT * FROM employees;",
    ai_answer="There are 40 employees.",
    execution_time_ms=231.55
)

print("History saved successfully.")