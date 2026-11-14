import pandas as pd 
df = pd.read_csv("data/students.csv")
print(df.shape)
print(df.columns)
print(df["maths"])
print(df.head(3))
print(df.info())
print(df.describe())
print(df)
