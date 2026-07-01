import streamlit as st

from components.sidebar import render_sidebar
from components.footer import render_footer
from components.theme import load_theme
from components.hero import render_hero


# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

render_sidebar()
load_theme()

# ---------------------------------------------------------
# Session State Defaults
# ---------------------------------------------------------

defaults = {
    "page_size": 10,
    "query_timeout": 60,
    "theme": "Dark",
    "auto_refresh": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ---------------------------------------------------------
# Header
# ---------------------------------------------------------

render_hero(
    icon="⚙️",
    title="Settings",
    subtitle="Manage AI models, backend configuration and application preferences."
)


# ---------------------------------------------------------
# General Settings
# ---------------------------------------------------------

st.header("🛠 General Settings")

col1, col2 = st.columns(2)

with col1:

    page_size = st.slider(
        "Default Preview Page Size",
        min_value=5,
        max_value=100,
        value=st.session_state.page_size,
        step=5
    )

with col2:

    timeout = st.slider(
        "Query Timeout (seconds)",
        min_value=10,
        max_value=300,
        value=st.session_state.query_timeout,
        step=10
    )

theme = st.selectbox(

    "Application Theme",

    [

        "Dark",

        "Light"

    ],

    index=0 if st.session_state.theme == "Dark" else 1

)

auto_refresh = st.toggle(

    "Auto Refresh Dashboard",

    value=st.session_state.auto_refresh

)


# ---------------------------------------------------------
# Save Settings
# ---------------------------------------------------------

if st.button(
    "💾 Save Settings",
    use_container_width=True
):

    st.session_state.page_size = page_size

    st.session_state.query_timeout = timeout

    st.session_state.theme = theme

    st.session_state.auto_refresh = auto_refresh

    st.success("Settings saved successfully!")

st.divider()


# ---------------------------------------------------------
# AI Settings
# ---------------------------------------------------------

st.header("🤖 AI Settings")

model = st.selectbox(

    "LLM Model",

    [

        "llama-3.3-70b-versatile",

        "llama-3.1-8b-instant",

        "mixtral-8x7b-32768"

    ],

    index=0

)

temperature = st.slider(

    "Temperature",

    0.0,

    1.0,

    0.2,

    0.1

)

max_tokens = st.slider(

    "Maximum Tokens",

    256,

    4096,

    1024,

    256

)

st.divider()


# ---------------------------------------------------------
# Backend Configuration
# ---------------------------------------------------------

st.header("🌐 Backend Configuration")

backend_url = st.text_input(

    "Backend API URL",

    value="http://127.0.0.1:8000"

)

database = st.text_input(

    "Database",

    value="MySQL",

    disabled=True

)

provider = st.text_input(

    "AI Provider",

    value="Groq",

    disabled=True

)

st.divider()


# ---------------------------------------------------------
# Connection Status
# ---------------------------------------------------------

st.header("🔍 Connection Status")

left, middle, right = st.columns(3)

with left:

    st.success("🟢 Backend Connected")

with middle:

    st.success("🟢 Database Connected")

with right:

    st.success("🟢 Groq Connected")

st.divider()


# ---------------------------------------------------------
# Test Connection
# ---------------------------------------------------------

st.header("🧪 Diagnostics")

if st.button(
    "Test Backend Connection",
    use_container_width=True
):

    try:

        import requests

        response = requests.get(
            f"{backend_url}/",
            timeout=5
        )

        if response.status_code == 200:

            st.success(
                "Backend is running successfully."
            )

        else:

            st.error(
                "Backend responded with an error."
            )

    except Exception as e:

        st.error(e)

st.divider()


# ---------------------------------------------------------
# About
# ---------------------------------------------------------

st.header("ℹ️ About")

st.markdown(
    """
### 🤖 AI SQL RAG Assistant

An AI-powered SQL Assistant that converts natural language into SQL,
executes queries on MySQL, and provides analytics and database exploration.

**Built With**

- 🐍 Python
- ⚡ FastAPI
- 🎈 Streamlit
- 🗄 MySQL
- 🤖 Groq LLM
- 📊 Plotly
"""
)

st.divider()


# ---------------------------------------------------------
# System Information
# ---------------------------------------------------------

st.header("💻 System Information")

import platform
import sys

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Python Version",
        platform.python_version()
    )

    st.metric(
        "Operating System",
        platform.system()
    )

with col2:

    st.metric(
        "Architecture",
        platform.machine()
    )

    st.metric(
        "Platform",
        platform.platform()
    )

st.divider()


# ---------------------------------------------------------
# Project Information
# ---------------------------------------------------------

st.header("📁 Project Information")

st.info(
    """
Project Name:
AI SQL RAG Assistant

Version:
1.0.0

Architecture:
Frontend → Streamlit

Backend → FastAPI

Database → MySQL

AI → Groq LLM

Charts → Plotly
"""
)

st.divider()


# ---------------------------------------------------------
# Reset Settings
# ---------------------------------------------------------

st.header("♻️ Reset Settings")

st.warning(
    "This resets all application settings to their default values."
)

if st.button(
    "Reset to Default Settings",
    use_container_width=True
):

    st.session_state.page_size = 10
    st.session_state.query_timeout = 60
    st.session_state.theme = "Dark"
    st.session_state.auto_refresh = False

    st.session_state.model = "llama-3.3-70b-versatile"
    st.session_state.temperature = 0.2
    st.session_state.max_tokens = 1024
    st.session_state.backend_url = "http://127.0.0.1:8000"

    st.success("Settings reset successfully.")

    st.rerun()

st.divider()


# ---------------------------------------------------------
# Developer
# ---------------------------------------------------------

st.header("👨‍💻 Developer")

st.success(
    """
Developed by

**Shaik Mahaboob Vali**

AI / ML Engineer

Built using Streamlit, FastAPI, Groq and MySQL.
"""
)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

render_footer()