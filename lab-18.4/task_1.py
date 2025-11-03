import requests
import json

def get_weather(city_name):
    """
    Fetch and display weather information for a given city.
    
    Args:
        city_name (str): Name of the city to get weather information for
    """
    if not city_name.strip():
        print("Error: City name cannot be empty!")
        return

    api_key = '0ccf020f12840b0b776fe94c31d5c407'  # Replace with your actual API key
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes
        weather_data = response.json()
        
        # Format and display weather information
        print(f"\nWeather in {city_name.title()}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Feels like: {weather_data['main']['feels_like']}°C")
        print(f"Weather: {weather_data['weather'][0]['description'].title()}")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error processing weather data: {e}")

# Example usage:
if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    get_weather(city)