#Feature Engineering - Creating new data to improve current data for model

import pandas as pd

#1 - Create new data using .apply()
df = pd.read_csv("Pandas_DS/raw_data.csv")
df["tax"] = df["income"].apply(lambda x: x * 0.1)
print(df.head())
#This will create new column "tax" and apply the lambda function to the income column
#currently calculating tax as 10% of income
#can pass any function in .apply() 

#2 - Replace Current Data using .map()
gender_map = {
    "Male": 1,
    "Female": 2,
    "Unknown": 3,
}
df["gender"] = df["gender"].map(gender_map)
print(df.head())
#In gender column, Male will be replaced with 1, Female with 2, and Unknown with 3

#3 - Create new Column using .assign()
df = df.assign(total_expenses = df["income"] + df["tax"])
print(df.head())
#This will create new column "total_expenses" and add the income and tax columns
#can pass any function in .assign()

#4 - Replace specific old value with new values using .replace()
df2 = pd.read_csv("Pandas_DS/raw_data.csv")
df2 = df2.replace("Unknown", "Other")
print(df2.head())
#In gender column, Unknown will be replaced with Other

#5 - Editing new Columns using .columns
df3 = pd.read_csv("Pandas_DS/raw_data.csv")
df3.columns = ["ID", "Name", "Age", "Gender", "Country", "Income"]
print(df3.head())
#This will rename the columns to ID, Name, Age, Gender, Country, and Income

#6 - Rename Partiular Column name only
df4 = pd.read_csv("Pandas_DS/raw_data.csv")
df4.rename(columns={"Income": "Salary"}, inplace=True) #to replace column name
df4.rename(index={0: "First", 1: "Second", 2: "Third"}, inplace=True) #to replace row name
print(df4.head())
#This will rename the column name to Salary

#7 - Sort the data like sorting filter
df5 = pd.read_csv("Pandas_DS/raw_data.csv")
df5 = df5.sort_values(by="Income", ascending=False)
print(df5.head())
#This will sort the data by Income in descending order. otherwise it will be in ascending order by default. 

