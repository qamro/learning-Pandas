import pandas as pd

# DataFrames are two-dimensional labeled data structures with columns of potentially different types.
# You can think of them like a spreadsheet or SQL table, or a dict of Series objects.
# It is generally the most commonly used pd object.
# A pandas DataFrame can be created using the following constructor:
# pandas.DataFrame(data, index, columns, dtype, copy)
data = {
    "Name": ["Qamro", "Bassem", "Firas", "Seddik", "Raiden"],
    "Age": [18, 18, 19, 41, 39],
    "City": ["Sétif", "Mila", "Jijel", "Batna", "Béjaia"]
}
df = pd.DataFrame(data)
print(df)
print()
df_with_index = pd.DataFrame(data, index=["student1", "student2", "student3", "student4", "student5"]) 
print(df_with_index)
print()

# Note: that the index labels must be unique and of the same length as the data.
# to access the elements of a DataFrame
# you can use the column labels to access the columns of the DataFrame.
print(df["Name"])  # Accessing the "Name" column
print(df[["Name", "Age"]])  # Accessing multiple columns
print()
# you can also use the loc method to access the rows of the DataFrame.
print(df_with_index.loc["student1"])  # Accessing the first row
print()
# you can also use the iloc method to access the rows of the DataFrame by integer index.
print(df_with_index.iloc[0])  # Accessing the first row by integer index
