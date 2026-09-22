#Task - Print id column last instead of first

import pandas as pd

df = pd.read_csv("Pandas_DS/raw_data.csv")
df_copy = df.copy()  # never change original data

#select columns in new order - id at the end
print(df_copy[["name", "age", "country", "gender", "income", "id"]])
