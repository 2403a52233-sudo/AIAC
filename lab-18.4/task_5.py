import requests
import json
import os

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
        if response.status_code == 404:
            print("Error: City not found. Please enter a valid city.")
            return
        response.raise_for_status()
        data = response.json()

        city = data['name']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description'].capitalize()

        # Display formatted output
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description}")

        # Prepare data to store
        weather_entry = {
            "city": city,
            "temp": temperature,
            "humidity": humidity,
            "weather": description
        }

        # Load existing data if file exists
        filename = "results.json"
        if os.path.exists(filename):
            with open(filename, "r") as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    existing_data = []
        else:
            existing_data = []

        # Append new entry and save
        existing_data.append(weather_entry)
        with open(filename, "w") as file:
            json.dump(existing_data, file, indent=4)

    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# Example usage:
city = input("Enter city name: ")
get_weather(city)