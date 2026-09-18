import pandas as pd

df = pd.read_csv("Pandas_DS/globalAirQuality.csv")

#load and get summary  
print(df.head(2))
print(df.describe())

#select particular column 
print(df[["city", "aqi"]])

#select particular row - 'loc' for label location and 'iloc' for index location
print(df.loc[0:2]) #starting idx : ending idx
print(df.iloc[0])

#select row + column 
print(df.loc[0, ["aqi"]]) #row idx , column name

#select cell using at
print (df.at[0, "city"])

