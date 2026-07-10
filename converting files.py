import pandas as pd


# Create a simple DataFrame (rows have an index: 0, 1)
df = pd.DataFrame({
    "Name": ["Qamro", "Scofield"],
    "Age": [20, 22],
    "City": ["Sétif", "Fox River"]
})





# Converting the DataFrame to a CSV file

# we use index=False to avoid saving the row index in the CSV file.
# if we use index=True (default), the row index will be saved in the CSV file as an additional column.
df.to_csv("prison_break.csv", index=False)      # Save to CSV (don't save the row index)
df_csv = pd.read_csv("prison_break.csv")        # Read CSV into a DataFrame






# Converting the DataFrame to a JSON file

# when we convert a DataFrame to JSON, we can specify the orientation of the JSON data using the orient parameter.
# NOTE: the default orientation is 'columns', which means that the JSON data will be organized by columns.
# NOTE: indent parameter is just for JSON files not the CSV files
# and we add indent=4 to make the JSON file more readable.
# because indent=4 adds 4 spaces of indentation to each level of the JSON data, making it easier to read and understand.
# we can use indent=2 or indent=4 or any other number of spaces, depending on our preference.

df.to_json("records.json", orient="records", indent=4)
# records: list of dictionaries (most common in APIs, DATA exchanging...)
# each dictionary represents one row, with column names as keys and row values as values.

df.to_json("index.json", orient="index", indent=4)
# index: row index becomes the JSON key

df.to_json("columns.json", orient="columns", indent=4)
# columns: each column is a dictionary of index : value (default)

df.to_json("values.json", orient="values", indent=4)
# values: only the data, no column names

df.to_json("split.json", orient="split", indent=4)
# split: stores columns, index, and data separately

df.to_json("table.json", orient="table", indent=4)
# table: includes schema (column types) and data

# Read JSON back into a DataFrame
df_json = pd.read_json("records.json")







# to convert a CSV file to a JSON file 
"""
| Conversion       | pandas function  |
| ---------------- | ---------------- |
| CSV → DataFrame  | `pd.read_csv()`  |
| DataFrame → JSON | `df.to_json()`   |
"""





# to convert a JSON file to a CSV file 
"""
| Conversion       | pandas function  |
| ---------------- | ---------------- |
| JSON → DataFrame  | `pd.read_json()`  |
| DataFrame → CSV | `df.to_csv()`   |
"""