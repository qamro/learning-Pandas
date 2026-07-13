import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print()



# selection by column label
print(df["Name"])  # Accessing the "Name" column
print()
print(df[["Name", "Age"]])  # Accessing multiple columns
print()



# selection by row index
print(df.loc[0])  # Accessing the first row 
print()

# to make a row index, we can use the set_index() method to set a column as the index of the DataFrame.
df_with_index = df.set_index("Name")
print(df_with_index)
print(df_with_index.loc["Qamro"])  # Accessing the first row by index label
print()
# or we use the usuam method to set a column as the index of the DataFrame when we create the DataFrame.    
df_with_index = pd.read_csv("students.csv", index_col=["Name"])
print(df_with_index)
print(df_with_index.loc["Seddik"])  # Accessing the first row by index label
print() 



# selection by row index and column label
print(df.loc[0, "Name"])  # Accessing the value in the first row
print()
print(df.loc[0, ["Name", "Age"]])  # Accessing multiple values in the first row
print()
print(df.loc[[0, 1], ["Name", "Age"]])  # Accessing multiple rows and columns
print()
print(df.iloc[0:2])  # Accessing a range of rows and all columns
print()
print(df.loc[0:2, ["Name", "Age"]])  # Accessing a range of rows and specific columns   
print()
print(df.iloc[0:2])  # Accessing a range of rows and all columns
print()
print(df.iloc[0:2, 0:2])  # Accessing a range of rows and columns by integer index
print()
print(df.iloc[0:4:2, 0:2])  # Accessing a range of rows and columns by integer index with a step of 2
print()
print()
print()