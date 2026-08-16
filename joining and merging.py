import pandas as pd 

# Same key
pd.merge(df1, df2, on="id")

# Different keys
pd.merge(
    df1,
    df2,
    left_on="student_id",
    right_on="id"
)

# INNER
pd.merge(df1, df2, on="id", how="inner")

# LEFT
pd.merge(df1, df2, on="id", how="left")

# RIGHT
pd.merge(df1, df2, on="id", how="right")

# OUTER
pd.merge(df1, df2, on="id", how="outer")

# Multiple keys
pd.merge(df1, df2, on=["id", "year"])

# Index
pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True
)

# Join
df1.join(df2)

# Stack rows
pd.concat([df1, df2])

# Put columns side-by-side
pd.concat([df1, df2], axis=1)