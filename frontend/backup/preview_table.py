import json
import pandas as pd
import streamlit as st


def render_preview_table(preview_data):
    """
    Professional Preview Table Component

    Features
    --------
    ✅ Search records
    ✅ Pagination
    ✅ Record count
    ✅ CSV download
    ✅ JSON download
    ✅ Responsive dataframe

    Expected preview_data:

    {
        "rows": [...],
        "page":1,
        "page_size":10,
        "total_rows":100,
        "total_pages":10
    }
    """

    st.subheader("📄 Preview Data")

    if not preview_data:

        st.warning("No preview data found.")

        return

    rows = preview_data.get("rows", [])

    if len(rows) == 0:

        st.info("Table contains no records.")

        return

    page = preview_data.get("page", 1)
    page_size = preview_data.get("page_size", 10)
    total_rows = preview_data.get("total_rows", len(rows))
    total_pages = preview_data.get("total_pages", 1)

    df = pd.DataFrame(rows)

    # ---------------------------------------------------
    # Search
    # ---------------------------------------------------

    search = st.text_input(
        "🔍 Search Records",
        placeholder="Search in current page..."
    )

    if search:

        mask = df.astype(str).apply(
            lambda col: col.str.contains(
                search,
                case=False,
                na=False
            )
        ).any(axis=1)

        df = df[mask]

    # ---------------------------------------------------
    # Information
    # ---------------------------------------------------

    left, right = st.columns([2, 1])

    with left:

        start = ((page - 1) * page_size) + 1

        end = min(page * page_size, total_rows)

        st.caption(
            f"Showing **{start} - {end}** of **{total_rows}** records"
        )

    with right:

        st.caption(
            f"Page **{page} / {total_pages}**"
        )

    # ---------------------------------------------------
    # Data
    # ---------------------------------------------------

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # ---------------------------------------------------
    # Downloads
    # ---------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        csv = df.to_csv(index=False)

        st.download_button(
            "⬇ Download CSV",
            csv,
            file_name="table_preview.csv",
            mime="text/csv",
            use_container_width=True,
            key="csv_download"
        )

    with col2:

        json_data = json.dumps(
            df.to_dict(
                orient="records"
            ),
            indent=4,
            default=str
        )

        st.download_button(
            "⬇ Download JSON",
            json_data,
            file_name="table_preview.json",
            mime="application/json",
            use_container_width=True,
            key="json_download"
        )

    st.divider()

    # ---------------------------------------------------
    # Pagination Status
    # ---------------------------------------------------

    prev_disabled = page <= 1
    next_disabled = page >= total_pages

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:

        st.button(
            "⬅ Previous",
            disabled=prev_disabled,
            use_container_width=True,
            key="previous_page"
        )

    with col2:

        st.markdown(
            f"""
            <div style="
                text-align:center;
                font-size:18px;
                font-weight:bold;
                padding-top:8px;
            ">
                Page {page} of {total_pages}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.button(
            "Next ➡",
            disabled=next_disabled,
            use_container_width=True,
            key="next_page"
        )