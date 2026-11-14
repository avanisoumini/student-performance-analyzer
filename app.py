import streamlit as st
import pandas as pd

st.title("Student Performance Analyzer")

df = pd.read_csv("data/students_analysed.csv")
st.dataframe(df)

st.subheader("Class Summary")

col1, col2, col3 = st.columns(3)
col1.metric("Students", len(df))
col2.metric("Class average", round(df["average"].mean(), 1))

topper = df.loc[df["average"].idxmax()]
col3.metric("Topper", topper["name"])