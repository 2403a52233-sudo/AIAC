import requests

def get_weather(city_name):
    api_key = '0ccf020f12840b0b776fe94c31d5c407'  
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage:
city = input("Enter city name: ")
get_weather(city)