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

    text = response.choices[0].message.content.strip()

    # Remove markdown
    text = text.replace("```sql", "")
    text = text.replace("```", "").strip()

    # -----------------------------
    # Extract ONLY first SQL query
    # -----------------------------
    match = re.search(
        r"(?is)\b(SELECT|WITH)\b[\s\S]*?;",
        text
    )

    if not match:
        raise ValueError("LLM did not generate a valid SQL query.")

    sql = match.group(0).strip()

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