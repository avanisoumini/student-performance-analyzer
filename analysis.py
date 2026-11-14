#grading and finding avg
import pandas as pd
import numpy as np

df = pd.read_csv("data/students_clean.csv")
print(df.shape)
print(df.describe())
subjects = ["maths", "physics", "python", "english"]
df["total"] = df[subjects].sum(axis=1)
df["average"] = df[subjects].mean(axis=1)
print(df[["name", "total", "average"]])
df["result"] = np.where(df["average"] >= 40, "Pass", "Fail")
print(df[["name", "average", "result"]])

conditions = [
    df["average"] >= 85,
    df["average"] >= 70,
    df["average"] >= 55,
    df["average"] >= 40,
    
]
grades = ["A", "B", "C", "D"]
df["grade"] = np.select(conditions, grades, default="F")
print(df[["name", "average", "grade"]])
topper = df.loc[df["average"].idxmax()]
print(topper["name"], topper["average"])
print(df[subjects].mean())
print(df["grade"].value_counts())
print(df["result"].value_counts())
df.to_csv("data/students_analysed.csv", index=False)