import streamlit as st

from components.sidebar import render_sidebar
from components.footer import render_footer

from components.charts import (
    render_department_chart,
    render_department_pie,
    render_salary_histogram,
    render_hiring_trend
)

from components.theme import load_theme

from utils.analytics_api import (
    get_dashboard_metrics,
    get_department_data,
    get_salary_data,
    get_hiring_data,
    get_dashboard_insights
)


# ---------------------------------------------------------
# Page Config
# ---------------------------------------------------------

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

render_sidebar()
load_theme()

# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

st.markdown(
    """
    <h1 style="font-size:56px;font-weight:800;">
        📊 Analytics Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([8, 1])

with col2:
    if st.button("🔄 Refresh"):
        st.rerun()

st.caption(
    "Interactive dashboard for employee database analytics."
)

st.divider()


# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

try:

    with st.spinner("Loading dashboard..."):

        metrics = get_dashboard_metrics()

        department_data = get_department_data()

        salary_data = get_salary_data()

        hiring_data = get_hiring_data()

        insights = get_dashboard_insights()

except Exception as e:

    st.error(f"Failed to load dashboard.\n\n{e}")

    st.stop()

# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

st.subheader("📈 Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "👥 Employees",
        metrics["employees"]
    )

with col2:

    st.metric(
        "💰 Average Salary",
        f"₹ {metrics['avg_salary']:,.0f}"
    )

with col3:

    st.metric(
        "📈 Highest Salary",
        f"₹ {metrics['max_salary']:,.0f}"
    )

with col4:

    st.metric(
        "🏢 Departments",
        metrics["departments"]
    )

st.divider()


# ---------------------------------------------------------
# Charts
# ---------------------------------------------------------

st.markdown(
    """
    <h1 style="
        font-size:52px;
        font-weight:800;
        margin-bottom:20px;
    ">
        📊 Department Analytics
    </h1>
    """,
    unsafe_allow_html=True
)

render_department_chart(
    department_data
)

import pandas as pd

department_df = pd.DataFrame(department_data)

st.download_button(
    label="📥 Download Department Report",
    data=department_df.to_csv(index=False),
    file_name="department_report.csv",
    mime="text/csv"
)

st.divider()


# ---------------------------------------------------------
# Two Charts Side by Side
# ---------------------------------------------------------

left, right = st.columns(2)

with left:

    render_salary_histogram(
        salary_data
    )

with right:

    render_department_pie(
        department_data
    )

st.divider()


# ---------------------------------------------------------
# Hiring Trend
# ---------------------------------------------------------

render_hiring_trend(
    hiring_data
)

st.divider()


# ---------------------------------------------------------
# AI Insights
# ---------------------------------------------------------

st.subheader("🤖 AI Insights")

col1, col2 = st.columns(2)

# ---------------- Highest Paid Department ----------------

with col1:

    highest = insights["highest_paid_department"]

    st.success(
        f"""
🏆 **Highest Paid Department**

**Department:** {highest["department"]}

**Average Salary:** ₹ {highest["avg_salary"]:,.2f}
"""
    )

# ---------------- Lowest Paid Department ----------------

with col2:

    lowest = insights["lowest_paid_department"]

    st.info(
        f"""
📉 **Lowest Paid Department**

**Department:** {lowest["department"]}

**Average Salary:** ₹ {lowest["avg_salary"]:,.2f}
"""
    )

st.divider()

col3, col4 = st.columns(2)

# ---------------- Latest Hiring ----------------

with col3:

    st.warning(
        f"""
📅 **Latest Hiring Year**

{insights["latest_hiring_year"]}
"""
    )

# ---------------- Employee Count ----------------

with col4:

    st.success(
        f"""
👥 **Total Employees**

{insights["total_employees"]}
"""
    )

st.divider()

# ---------------- Overall Insight ----------------

st.markdown("### 💡 AI Summary")

st.info(
    f"""
The organization currently has **{metrics["employees"]} employees**
working across **{metrics["departments"]} departments**.

The **average salary** is **₹ {metrics["avg_salary"]:,.2f}**.

The **highest recorded salary** is **₹ {metrics["max_salary"]:,.2f}**.

The latest employee hiring was in **{insights["latest_hiring_year"]}**.
"""
)


# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------

render_footer()