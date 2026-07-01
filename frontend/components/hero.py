import streamlit as st


def render_hero(icon: str, title: str, subtitle: str):

    html = f"""
<div style="
background:linear-gradient(135deg,#1E293B,#0F172A);
padding:30px;
border-radius:18px;
border:1px solid #334155;
margin-bottom:25px;
box-shadow:0 8px 24px rgba(0,0,0,.25);
">

<div style="display:flex;align-items:center;gap:20px;">

<div style="font-size:55px;">
{icon}
</div>

<div>

<div style="
font-size:40px;
font-weight:700;
color:white;
">
{title}
</div>

<div style="
font-size:18px;
color:#CBD5E1;
margin-top:6px;
">
{subtitle}
</div>

</div>

</div>

</div>
"""

    st.markdown(html, unsafe_allow_html=True)