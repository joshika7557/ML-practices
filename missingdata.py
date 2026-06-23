import pandas as pd

data = {
    "Student": ["Rahul", "Priya", "Arun", "Meena"],
    "Attendance": [90, None, 85, 95]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nAfter Handling Missing Data:")
print(df)