import pandas as pd

# CSV file
df = pd.read_csv("students.csv")  #  reading a CSV file named "students.csv"
print(df)  # printing the DataFrame

# if u have a very large data in the CSV file, it will show only the first 5 rows and the last 5 rows of the DataFrame.
# if u want to print all the rows of the DataFrame, you can use the to_string() method.
print(df.to_string()) # that's it 
print()


# JSON file
df = pd.read_json("students.json")  #  reading a JSON file named "students.json"
print(df)  # printing the DataFrame

# if u have a very large data in the JSON file, it will show only the first 5 rows and the last 5 rows of the DataFrame.
# if u want to print all the rows of the DataFrame, you can use the to_string() method.
print(df.to_string()) # that's it 
print()



# EXCEL file
df = pd.read_excel("students.xlsx")  #  reading an EXCEL file named "students.xlsx"
print(df)  # printing the DataFrame

# if u have a very large data in the EXCEL file, it will show only the first 5 rows and the last 5 rows of the DataFrame.
# if u want to print all the rows of the DataFrame, you can use the to_string() method.
print(df.to_string()) # that's it 
print()