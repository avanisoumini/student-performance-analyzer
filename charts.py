import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("data/students_analysed.csv")
subjects = ["maths", "physics", "python", "english"]
averages = df[subjects].mean()

plt.bar(subjects, averages)
plt.title("Class Average by Subject")
plt.xlabel("Subject")
plt.ylabel("Average marks")
plt.savefig("charts/subject_averages.png")
plt.show()
grade_counts = df["grade"].value_counts()

grade_counts = df["grade"].value_counts()

plt.bar(grade_counts.index, grade_counts.values)
plt.title("Number of Students per Grade")
plt.xlabel("Grade")
plt.ylabel("Number of students")
plt.savefig("charts/grade_distribution.png")
plt.show()
plt.scatter(df["attendance"], df["average"])
plt.scatter(df["attendance"], df["average"])

for i in range(len(df)):
    plt.text(df["attendance"][i], df["average"][i], df["name"][i])

plt.title("Attendance vs Average Marks")
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average marks")
plt.savefig("charts/attendance_vs_average.png")
plt.show()
