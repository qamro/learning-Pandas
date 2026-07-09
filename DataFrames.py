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
print()



# accessing multiple rows using loc and iloc
print(df_with_index.iloc[0:2])  # Accessing the first two rows by integer index
print(df_with_index.loc["student1":"student2"])  # Accessing the first two rows by index label
print()



# to access a specific value in the DataFrame, you can use the column label and the index label.
# we use the loc or iloc method to access a specific value in the DataFrame.
# df.loc[index_label, column_label] or df.iloc[row_index, column_index]
print(df_with_index.loc["student1", "Name"])  # Accessing the value in the "Name" column of the first row
print(df_with_index.iloc[0, 0])  # Accessing the value in the first column of the first row by integer index
print() 
# to access a specific value in the DataFrame, you can also use the at method.
print(df_with_index.at["student1", "Name"])  # Accessing the value in the "Name" column of the first row
print()



# to access many values in the DataFrame, you can use the loc method with a list of index labels and a list of column labels.
# Accessing the "Name" and "Age" columns of the first two rows
print(df_with_index.loc[["student1", "student2"], ["Name", "Age"]])   
# or we can use the iloc method with a list of integer indexes and a list of integer indexes.
# Accessing the first two rows and the first two columns by integer index
print(df_with_index.iloc[[0, 1], [0, 1]])



# to change a value in a DataFrame, you can use the column label and the index label to assign a new value.
df_with_index.loc["student1", "Age"] = 20
df_with_index.loc["student1", "City"] = "Algiers"
print(df_with_index)
print()




# to add a new column to a DataFrame, you can use the column label and assign a new value.
# here we have the same country which is Algeria for all the students
# we can add a new column to the DataFrame and assign the value "Algeria" to all the rows.
df_with_index["Country"] = "Algeria" 
print(df_with_index)
# otherwise, we can assign different values to each row by using a list or a Series.
df_with_index["Country"] = ["Algeria", "Portugal", "Tunisia", "Libya", "Egypt"]
print(df_with_index)
print()





# to add a new row to a DataFrame, you can use the loc method with a new index label and assign a new value.
df_with_index.loc["student6"] = ["Ahmed", 25, "Skikda", "Algeria"]
print(df_with_index)
# or by pd.concat() method, we can concatenate two DataFrames together.
new_row = pd.DataFrame([{"Name": "Ahmed", "Age": 25, "City": "Skikda", "Country": "Algeria"}], index=["student6"])
df = pd.concat([df_with_index, new_row])    
print(df)