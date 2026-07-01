import streamlit as st

from components.answer_card import render_answer
from components.sql_card import render_sql
from components.metric_cards import render_metrics
from components.result_table import render_table


def render_chat(chat, index):

    response = chat["response"]

    # ---------------- USER ---------------- #

    with st.chat_message("user"):

        st.markdown(chat["question"])

    # ---------------- AI ---------------- #

    with st.chat_message("assistant"):

        render_answer(response["answer"])

        render_metrics(
            response["rows_returned"],
            response["execution_time_ms"]
        )

        with st.expander("💻 Generated SQL"):

            render_sql(response["generated_sql"])

        with st.expander("📊 Query Results"):

            render_table(
                response["data"],
                key_suffix=index
            )

        st.divider()