#API - Application Programming Interface 
#Fetching Data using 'Requests' Python Library

import requests
import pandas as pd

URL = "https://stephen-king-api.onrender.com/api/books"
response = requests.get(URL)                                   #.get() to fetch data from URL

fetched = (response.json())                   #print fetched data in json


#Using Pandas to filter the fetched data
df = pd.json_normalize(fetched["data"])      #.json_normalize() to convert json data to pandas dataframe
df = df[['id', 'Title', 'Year']]             #column names from the fetched data
print (df)
