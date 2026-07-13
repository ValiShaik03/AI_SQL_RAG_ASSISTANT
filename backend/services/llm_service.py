import os
import re
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL_NAME = "llama-3.3-70b-versatile"


def generate_sql(prompt):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    sql = response.choices[0].message.content.strip()

    # Remove markdown if present
    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "").strip()

    # -----------------------------
    # Extract ONLY SQL
    # -----------------------------
    match = re.search(
    r"(SELECT\b[\s\S]*|WITH\b[\s\S]*)",
    sql,
    re.IGNORECASE)
    if match:
        sql = match.group(1).strip()
        
    if not sql.endswith(";"):
        sql += ";"

    if match:
        sql = match.group(1).strip()

    return sql


def generate_answer(question, sql, data, prompt):

    final_prompt = f"""
{prompt}

User Question:
{question}

Generated SQL:
{sql}

SQL Result:
{data}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": final_prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content.strip()