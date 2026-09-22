#We don't majorly scrap from the website. Each website has a page source in HTML,CSS, JS which is sent from servers. 
#We basically scrap that code

#Beautiful Soup (bs4) is a library that helps to parse the HTML code and extract the data we need.
#We need to install the library using pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = "https://stephen-king-api.onrender.com/api/books"
response = requests.get(url)        #fetched the response 
soup = BeautifulSoup(response.text, 'html.parser') #parsed the response to HTML code
print(soup.prettify()) #made it pretty    

h1 = soup.find('h1')
print(h1)


