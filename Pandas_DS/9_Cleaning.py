#This handles missing values and duplicates

import pandas as pd

#1 - Handles missing values
var1 = pd.read_csv("Pandas_DS/raw_data.csv")
mark_null = pd.isnull(var1) #makes missing value TRUE and not missing value FALSE
print(mark_null)    

print (var1.isnull().sum()) #combine funtions - calculate the number of missing values in the dataframe

#2 - Drops the missing values
print (var1.dropna()) #every row having missing info will get deleted
print (var1.dropna(axis=1)) #every column having missing info will get deleted

#3 - Fills the null values
print (var1.fillna(2)) #fills the every missing values with 2

#Ex - Replace null age values with other avg age values
age_mean = var1['age'].mean()
print (var1['age'].fillna(age_mean))

#Ex - Replace changed values in original data
change_data = var1.copy()
change_data['age'] = change_data['age'].fillna(age_mean)
print (change_data)
#So now the calculated mean age will be replaced in the original data

#4 - Forward and Backward Fill
print (var1.ffill()) #fills the missing values with the previous value (up to down)
print (var1.bfill()) #fills the missing values with the next value (down to up)

#5 - Check Duplicates values
print (var1.duplicated()) #checks for duplicates in the dataframe
print (var1.duplicated().sum()) #counts the number of duplicates in the dataframe

#6 - Drop Duplicates
print (var1.drop_duplicates()) #drops the duplicates in the dataframe
print (var1.drop_duplicates(keep='first')) #drops the duplicates in the dataframe and keeps the first occurrence
print (var1.drop_duplicates(keep='last')) #drops the duplicates in the dataframe and keeps the last occurrence
print (var1.drop_duplicates(keep=False)) #drops the duplicates in the dataframe and keeps the first occurrence

#7 - Change Datatype of Columns
print (var1.astype({'age': 'int64'})) #changes the datatype of the age column to int64
#rule - neither cell should be null

#Operations on Strings - 
print()
print (var1['name'].str.lower()) #converts the name column to lowercase
print (var1['name'].str.len()) #counts the number of characters in the name column
print (var1['name'].str.startswith('A')) #checks if the name column starts with 'A'
print (var1['name'].str.endswith('A')) #checks if the name column ends with 'A'
print (var1['name'].str.contains('A')) #checks if the name column contains 'A'
