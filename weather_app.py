-- Steps to Use:
-- Get a free API key from OpenWeatherMap.
-- Replace "your_api_key_here" in the code with your actual API key.
-- Run the script using:
-- sh
-- Copy
-- Edit
-- python weather_app.py
-- Enter a city name, and the script will fetch and display real-time weather.

import requests

def get_weather(city):
    API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Change to "imperial" for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\n🌍 Weather in {city.capitalize()}:")
        print(f"🌦 Condition: {weather.capitalize()}")
        print(f"🌡 Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬 Wind Speed: {wind_speed} m/s")

    else:
        print("⚠ Error: Could not fetch weather data. Check your city name or API key.")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
