import streamlit as st


def render_metrics(rows, execution_time):

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "📄 Rows",
            rows
        )

    with col2:
        st.metric(
            "⚡ Time",
            f"{execution_time:.2f} ms"
        )

    with col3:
        st.metric(
            "🧠 Model",
            "Llama 3.3"
        )

    with col4:
        st.metric(
            "💾 Database",
            "MySQL"
        )