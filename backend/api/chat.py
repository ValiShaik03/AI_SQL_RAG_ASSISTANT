import time
import traceback
from fastapi import APIRouter
from pydantic import BaseModel

from prompts.sql_prompt import build_sql_prompt
from services.schema_service import get_database_schema
from prompts.answer_prompt import ANSWER_PROMPT
from fastapi import Depends
from utils.roles import require_role
from services.history_service import save_query_history
from services.llm_service import (
    generate_sql,
    generate_answer
)

from services.sql_service import execute_query

from utils.question_validator import validate_question
from utils.sql_validator import validate_sql


router = APIRouter(
    prefix="/api",
    tags=["AI SQL Assistant"]
)


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(
    request: ChatRequest,
    current_user=Depends(require_role(["Admin","User"]))
):

    try:

        start_time = time.perf_counter()

        # ---------------------------------
        # Validate User Question
        # ---------------------------------
        
        is_valid_question, message = validate_question(request.question)
        if not is_valid_question:
            return {
        "status": "failed",
        "question": request.question,
        "error": message
    }

        # ---------------------------------
        # Generate SQL
        # ---------------------------------

        schema = get_database_schema()

        prompt = build_sql_prompt(
            schema=schema,
            question=request.question
        )

        generated_sql = generate_sql(prompt)
        
        # ---------------------------------
        # Validate SQL
        # ---------------------------------

        is_valid_sql, message = validate_sql(generated_sql)
        
        if not is_valid_sql:
            return {
                "status": "failed",
                "question": request.question,
                "generated_sql": generated_sql,
                "error": message
            }

        # ---------------------------------
        # Execute SQL
        # ---------------------------------

        columns, data = execute_query(generated_sql)

        # ---------------------------------
        # Generate AI Answer
        # ---------------------------------

        answer = generate_answer(
            request.question,
            generated_sql,
            data,
            ANSWER_PROMPT
        )

        # ---------------------------------
        # Execution Time
        # ---------------------------------

        execution_time = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        answer = generate_answer(
            request.question,
            generated_sql,
            data,
            ANSWER_PROMPT
        )

        execution_time = round(
            (time.perf_counter() - start_time) * 1000,
            2
        )

        # ---------------------------------
        # Save Query History
        # ---------------------------------

        save_query_history(
            user_id=current_user["user_id"],
            question=request.question,
            generated_sql=generated_sql,
            ai_answer=answer,
            execution_time_ms=execution_time
        )

        # ---------------------------------
        # Response
        # ---------------------------------

        return {
            "status": "success",
            "question": request.question,
            "generated_sql": generated_sql,
            "answer": answer,
            "columns": columns,
            "rows_returned": len(data),
            "execution_time_ms": execution_time,
            "data": data
        }
    except Exception as e:

        traceback.print_exc()

        return {
                "status": "error",
                "question": request.question,
                "generated_sql": generated_sql if "generated_sql" in locals() else "",
                "error": str(e)
            }