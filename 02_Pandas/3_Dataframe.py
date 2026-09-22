#DataFrame - 2D Labeled Array

import pandas as pd
import numpy as np 

#Option 1 is by creating DICTIONARY
info = {
    "Name": ["John", "Jane", "Jim", "Jill"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"],
}

df = pd.DataFrame(info)
print(df)
print(df.columns)  #for printing the columns names

#Option 2 is by list , just give columns name seperately.
df2 = pd.DataFrame([["John", 25, "New York"], ["Jane", 30, "Los Angeles"], ["Jim", 35, "Chicago"]], columns=["Name", "Age", "City"])
print(df2)

#Option 3 is by creating using Numpy too but give columns name
np_arr = np.array([[1,2,3],[4,5,6]])
df3 = pd.DataFrame(np_arr, columns=["A", "B", "C"])
print(df3)