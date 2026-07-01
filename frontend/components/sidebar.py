import streamlit as st


def render_sidebar():

    with st.sidebar:

        st.markdown("# 🤖 AI SQL RAG")

        st.caption("Natural Language → SQL → AI")

        st.divider()

        st.subheader("System Status")

        st.success("🟢 Backend Online")

        st.success("🟢 MySQL Connected")

        st.success("🟢 Groq Connected")

        st.divider()

        st.subheader("Quick Questions")

        examples = [
            "Show all employees",
            "Who earns the highest salary?",
            "Average salary by department",
            "Employees hired after 2022",
            "Show employees in IT department"
        ]

        for q in examples:

            if st.button(q, use_container_width=True):

                st.session_state["example_question"] = q

        st.divider()

        if st.button("🗑 Clear Chat", use_container_width=True):

            st.session_state.chat_history = []

            st.rerun()

        st.divider()

        st.caption("Version 1.0")

        st.caption("Developed using FastAPI + Groq + Streamlit")