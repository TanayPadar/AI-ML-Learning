#Actual Save/Write a cleaned data in .csv or /json file

import pandas as pd

df = pd.read_csv("Pandas_DS/raw_data.csv")
df2 = df.copy()

#Drop Dupliacte Values , Fill Empty Values , Sort the data , etc.
df2 = df2.drop_duplicates()
df2 = df2.fillna(0)
df2 = df2.sort_values(by="income", ascending=False)
print(df2.head())
#This will drop the duplicate values, fill the empty values, and sort the data by name in descending order

df2.to_csv("Pandas_DS/cleaned_data.csv", index=False)
print(df2.head())
#This will save the data to a new file called "cleaned_data.csv"

df2.to_json("Pandas_DS/cleaned_data.json", index=False)
print(df2.head())
#This will save the data to a new file called "cleaned_data.json"