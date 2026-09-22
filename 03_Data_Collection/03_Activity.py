#Scrapping the Quote 

import requests
from bs4 import BeautifulSoup

page_count = 1

while True:
    url = f"https://quotes.toscrape.com/page/{page_count}/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')
    
    print(quotes)

    break
