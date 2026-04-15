import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Check data types
print(df.dtypes)

# Select numeric columns
col1 = 'age'       # change based on your dataset
col2 = 'salary'    # optional

# Boxplot for single column
plt.figure()
plt.boxplot(df[col1])

plt.title("Boxplot of Age")
plt.ylabel("Age")

plt.show()

# Boxplot for multiple columns (comparison)
plt.figure()
plt.boxplot([df[col1], df[col2]], labels=['Age', 'Salary'])

plt.title("Age vs Salary Boxplot")
plt.ylabel("Values")

plt.show()