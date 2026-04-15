import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data.csv")

# Select numeric column
print(df.dtypes)

# Example column
column = 'age'   # change to your dataset column

# Create histogram
plt.figure()
df[column].hist(bins=10)

# Labels
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Age")

plt.show()