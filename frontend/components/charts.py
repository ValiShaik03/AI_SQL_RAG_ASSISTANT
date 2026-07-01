import pandas as pd
import plotly.express as px
import streamlit as st


# ---------------------------------------------------
# Department Bar Chart
# ---------------------------------------------------

def render_department_chart(data):

    st.subheader("📊 Employees by Department")

    if not data:

        st.info("No data available.")

        return

    df = pd.DataFrame(data)

    fig = px.bar(

        df,

        x="department",

        y="total",

        text="total",

        title="Employees in Each Department"

    )

    fig.update_layout(

        xaxis_title="Department",

        yaxis_title="Employees",

        height=450,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------
# Department Pie Chart
# ---------------------------------------------------

def render_department_pie(data):

    st.subheader("🥧 Department Distribution")

    if not data:

        st.info("No data available.")

        return

    df = pd.DataFrame(data)

    fig = px.pie(

        df,

        values="total",

        names="department",

        hole=0.45

    )

    fig.update_layout(
        height=450,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------
# Salary Histogram
# ---------------------------------------------------

def render_salary_histogram(data):

    st.subheader("💰 Salary Distribution")

    if not data:

        st.info("No data available.")

        return

    df = pd.DataFrame(data)

    fig = px.histogram(

        df,

        x="salary",

        nbins=10,

        title="Salary Distribution"

    )

    fig.update_layout(

        xaxis_title="Salary",

        yaxis_title="Employees",

        height=450,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ---------------------------------------------------
# Hiring Trend
# ---------------------------------------------------

def render_hiring_trend(data):

    st.subheader("📈 Hiring Trend")

    if not data:

        st.info("No data available.")

        return

    df = pd.DataFrame(data)

    fig = px.line(

        df,

        x="year",

        y="total",

        markers=True,

        title="Employees Hired Per Year"

    )

    fig.update_layout(

        xaxis_title="Year",

        yaxis_title="Employees",

        height=450,

        template="plotly_dark",

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        margin=dict(
            l=20,
            r=20,
            t=50,
            b=20
        )

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )