#Methods to EDA data and sort using Dataframe

import pandas as pd

df = pd.read_csv("Pandas_DS/data.csv")

#1. head() - to print first 5 rows
print(df.head())

#2. tail() - to print last 5 rows by default but can enter num you want
print(df.tail(2))

#3. sample() - to print random rows
print(df.sample(2))

#4. describe() - to print summary of the dataframe
print(df.describe())

#5. info() - to print information about the dataframe
print(df.info())

#6. columns - to print columns names
print(df.columns)

#7. shape - to print shape of the dataframe
print(df.shape)

 