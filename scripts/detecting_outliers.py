import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Select column
col = 'salary'   # change this

# 🔹 1. Visual Inspection (Boxplot)
plt.figure()
plt.boxplot(df[col])
plt.title("Boxplot for Outlier Detection")
plt.ylabel(col)
plt.show()

# 🔹 2. IQR Rule
Q1 = df[col].quantile(0.25)
Q3 = df[col].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Find outliers
outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]

print("Outliers:")
print(outliers)