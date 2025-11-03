import requests
import json

def get_weather(city_name):
    api_key = '0ccf020f12840b0b776fe94c31d5c407'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        weather_data = response.json()
        print(json.dumps(weather_data, indent=4))
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage:
city = input("Enter city name: ")
get_weather(city)