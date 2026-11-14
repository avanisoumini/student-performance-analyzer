#testing 
import pandas as pd

df = pd.read_csv("data/students_analysed.csv")

# Test 1: there should be no empty cells
assert df.isnull().sum().sum() == 0, "There are missing values"
# Test 2: marks must be between 0 and 100
marks = ["maths", "physics", "python", "english"]
assert df[marks].min().min() >= 0, "A mark is below 0"
assert df[marks].max().max() <= 100, "A mark is above 100"

# Test 3: attendance must be between 0 and 100
assert df["attendance"].between(0, 100).all(), "Attendance is outside 0-100"

# Test 4: no student should appear twice
assert not df["student_id"].duplicated().any(), "Duplicate student found"
# Test 5: every grade must be A, B, C, D or F
assert df["grade"].isin(["A","B","C","D","F"]).all(), "something's wrong"

print("All tests passed")