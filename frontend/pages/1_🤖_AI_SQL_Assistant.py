import streamlit as st

from utils.api_client import ask_ai

from components.sidebar import render_sidebar
from components.header import render_header
from components.answer_card import render_answer
from components.sql_card import render_sql
from components.metric_cards import render_metrics
from components.result_table import render_table
from components.footer import render_footer
from components.example_questions import render_examples
from components.user_message import render_user_question
from components.theme import load_theme

# --------------------------------------------------
# Page
# --------------------------------------------------

st.set_page_config(
    page_title="AI SQL Assistant",
    page_icon="🤖",
    layout="wide"
)

render_sidebar()
load_theme()

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# --------------------------------------------------
# Header (only once)
# --------------------------------------------------

if len(st.session_state.chat_history) == 0:

    render_header()


# --------------------------------------------------
# Display previous conversations
# --------------------------------------------------

for index, chat in enumerate(st.session_state.chat_history):

    response = chat["response"]

    render_user_question(chat["question"])

    render_answer(response["answer"])

    render_sql(response["generated_sql"])

    render_metrics(
        response["rows_returned"],
        response["execution_time_ms"]
    )

    render_table(
        response["data"],
        key=index
    )

    st.divider()


# --------------------------------------------------
# Chat Input
# --------------------------------------------------

question = st.chat_input(
    "💬 Ask anything about your SQL database..."
)


# --------------------------------------------------
# New Question
# --------------------------------------------------

if question:

    with st.spinner("Thinking..."):

        response = ask_ai(question)

    if response["status"] == "success":

        st.session_state.chat_history.append(
            {
                "question": question,
                "response": response
            }
        )

        st.rerun()

    else:

        st.error(response["error"])


# --------------------------------------------------
# Footer
# --------------------------------------------------

render_footer()