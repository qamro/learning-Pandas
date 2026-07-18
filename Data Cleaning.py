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




# Handle missing data

# NOTE: None means nothing here, no value
# NOTE: float("nan")"Not a Number" used to indicate an undefined, invalid, or missing numeric value, while still technically being of type float.
# Drop all the rows that contain a missing value(float("nan") or None)
# Drop all the rows that contain a missing data like "float("nan") data" or "None data"
# we need to add new columns that contain missing data to perform this operation
df["Average"] = [10.15, float("nan"), 12.88, None, 10.01]
print(df)
print()

# Drop all the rows that contain missing data in the Average column
df_1 = df.dropna(subset=["Average"]) # dropna method means drop Not Available
print(df_1)
print()

# To replace all the missing data by a specific value in the average column
df_2 = df.fillna({"Average": "We dont know"})
print(df_2)
print()
