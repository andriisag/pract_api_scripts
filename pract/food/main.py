import requests
import json
import pandas as pd
api_key = "pb6FJ2RXZ6Ai6N9mXxdmwnnXvk3Q9f57GnncIXGgo_YSjHeT2XM78u_aQJhzOzD1VJEnGcyoVEsClHapclA-wjtAbTN01ITXQt8_IZ6CharSWMIJxuODqFrqXuoOZHYx"
headers = {'Authorization': 'Bearer {}'.format(api_key)}
url = 'https://api.yelp.com/v3/businesses/search'
city = input("Input city: ")
region = input("Input region: ")
params = {'term': 'chocolate', 
          'location': f'{city},f{region}',
          'limit': 50}
response = requests.get(url, headers=headers, params=params, timeout=5)
data_dict = response.json()
for i in range(len(data_dict['businesses'])):
 info = pd.DataFrame({
    "location": data_dict['businesses'][i]["location"]["display_address"]
 })
 print("Name: " + data_dict['businesses'][i]["name"])
 print(info)
 print("           ")

   