import streamlit as st


def render_user_question(question: str):

    with st.chat_message("user"):

        st.markdown(
            f"""
<div style="
background:#1F2937;
padding:16px;
border-radius:12px;
border-left:5px solid #3B82F6;
margin-bottom:10px;
">

### 👤 You

{question}

</div>
""",
            unsafe_allow_html=True,
        )