import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data4.csv")
df.columns = df.columns.str.strip()

plt.figure(figsize=(10,8))

# Plot 1 - Bar Chart
plt.subplot(2,2,1)
plt.bar(df["name"], df["mark"])
plt.title("Bar Chart")
plt.xlabel("name")
plt.ylabel("mark")

# Plot 2 - Line Chart
plt.subplot(2,2,2)
plt.plot(df["name"], df["mark"], marker="o")
plt.title("Line Chart")
plt.xlabel("name")
plt.ylabel("mark")

# Plot 3 - Scatter Plot
plt.subplot(2,2,3)
plt.scatter(df["name"], df["mark"])
plt.title("Scatter Plot")
plt.xlabel("name")
plt.ylabel("mark")

# Plot 4 - Pie Chart
plt.subplot(2,2,4)
plt.pie(
    df["mark"],
    labels=df["name"],
    autopct="%1.1f%%"
)
plt.title("Pie Chart")
plt.xlabel("name")
plt.ylabel("mark")

plt.tight_layout()
plt.show()