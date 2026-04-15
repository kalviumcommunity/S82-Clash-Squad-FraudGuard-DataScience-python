import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Convert to datetime (change column name accordingly)
df['date'] = pd.to_datetime(df['date'])

# Sort by date (VERY IMPORTANT)
df = df.sort_values(by='date')

# Line plot
plt.figure()
plt.plot(df['date'], df['sales'])

# Labels
plt.xlabel("Date")
plt.ylabel("Sales")
plt.title("Sales Trend Over Time")

plt.show()