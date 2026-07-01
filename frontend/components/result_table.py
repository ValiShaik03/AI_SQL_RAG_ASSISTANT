import streamlit as st
import pandas as pd

def render_table(data, key):

    if not data:
        return

    df = pd.DataFrame(data)

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    json_data = df.to_json(
        orient="records",
        indent=4
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            "⬇ Download CSV",
            csv,
            "results.csv",
            "text/csv",
            key=f"csv_{key}"
        )

    with col2:

        st.download_button(
            "⬇ Download JSON",
            json_data,
            "results.json",
            "application/json",
            key=f"json_{key}"
        )