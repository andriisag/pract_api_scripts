import requests
import json
from bs4 import BeautifulSoup
api_key = "AIzaSyBiZxMhbhk4EoS6aLB0krAiT6eNoTenWVs"
book_name = input("Book name: ")
# author = input("Author: ")
url = f"https://www.googleapis.com/books/v1/volumes?q={book_name}&key={api_key}"
response = requests.get(url)
data = json.loads(response.text)
print("Name: "  + str(data['items'][0]['volumeInfo']['title']) + "\n", "Author: " + str(data['items'][0]['volumeInfo']['authors'][0]))
url_parse = data['items'][0]['volumeInfo']['infoLink']
response_parse = requests.get(url_parse)
soup = BeautifulSoup(response_parse.text, 'lxml')
quotes = soup.find('div', class_='h3YV2d')
print("Review: " + quotes.text)
print("Link: " + url_parse)

