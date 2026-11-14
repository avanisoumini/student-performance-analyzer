import pandas as pd
import streamlit as st

from charts import (
    SUBJECTS,
    GRADES,
    subject_average_chart,
    grade_distribution_chart,
    attendance_chart,
    student_average_chart,
    student_report_chart,
)

st.set_page_config(page_title="Student Performance Analyzer", page_icon="🎓", layout="wide")

st.title("🎓 Student Performance Analyzer")
st.caption("Built with Python, Pandas and Streamlit")

# Load the analysed data and add each student's rank
df = pd.read_csv("data/students_analysed.csv")
df["rank"] = df["average"].rank(ascending=False, method="min").astype(int)

# Sidebar filter
st.sidebar.header("🔎 Filters")
chosen_grades = st.sidebar.multiselect("Show grades", GRADES, default=GRADES)
filtered = df[df["grade"].isin(chosen_grades)]

if filtered.empty:
    st.warning("No students match this filter. Choose at least one grade in the sidebar.")
    st.stop()

tab_overview, tab_charts, tab_report = st.tabs(
    ["📋 Overview", "📊 Charts", "🧑‍🎓 Student report"]
)

# Tab 1: summary numbers and the table
with tab_overview:
    top = filtered.loc[filtered["average"].idxmax()]
    pass_rate = (filtered["result"] == "Pass").mean() * 100

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Students", len(filtered))
    c2.metric("Class average", round(filtered["average"].mean(), 1))
    c3.metric("Pass rate", f"{pass_rate:.0f}%")
    c4.metric("Topper", top["name"])

    st.subheader("All students")
    st.dataframe(filtered, hide_index=True)

# Tab 2: the four charts
with tab_charts:
    left, right = st.columns(2)

    with left:
        st.subheader("Class average by subject")
        subject_average_chart(filtered)
        st.subheader("Attendance vs average marks")
        attendance_chart(filtered)

    with right:
        st.subheader("Grade distribution")
        grade_distribution_chart(filtered)
        st.subheader("Average marks per student")
        student_average_chart(filtered)

# Tab 3: individual student report
with tab_report:
    name = st.selectbox("Choose a student", df["name"])
    student = df[df["name"] == name].iloc[0]
    marks = df.loc[df["name"] == name, SUBJECTS].iloc[0]

    r1, r2, r3, r4, r5 = st.columns(5)
    r1.metric("Rank", f"{int(student['rank'])} of {len(df)}")
    r2.metric("Average", round(student["average"], 1))
    r3.metric("Grade", student["grade"])
    r4.metric("Result", student["result"])
    r5.metric("Attendance", f"{student['attendance']:.0f}%")

    strongest = marks.idxmax()
    weakest = marks.idxmin()
    st.info(
        f"💪 Strongest subject: {strongest} ({marks[strongest]:.0f})   |   "
        f"📉 Weakest subject: {weakest} ({marks[weakest]:.0f})"
    )

    if student["attendance"] < 75:
        st.warning("⚠️ Attendance is below 75%.")

    st.subheader(f"{name} vs class average")
    student_report_chart(df, name)