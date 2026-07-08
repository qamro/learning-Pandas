import pandas as pd
import numpy as np

# there are a lot of ways to create a DataFrame, 
# but the most common way is to use a dictionary of lists or a list of dictionaries.
# we start with
# a dictionary of lists
data = {
    "Name": ["Qamro", "Bassem", "Firas", "Seddik", "Raiden"],
    "Age": [18, 18, 19, 41, 39],
    "City": ["Sétif", "Mila", "Jijel", "Batna", "Béjaia"]
}
df = pd.DataFrame(data)
print(df)
print()

# a list of dictionaries
# each dictionary represents one row.
data_list = [
    {"Name": "Qamro", "Age": 18, "City": "Sétif"},
    {"Name": "Bassem", "Age": 18, "City": "Mila"},  
    {"Name": "Firas", "Age": 19, "City": "Jijel"},
    {"Name": "Seddik", "Age": 41, "City": "Batna"},
    {"Name": "Raiden", "Age": 39, "City": "Béjaia"}
]
df_from_list = pd.DataFrame(data_list)
print(df_from_list) # each dictionary represents one row.
print()


# a list of lists
# each inner list represents one row.
data_list_of_lists = [
    ["Qamro", 18, "Sétif"],
    ["Bassem", 18, "Mila"],
    ["Firas", 19, "Jijel"],
    ["Seddik", 41, "Batna"],
    ["Raiden", 39, "Béjaia"]
]
df_from_list_of_lists = pd.DataFrame(data_list_of_lists, columns=["Name", "Age", "City"])
print(df_from_list_of_lists) # each inner list represents one row.  
print()



# a numpy array
