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
df_with_index = pd.DataFrame(data, index=['student1', 'student2', 'student3', 'student4', 'student5']) 
print(df_with_index)