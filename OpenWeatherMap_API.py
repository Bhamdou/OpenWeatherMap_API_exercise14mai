import requests
import json

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # to get the temperature in Celsius
    }
    response = requests.get(base_url, params=params)
    weather_data = response.json()

    return weather_data

# replace 'your_api_key' with your actual API key
# replace 'London' with the city you are interested in
weather_data = get_weather('London', 'your_api_key')

print(f"The current temperature in London is {weather_data['main']['temp']}°C.")
