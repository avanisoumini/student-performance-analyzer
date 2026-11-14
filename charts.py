import altair as alt
import pandas as pd
import streamlit as st

SUBJECTS = ["maths", "physics", "python", "english"]
GRADES = ["A", "B", "C", "D", "F"]

PINK = "#FF6F91"
PURPLE = "#9B8CFF"
MINT = "#4DD0B1"
SUN = "#FFB86B"


def subject_average_chart(df):
    """Bar chart: class average for each subject."""
    st.bar_chart(df[SUBJECTS].mean(), color=PINK)


def grade_distribution_chart(df):
    """Bar chart: how many students got each grade (A to F)."""
    counts = df["grade"].value_counts().reindex(GRADES, fill_value=0)
    st.bar_chart(counts, color=PURPLE)


def attendance_chart(df):
    """Scatter plot: attendance vs average marks. Hover to see the name."""
    chart = (
        alt.Chart(df)
        .mark_circle(size=140, color=MINT)
        .encode(
            x=alt.X("attendance", title="Attendance (%)", scale=alt.Scale(zero=False)),
            y=alt.Y("average", title="Average marks", scale=alt.Scale(zero=False)),
            tooltip=["name", "attendance", "average", "grade"],
        )
        .interactive()
    )
    st.altair_chart(chart)


def student_average_chart(df):
    """Bar chart: average marks of every student."""
    st.bar_chart(df.set_index("name")["average"], color=SUN)


def student_report_chart(df, name):
    """Bar chart: one student's marks next to the class average."""
    marks = df.loc[df["name"] == name, SUBJECTS].iloc[0]
    compare = pd.DataFrame({"Student": marks, "Class average": df[SUBJECTS].mean()})
    st.bar_chart(compare, color=[PINK, PURPLE], stack=False)