import pandas as pd

# data cleaning is the process of fixing or removing incomplete, incorrect, or irrelevant data
# NOTE: 75% of work done with pandas is data cleaning 

df = pd.read_csv("students.csv")
print(df)
print()

# Drop irrelevant column