import streamlit as st


def render_table_info(info):
    """
    Displays information about the selected table.

    Expected info dictionary:
    {
        "table": "employees",
        "rows": 5,
        "columns": 8,
        "primary_key": "employee_id"
    }
    """

    if not info:
        st.warning("No table information available.")
        return

    st.subheader("📋 Table Information")

    col1, col2 = st.columns(4)

    with col1:
        st.metric(
            label="📄 Table",
            value=info.get("table", "-")
        )

    with col2:
        st.metric(
            label="📊 Rows",
            value=info.get("rows", 0)
        )

    with col3:
        st.metric(
            label="🧩 Columns",
            value=info.get("columns", 0)
        )

    with col4:
        st.metric(
            label="🔑 Primary Key",
            value=info.get("primary_key", "-")
        )

    st.divider()