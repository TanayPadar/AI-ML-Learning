#Series - One Dimensional Labeled Array 
#index = position
#labeled = named index . can give label using index[]


import pandas as pd

data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series)

#Properteries of Series
#1. Homogenous data type - all elements of same type
#2. Vectorised Operations - can apply operations to all elements at once
#3. Mutuable Values -   can changes values of series in future
#4. Immutable Index - cannot change index of series in future. if done, new series will be automatically created
