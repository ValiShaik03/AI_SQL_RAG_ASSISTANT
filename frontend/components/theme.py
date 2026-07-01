import streamlit as st


def load_theme():

    with open(
        "assets/styles.css",
        encoding="utf-8"
    ) as css:

        st.markdown(

            f"""
<style>

{css.read()}

</style>
""",

            unsafe_allow_html=True

        )