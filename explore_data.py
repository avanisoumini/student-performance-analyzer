import pandas as pd 
df = pd.read_csv("data/student_messy.csv")
print(df.shape)
print(df.info())
print(df.isnull().sum())
print(df.duplicated().sum())
print(df[df["python"] > 100])
df = df.drop_duplicates()
df = df[df["python"]<=100]
df = df[df["attendance"]<=100]
df["physics"] = df["physics"].fillna(df["physics"].mean())
print(df.shape)
print(df.isnull().sum())
df.to_csv("data/students_clean.csv", index=False)