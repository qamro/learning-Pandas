import pandas as pd

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
data_list = [
    {"Name": "Qamro", "Age": 18, "City": "Sétif"},
    {"Name": "Bassem", "Age": 18, "City": "Mila"},  
    {"Name": "Firas", "Age": 19, "City": "Jijel"},
    {"Name": "Seddik", "Age": 41, "City": "Batna"},
    {"Name": "Raiden", "Age": 39, "City": "Béjaia"}
]
df_from_list = pd.DataFrame(data_list)
print(df_from_list) 