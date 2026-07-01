import streamlit as st
import pandas as pd

from utils.api_client import (
    get_stats,
    get_tables,
    get_table_info,
    get_schema,
    get_preview,
)

from components.sidebar import render_sidebar
from components.footer import render_footer
from components.theme import load_theme
from components.hero import render_hero

# -----------------------------------------------------
# Page Configuration
# -----------------------------------------------------

st.set_page_config(
    page_title="Database Explorer",
    page_icon="🗂️",
    layout="wide",
)

render_sidebar()
load_theme()


render_hero(
    icon="🗄️",
    title="Database Explorer",
    subtitle="Browse database tables, schemas and preview records instantly."
)


# -----------------------------------------------------
# Load Database Information
# -----------------------------------------------------

stats = get_stats()
tables = get_tables()

if not tables:

    st.error("No tables found.")

    st.stop()


# -----------------------------------------------------
# Database Overview
# -----------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "📦 Tables",
        stats["total_tables"]
    )

with col2:

    st.metric(
        "📄 Total Rows",
        stats["total_rows"]
    )

with col3:

    st.metric(
        "🧱 Columns",
        stats["total_columns"]
    )

with col4:

    st.metric(
        "💾 Database",
        stats["database"]
    )

st.divider()


# -----------------------------------------------------
# Table Selection
# -----------------------------------------------------

search = st.text_input(
    "🔍 Search Tables",
    placeholder="Type table name..."
)

filtered_tables = [

    table

    for table in tables

    if search.lower() in table.lower()

]

if len(filtered_tables) == 0:

    st.warning("No matching tables found.")

    st.stop()

selected_table = st.selectbox(

    "Select Table",

    filtered_tables

)

st.divider()


# -----------------------------------------------------
# Load Selected Table Information
# -----------------------------------------------------

table_info = get_table_info(selected_table)

schema = get_schema(selected_table)

preview = get_preview(
    selected_table,
    page=1,
    page_size=10
)

st.success(f"Loaded table: **{selected_table}**")

# -----------------------------------------------------
# Table Information
# -----------------------------------------------------

st.divider()

st.subheader("📋 Table Information")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Rows",
        table_info["rows"]
    )

with col2:

    st.metric(
        "Columns",
        table_info["columns"]
    )

with col3:

    primary = table_info["primary_key"]

    if primary:

        st.metric(
            "Primary Key",
            primary
        )

    else:

        st.metric(
            "Primary Key",
            "None"
        )


# -----------------------------------------------------
# Schema
# -----------------------------------------------------

st.divider()

st.subheader("📑 Table Schema")

schema_df = pd.DataFrame(schema)

st.dataframe(
    schema_df,
    use_container_width=True,
    hide_index=True
)


# -----------------------------------------------------
# Schema Summary
# -----------------------------------------------------

numeric = 0
text = 0
date = 0

for row in schema:

    dtype = row["Type"].lower()

    if any(
        x in dtype
        for x in [
            "int",
            "decimal",
            "float",
            "double",
            "bigint",
            "smallint"
        ]
    ):

        numeric += 1

    elif any(
        x in dtype
        for x in [
            "date",
            "datetime",
            "timestamp"
        ]
    ):

        date += 1

    else:

        text += 1


st.divider()

st.subheader("📊 Schema Summary")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "Numeric Columns",
        numeric
    )

with c2:

    st.metric(
        "Text Columns",
        text
    )

with c3:

    st.metric(
        "Date Columns",
        date
    )

# -----------------------------------------------------
# Preview Data
# -----------------------------------------------------

st.divider()

st.subheader("👀 Preview Data")

preview_rows = preview["rows"]

preview_df = pd.DataFrame(preview_rows)

# -----------------------------------------------------
# Search Records
# -----------------------------------------------------

search_record = st.text_input(
    "🔍 Search Records",
    placeholder="Search in current page..."
)

if search_record:

    mask = preview_df.astype(str).apply(
        lambda column: column.str.contains(
            search_record,
            case=False,
            na=False
        )
    ).any(axis=1)

    preview_df = preview_df[mask]

# -----------------------------------------------------
# Table
# -----------------------------------------------------

st.dataframe(
    preview_df,
    use_container_width=True,
    hide_index=True
)

# -----------------------------------------------------
# Record Information
# -----------------------------------------------------

left, right = st.columns(2)

with left:

    st.caption(
        f"Showing {len(preview_df)} of {preview['total_rows']} records"
    )

with right:

    st.caption(
        f"Page {preview['page']} of {preview['total_pages']}"
    )

# -----------------------------------------------------
# Downloads
# -----------------------------------------------------

csv = preview_df.to_csv(index=False)

st.download_button(
    "⬇ Download CSV",
    csv,
    file_name=f"{selected_table}.csv",
    mime="text/csv",
    use_container_width=True
)

import json

json_data = json.dumps(
    preview_df.to_dict(orient="records"),
    indent=4,
    default=str
)

st.download_button(
    "⬇ Download JSON",
    json_data,
    file_name=f"{selected_table}.json",
    mime="application/json",
    use_container_width=True
)

# -----------------------------------------------------
# Pagination
# -----------------------------------------------------

st.divider()

col1, col2, col3 = st.columns([1, 2, 1])

with col1:

    if st.button(
        "⬅ Previous",
        disabled=preview["page"] <= 1
    ):

        st.session_state.page -= 1

        st.rerun()

with col2:

    st.markdown(
        f"""
        <div style="text-align:center;font-size:18px;font-weight:bold;">
        Page {preview['page']} of {preview['total_pages']}
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    if st.button(
        "Next ➡",
        disabled=preview["page"] >= preview["total_pages"]
    ):

        st.session_state.page += 1

        st.rerun()