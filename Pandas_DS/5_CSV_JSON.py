#Data Fetching using CSV and JSON

import pandas as pd

#CSV
df = pd.read_csv("Pandas_DS/data.csv")
print(df)

#JSON
df = pd.read_json("Pandas_DS/data.json")
print(df)

#Same using HTML , SQL , EXCEL too