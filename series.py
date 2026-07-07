import pandas as pd 

# series are one-dimensional labeled arrays capable of holding any data type (integers, strings, floats, Python objects, etc.)
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
print(series_with_index['a'])  # Accessing the element with index label 'a'
# or you can use the index labels with loc method   
print(series_with_index.loc['a'])  # Accessing the element with index label 'a'
print()
# to change a value in a Series, you can use the index label to assign a new value.
series_with_index['a'] = 100
series_with_index.loc['a'] = 100 # or you can use the loc method to assign a new value.
print(series_with_index)
print()
# to change the index labels of a Series, you can use the index attribute.
series_with_index.index = ['A', 'B', 'C', 'D', 'E']
print(series_with_index)
print()

# FILTERING
print(series_with_index[series_with_index > 100])  # Filtering elements greater than 100
print(series_with_index[series_with_index > 200])  # Filtering elements greater than 200
print(series_with_index[series_with_index < 200])  # Filtering elements less than 200
print()



# above we use a list as a data, now we will use a dictionary as a data to create a series.
data_dict = {'a': 10, 'b': 234, 'c': 32, 'd': 443, 'e': 500}
series_from_dict = pd.Series(data_dict)
print(series_from_dict)
# as u can see the index labels are taken from the keys of the dictionary by default.
# and the data are taken from the values of the dictionary by default.
# the accessing and filtering of the series created from a dictionary is the same as the series created from a list.
print(series_from_dict['a'])  # Accessing the element with index label 'a'
print(series_from_dict.loc['a'])  # Accessing the element with index label 'a'
series_from_dict['a'] = 100
series_from_dict.loc['a'] = 100 # or you can use the loc method to assign a new value.
print(series_from_dict) 
print(series_from_dict[series_from_dict > 100])  # Filtering elements greater than 100