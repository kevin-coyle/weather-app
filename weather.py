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
        # concert the temp to fahrenheit
        tempFarenheit = int((temp * 9/5) + 32)

        # Get current time
        time = datetime.datetime.now().strftime('%H:%M:%S')

        print(f'Weather in {city}:')
        print(f'{main} - {description}')
        print(f'Temperature: {temp}°C/{tempFarenheit}°F')
        print(f'Current time: {time}')
    else:
        print(f'Error {response.status_code}: Unable to get the weather forecast.')
get_weather(city)
