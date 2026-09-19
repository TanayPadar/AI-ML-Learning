#Melting - Converting wide data to long data (columns to rows)
#Pivoting - Converting long data to wide data (rows to columns)

import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [25, 30, 35, 40],
    "Gender": ["Male", "Female", "Male", "Female"],
    "Country": ["USA", "Canada", "USA", "Canada"],
    "Income": [50000, 60000, 70000, 80000],
    "Tax": [5000, 6000, 7000, 8000]
})
print(df)
df2 = df.copy()

#Melting the data
df_melted = df2.melt(id_vars=["Name", "Age", "Gender", "Country"], value_vars=["Income", "Tax"], var_name="Amount")
print(df_melted)
#id_vars = What Columns to keep as it is
#value_vars = What Columns to melt / convert to rows
#var_name = What to call the new column

#When melting - its not neccessary to reduce columns by size. but increase row instead. 
#coincidence like this example

#Pivoting - Converting long data to wide data (rows to columns)
df_pivoted = df_melted.pivot(index="Name", columns="Amount", values="value")
print(df_pivoted)
#index = What to keep as it is
#columns = What to convert to columns
#values = What to keep as it is
