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

# in these functions we don't need to pass the numeric_only=True because Age column is basically numeric 
print(df["Age"].sum())  # Get the sum of the Age columns
print()
print(df["Age"].mean()) # get the mean of Age columns
print()
print(df["Age"].min()) # get the minimum of Age columns
print()
print(df["Age"].max()) # get the maximum of Age columns
print()
print(df["Age"].count()) # get the number of values in Age column
print()

# generally if we use an aggregate functions on multiple columns:
# if all the columns contains numeric values we dont pass numeric_only=True.
# if not all the columns contains numeric values we should pass numeric_only=True, for example:
print(df[["Age", "Country", "Name"]].sum(numeric_only=True))  # Get the sum of the mentioned columns
print()
print(df[["Age", "Country", "Name"]].mean(numeric_only=True)) # get the mean of the mentioned columns
print()
print(df[["Age", "Country", "Name"]].min(numeric_only=True)) # get the minimum of the mentioned columns
print()
print(df[["Age", "Country", "Name"]].max(numeric_only=True)) # get the maximum of the mentioned columns
print()
print(df[["Age", "Country", "Name"]].count()) # get the number of values in the mentioned columns
print()









# this is the most common use of aggregate functions.
# we can use aggregate functions with groupby() method.
# the groupby() method is used to splits data into groups
# apply an operation to each group then combine the results 
# its one of the most useful tools and methods for Data Analysis
# the syntax of groupby method is simple: df.groupby("the column used to create the groups")
# if there are many columns used to create the groups:
# df.groupby(["the first column, the second, the third, ..."])
# to see the the effect of the groupby() method perfectly in the output we should we must create another df.
data2 = {"Students": ["Qamro", "Bassem", "Raiden", "Mouh", "Raid", "Seddik"],
    "Department": ["AI", "AI", "CS", "AI", "IoT", "IoT"],
    "Salary": [5000, 3200, 2500, 4350, 2000, 1600]
    }
df2 = pd.DataFrame(data2)
print(df2)
print()


# group by one column
groups = df2.groupby("Department")
"""
this creates a group:
AI → Qamro, Bassem, Mouh
# CS → Raiden
# IoT → Raid, Seddik
"""


# Calculate the average salary
print(df2.groupby("Department")["Salary"].mean())
print()
"""
the output:
Department
AI     4183.333333
CS     2500.000000
IoT    1800.000000  
"""


# Sum salaries
print(df2.groupby("Department")["Salary"].sum())
print()
"""
the output:
Department
AI     12550
CS      2500
IoT     3600
"""


# Count employees
print(df2.groupby("Department").size())
print()
"""
the output:
Department
AI     3
CS     1
IoT    2
"""



# Multiple aggregations
# NOTE: we can use this multiple aggregation syntax for series or normal DataFrame without groupby() method
print(df2.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum"]))
print()
"""
the output:
                mean   max   min    sum
Department                                
AI        4183.333333  5000  3200  12550
CS        2500.000000  2500  2500   2500
IoT       1800.000000  2000  1600   3600
"""



# Group by multiple columns

# Suppose we add another column:
df2["Gender"] = ["M", "M", "F", "F", "M", "F"]

print(df2.groupby(["Department", "Gender"])["Salary"].mean())
print()
"""
the output:
Department  Gender
AI          F         4350.0
            M         4100.0
CS          F         2500.0
IoT         F         1600.0
            M         2000.0
"""



# Iterate through groups(This prints each department and its corresponding rows)
for department, group in df2.groupby("Department"):
    print(department)
    print(group)
    print()
print()
"""
the output:
AI
    Students Department  Salary Gender
0    Qamro         AI    5000      M
1   Bassem         AI    3200      M
3     Mouh         AI    4350      F

CS
    Students Department  Salary Gender
2   Raiden         CS    2500      F

IoT
    Students Department  Salary Gender
4     Raid        IoT    2000      M
5   Seddik        IoT    1600      F
"""
    