import pandas as pd 

# series are one-dimensional labeled arrays capable of holding any data type (integers, strings, floating point numbers, Python objects, etc.).
# The axis labels are collectively referred to as the index.
# A pandas Series can be created using the following constructor :
# pandas.Series(data, index, dtype, name, copy)
data = [10, 234, 32, 443, 500]
series = pd.Series(data)
print(series)
print()
# the index is by default an integer index starting from 0.
# You can also specify your own index labels.
series_with_index = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
print(series_with_index)
print()
# Note: that the index labels must be unique and of the same length as the data.
# to access the elements of a Series
# u can use the index labels 
print(series[0])  # Accessing the first element
# or you can use the index labels   
print(series_with_index.loc['a'])  # Accessing the element with index label 'a'