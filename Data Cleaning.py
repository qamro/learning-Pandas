import pandas as pd

# data cleaning is the process of fixing or removing incomplete, incorrect, or irrelevant data
# NOTE: 75% of work done with pandas is data cleaning 

df = pd.read_csv("students.csv")
print(df)
print()




# Drop irrelevant columns

# Drop Country column
df1 = df.drop(columns=["Country"])
print(df1)
print()
# Drop Country and City columns
df2 = df.drop(columns=["Country", "City"])
print(df2)
print()
# Drop Country and City and Age columns
df3 = df.drop(columns=["Country", "City", "Age"])
print(df3)
print()




# 
