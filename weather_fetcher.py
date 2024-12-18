import time
import request

"""
Weather Fetcher and Updater
The comprehensive description for this project is available @Readme.md
"""

# Prompt user to input multiple locations
print("Welcome to the Weather Fetcher!")
print("Enter the names of cities you want to monitor, separated by commas.")
locations = input("Locations: ").split(",")
locations = [location.strip() for location in locations]  # Clean input and prepare for implementation 

print("\nFetching weather details for:", locations)

#Now let's begin 
API_KEY = "dba9af993c1ada8d045c99e6492363ba"  # This is my API key i generated from openweathermap portal after signing up 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Metric system for Celsius
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
    else:
        return {"error": f"Could not fetch weather for {city}"}

# Fetch weather for all locations    
while True:
    for city in locations:
        weather = get_weather(city)
        if "error" in weather:
            print(weather["error"])
        else:
            print(f"\nWeather in {city}:")
            print(f"  Temperature: {weather['temperature']}°C")
            print(f"  Feels Like: {weather['feels_like']}°C")
            print(f"  Description: {weather['description']}")
            print(f"  Humidity: {weather['humidity']}%")
            print(f"  Wind Speed: {weather['wind_speed']} m/s")
     print("\nUpdating weather data in 120 seconds...\n")
     time.sleep(120) #Based on how you decide to refresh 

