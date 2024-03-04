# Programmer - Cade Smith
# Date - 2.29.2024
# Program - AI Playground

print("This will be a place for me to play with programming using Python programming using AI Technology.")

import requests

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},US&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        country = data["sys"]["country"]

        print(f"Weather in {city}, {country}: {weather_desc}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("Failed to fetch weather data. Please check the city name.")

if __name__ == "__main__":
    api_key = "API Key Here"  # Replace 'YOUR_API_KEY' with your OpenWeatherMap API key
    city = "Detroit"  # You can change this to any city in Michigan
    get_weather(api_key, city)