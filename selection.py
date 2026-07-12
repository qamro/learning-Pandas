import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print()
# selection by column label
print(df["Name"])  # Accessing the "Name" column
print()
print(df[["Name", "Age"]])  # Accessing multiple columns
print()