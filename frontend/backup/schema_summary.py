import streamlit as st


def render_schema_summary(summary):
    """
    Displays a summary of the selected table schema.

    Expected summary dictionary:
    {
        "columns": 8,
        "primary_key": "employee_id",
        "numeric_columns": 2,
        "text_columns": 5,
        "date_columns": 1
    }
    """

    if not summary:
        st.warning("No schema summary available.")
        return

    st.subheader("📑 Schema Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            label="🧩 Total Columns",
            value=summary.get("columns", 0)
        )

        st.metric(
            label="🔢 Numeric Columns",
            value=summary.get("numeric_columns", 0)
        )

    with col2:

        st.metric(
            label="🔑 Primary Key",
            value=summary.get("primary_key", "-")
        )

        st.metric(
            label="📝 Text Columns",
            value=summary.get("text_columns", 0)
        )

        st.metric(
            label="📅 Date Columns",
            value=summary.get("date_columns", 0)
        )

    st.divider()