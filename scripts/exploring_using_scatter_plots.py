import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Scatter plot
plt.figure()
plt.scatter(df['hours_studied'], df['marks'])

# Labels
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied vs Marks")

plt.show()