import requests
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
city = 'Manchester'

def get_weather(city):
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY})
    data = response.json()

    if response.status_code == 200:
        main = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = int(data['main']['temp'] - 273.15)  # Convert temperature from Kelvin to Celsius

        return {
            'main': main,
            'description': description,
            'temp': temp,
        }
    else:
        return None

weather = get_weather(city)
print(weather)
