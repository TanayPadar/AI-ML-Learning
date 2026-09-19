#Group by and Aggregate data

import pandas as pd

df = pd.read_csv("Pandas_DS/raw_data.csv")
df2 = df.copy()
#This will read the data from the csv file

#Group by the data by the country
df_grouped = df2.groupby("country")["income"].mean()
print(df_grouped.head())
#This will group the data by the country and then calculate the mean of the income

df_grouped = df2.groupby("gender")["income"].min()
print(df_grouped.head())
#This will group the data by the gender and then calculate the minimum of the income

df_grouped = df2.groupby("gender")["income"].agg(["mean", "min", "max"])
print(df_grouped.head())
#This will group the data by the gender and then calculate the mean, minimum, and maximum of the income

