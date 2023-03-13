import requests
import json
api_key = "6af23f00c5ec30d161665c4e86226f1e"
city = input("Input city: ")
url = "https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=metric" % (city, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data['weather'][0]['main'])