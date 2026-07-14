import pandas as pd

# aggregate functions are used to perform a calculation on a set of values and return a single value.

df = pd.read_csv("students.csv")
print(df)
print()



# aggregate function on the whole DataFrame. 

# if we try this aggregate function on a column that contains non-numeric values, we will get an error.
# for example, if we try to get the sum of the "Name" column.
#  we will get an error because the "Name" column contains non-numeric values.
# so we need to select only the numeric columns before applying the aggregate functions.
# and we do that by passing numeric_only=True in the aggregate function.
print(df.sum(numeric_only=True))  # Get the sum of the numeric columns
print()
print(df.mean(numeric_only=True)) # get the mean of numeric columns
print()
print(df.min(numeric_only=True)) # get the minimum of numeric columns
print()
print(df.max(numeric_only=True)) # get the maximum of numeric columns
print()
print(df.count()) # in count function we dont need to pass the numeric_only=True 
                    # count function returns the number of value in each column 
print()




# aggregate function on specific columns in the DataFrame. 

# 
print(df["Age"].sum())  # Get the sum of the numeric columns
print()
print(df["Age"].mean()) # get the mean of numeric columns
print()
print(df.min()) # get the minimum of numeric columns
print()
print(df.max()) # get the maximum of numeric columns
print()
print(df.count()) # in count function we dont need to pass the numeric_only=True 
                    # count function returns the number of value in each column 
print()