import pandas as pd 

"""
NOTE:
merge()  → "Find matching keys between two DataFrames"
join()   → "Combine mainly using indexes"
concat() → "Put DataFrames together"
"""

"""
NOTE: join() and merge() are almost the same the difference is:
merge() → join using columns/keys and the key is generally on="id"
join() → join using indexes
"""

# DataFrames
df1 = pd.DataFrame({
    "id": [1, 2, 3, 4],
    "name": ["qamro", "raiden", "bassem", "raid"],
    "city": ["Paris", "London", "Paris", "Madrid"]
})

df2 = pd.DataFrame({
    "id": [3, 4, 5, 6],
    "age": [21, 22, 20, 23]
})

print(df1)
print(df2)





# Merge
"""
NOTE: u should remove the id column from one the dataframes to make the pd.join() works 
Because the pd.join() its the same as pd.merge() but pd.join() works on indexes 
We shouldn't have any same column in the dataframes that we want to make a pd.join()
"""
# INNER
pd.merge(df1, df2, on="id", how="inner")

# LEFT
pd.merge(df1, df2, on="id", how="left")

# RIGHT
pd.merge(df1, df2, on="id", how="right")

# OUTER
pd.merge(df1, df2, on="id", how="outer")






# Join

# Left join
df1.join(df2, how="left")

# Right join
df1.join(df2, how="right")

# inner join
df1.join(df2, how="inner")

# outer join
df1.join(df2, how="outer")




# concatenate

# Stack rows(concatenate rows)
pd.concat([df1, df2]) # its axis=0 which means rows by default

# Put columns side-by-side
pd.concat([df1, df2], axis=1) # axis=1 means columns