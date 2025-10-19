import pandas as pd

# Create a DataFrame
data = {
    "Name" : ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age" : [25, 30, 35, 40, 45],
    "City" : ["New York", "Los Angeles", "Chicago", "Boston", "Phoenix"]
}
""" df means DataFrame → table-like structure """
df = pd.DataFrame(data)
print(df)

# Grouped by "City" and find average age
grouped = df.groupby("City")["Age"].mean().reset_index()
print("Grouped DataFrame:\n", grouped)

# Multiple Aggregation Functions
"""
Apply multiple aggregation functions on 'Age'
agg() → lets you use many functions at once (mean, max, min)
"""
agg_funcs = df.groupby("City")["Age"].agg(["mean", "max", "min"]).reset_index()
print("Aggregated DataFrame:\n", agg_funcs)

# Pivot Table
"""
Create a Pivot Table
values = what to summarize
index = rows (City)
aggfunc = how to summarize (mean)
"""
pivot_table = df.pivot_table(values="Age", index="City", aggfunc="mean").reset_index()
print("Pivot Table:\n", pivot_table)

import numpy as np

# Dropping Missing Values
"""
Make a copy so original df stays unchanged
Introduce a NaN at row index 2 in column "Age"
Show DataFrame with NaN
Drop rows that contain any NaN (returns new DataFrame)
Show DataFrame after dropping rows with NaN
"""
df_with_nan = df.copy()
df_with_nan.loc[2, "Age"] = np.nan  # Introduce a NaN
print("DataFrame with NaN:\n", df_with_nan)
df_dropped = df_with_nan.dropna() # Drop rows with NaN
print("DataFrame after dropping NaN:\n", df_dropped)

# Fillna() 
"""
Fillna() - Filling missing values
"""
df_filled = df_with_nan.fillna({"Age": df_with_nan["Age"].mean()}) # Fill NaN with mean age
print("DataFrame after filling NaN:\n", df_filled)
print("Original DataFrame remains unchanged:\n", df)

