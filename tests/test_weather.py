import unittest
from unittest.mock import patch
import weather  # assume our weather function is in weather.py

class TestGetWeather(unittest.TestCase):
    @patch('requests.get')
    def test_get_weather(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'weather': [{'main': 'Cloudy', 'description': 'cloudy with a chance of meatballs'}],
            'main': {'temp': 273.15 + 22},  # 22 degrees Celsius
        }

        weather_data = weather.get_weather('London')

        self.assertEqual(weather_data['main'], 'Cloudy')
        self.assertEqual(weather_data['description'], 'cloudy with a chance of meatballs')
        self.assertEqual(weather_data['temp'], 22)

if __name__ == '__main__':
    unittest.main()
