import streamlit as st

from components.sidebar import render_sidebar
from components.footer import render_footer
from components.theme import load_theme
from components.hero import render_hero

# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------

st.set_page_config(
    page_title="Query History",
    page_icon="🕒",
    layout="wide"
)

render_sidebar()
load_theme()

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

render_hero(
    icon="🕒",
    title="Query History",
    subtitle="Review previous SQL queries, execution time and AI responses."
)

# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# ---------------------------------------------------------
# No History
# ---------------------------------------------------------

if len(st.session_state.chat_history) == 0:

    st.info("No query history found.")

    render_footer()

    st.stop()


# ---------------------------------------------------------
# Search
# ---------------------------------------------------------

search = st.text_input(
    "🔍 Search History",
    placeholder="Search by question..."
)

history = st.session_state.chat_history

if search:

    history = [

        item

        for item in history

        if search.lower() in item["question"].lower()

    ]


# ---------------------------------------------------------
# Display History
# ---------------------------------------------------------

for index, item in enumerate(reversed(history), start=1):

    response = item["response"]

    col_left, col_right = st.columns([12,1])

    with col_left:

        expanded = st.expander(
            f"{index}. {item['question']}",
            expanded=False
        )

    with col_right:

        delete = st.button(
            "🗑",
            key=f"delete_{index}"
        )

    if delete:

        original_index = len(st.session_state.chat_history) - index

        st.session_state.chat_history.pop(original_index)

        st.rerun()

    with expanded:

        st.markdown("### 👤 User Question")

        st.write(item["question"])

        st.markdown("### 🤖 AI Answer")

        st.write(response["answer"])

        st.markdown("### 🧾 Generated SQL")

        st.code(
            response["generated_sql"],
            language="sql"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Rows Returned",
                response["rows_returned"]
            )

        with col2:

            st.metric(
                "Execution Time",
                f"{response['execution_time_ms']} ms"
            )

        if "timestamp" in item:

            st.caption(
                f"🕒 {item['timestamp']}"
            )
        st.divider()

        import pandas as pd

        rows = []

        for item in st.session_state.chat_history:

            rows.append({

                "Question": item["question"],

                "SQL": item["response"]["generated_sql"],

                "Answer": item["response"]["answer"],

                "Rows Returned": item["response"]["rows_returned"],

                "Execution Time": item["response"]["execution_time_ms"],

                "Timestamp": item.get("timestamp", "")

            })

        df = pd.DataFrame(rows)

        st.download_button(

            "📥 Download CSV",

            df.to_csv(index=False),

            "query_history.csv",

            "text/csv",

            use_container_width=True
        )

        import json

        st.download_button(

            "📄 Download JSON",

            json.dumps(rows, indent=4),

            "query_history.json",

            "application/json",

            use_container_width=True
        )

        if st.button(
            "🧹 Clear History",
            use_container_width=True
            ):
            st.session_state.chat_history.clear()

            st.success("History Cleared.")

            st.rerun()


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

render_footer()


# ---------------------------------------------------------
# History Statistics
# ---------------------------------------------------------

total_queries = len(history)

avg_execution = 0

if total_queries > 0:

    avg_execution = sum(
        item["response"]["execution_time_ms"]
        for item in history
    ) / total_queries

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "📊 Total Queries",
        total_queries
    )

with col2:

    st.metric(
        "⚡ Avg Execution Time",
        f"{avg_execution:.1f} ms"
    )

st.divider()