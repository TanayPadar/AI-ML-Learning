#Basic Data Visualization using hist() and plot()
#Pandas calls matplotlib internally to plot the data. so install matplotlib first.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Pandas_DS/raw_data.csv")
df2 = df.copy()
#This will read the data from the csv file

#Basic Data Visualization using hist()
df3 = df2["income"].hist()
print(df3)
#This will plot the histogram of the income column

#Basic Data Visualization using plot()
df4 = df2["income"].plot(kind="bar") #kind can be also scatter, line, etc.
print(df4)
#This will plot the bar chart of the income column

plt.show()