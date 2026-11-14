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