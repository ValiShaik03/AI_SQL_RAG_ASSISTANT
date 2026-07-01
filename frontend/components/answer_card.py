import streamlit as st


def render_answer(answer: str):

    with st.chat_message("assistant"):

        st.markdown(
            f"""
<div style="
background:#1E1E1E;
padding:18px;
border-radius:12px;
border-left:6px solid #00C853;
margin-bottom:15px;
">

### 🤖 AI Assistant

{answer}

</div>
""",
            unsafe_allow_html=True,
        )