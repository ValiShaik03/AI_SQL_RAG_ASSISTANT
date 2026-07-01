import streamlit as st


def render_header():

    st.title("🤖 AI SQL RAG Assistant")

    st.caption(
        "Ask natural language questions and let AI generate SQL automatically."
    )

    st.info(
        """
💡 **Example Questions**

• Show all employees

• Highest salary

• Employees in IT department

• Average salary by department

• Employees hired after 2022
"""
    )
