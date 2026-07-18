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
df["Pet"] = ["Cat", "Dog", None, None, "Bird"]
print(df)
print()

# Drop all the rows that contain missing data in the Average column
df_1 = df.dropna(subset=["Average"]) # dropna method means drop Not Available
print(df_1)
print()
# Drop all the rows that contain missing data in the Average and Pet columns
df_2 = df.dropna(subset=["Average", "Pet"])
print(df_2)
print()

# replace all the missing data by a specific value in the average column
# using the fillna({"column": "the new data that we want to fill"})
df_3 = df.fillna({"Average": "No Average"})
print(df_3)
print()
# replace all the missing data by a specific value in the average and Pet columns
df_3 = df.fillna({"Average": "No Average", "Pet": "No Pet"})
print(df_3)
print()






# Fix inconsistent values and data in a specific column
# using df["column"].replace({dictionary of previous data as a keys and new data as a values})
df["City"] = df["City"].replace({"Sétif": "SÉTIF",
                                "Mila": "MILA",
                                "Jijel": "JIJEL",
                                "Batna": "BATNA",
                                "Béjaia": "BÉJAYA"})
print(df)
print()





# Standardize text in a specific column
# using all the different string methods
# for example make all the values in the city column in lower letters
df["City"] = df["City"].str.lower()
print(df)
print()
# make all the values in the city column in upper letters
df["City"] = df["City"].str.upper()
print(df)
print()
# for example make all the values in the city column start with a capital letter
df["City"] = df["City"].str.capitalize()
print(df)
print()





# Fix or change data types
# using the df["column"].astype(the type we want) method
# we need to add a new column to make it clear and perform this operation
df["Rich"] = [0, 0, 0, 1, 0]
print(df)
print()
# change the type data in Rich column from integer to boolean cuz the column contains only 0 and 1 values
df["Rich"] = df["Rich"].astype(bool)
