#Get Cities where aqi is greater than 100

import pandas as pd
df= pd.read_csv("Pandas_DS/globalAirQuality.csv")
df_filtered = df[(df["aqi"] > 100) & (df["temperature"] > 20)]
print(df_filtered)

#After Filterning - Pandas preserve the data's original Label but the index changes

#Option 2 - using .query
qy_filtered = df.query("aqi > 100 & temperature > 20")
print(qy_filtered)