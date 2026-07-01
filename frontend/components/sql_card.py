import streamlit as st


def render_sql(sql):

    st.code(
        sql,
        language="sql",
        line_numbers=True
    )