import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print()

# filtering is keeping the rows that match a certain condition

# to get a boolean Series that indicates which rows match a certain condition, we can use the comparison operators.
# for example, to get a boolean Series that indicates which rows have an age greater than 20.
age_filter = df["Age"] > 20
print(age_filter)
print()


# to filter the DataFrame and keep only the rows that match a certain condition.
age_filter = df[df["Age"] > 20]
print(age_filter)
print()
city_filter = df[df["City"] == "Sétif"]
print(city_filter)
print()
city_filter2 = df[df["City"] == "New York"]
print(city_filter2)  # that return an empty DataFrame because there is no student from New York in the DataFrame.
print()



# the logical operators can be used to combine multiple conditions.
# for example, to filter rows have an age lower than 20 and are from Sétif.
age_city_filter = df[(df["Age"] < 20) & (df["City"] == "Sétif")]
print(age_city_filter)  
print()
