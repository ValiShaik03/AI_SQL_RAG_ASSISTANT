import streamlit as st


def render_table_selector(tables):
    """
    Renders:
    - Search box
    - Table dropdown

    Returns:
        selected_table (str)
    """

    st.subheader("🔍 Select Table")

    search = st.text_input(
        "Search Tables",
        placeholder="Type table name..."
    )

    # -----------------------------
    # Filter Tables
    # -----------------------------

    if search:

        filtered_tables = [
            table
            for table in tables
            if search.lower() in table.lower()
        ]

    else:

        filtered_tables = tables

    # -----------------------------
    # Empty Search Result
    # -----------------------------

    if not filtered_tables:

        st.warning("No matching tables found.")

        return None

    # -----------------------------
    # Dropdown
    # -----------------------------

    selected_table = st.selectbox(
        "Available Tables",
        filtered_tables,
        key="table_selector"
    )

    return selected_table