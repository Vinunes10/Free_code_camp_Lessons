import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather(city):

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()

    return weather_data

    # pprint(weather_data)

    # print(f"\nThis is the current weather of {weather_data["name"]}")
    # print(f"Temperature: {weather_data["main"]["temp"]}")
    # print(f"Feels like: {weather_data["main"]["feels_like"]}")
    # print(f"Description: {weather_data["weather"][0]["description"]}")

if __name__ == "__main__":

    print("\n--- Get current weather conditions ---")

    city = input("\nPlease enter a city name: ")

    weather_data = get_current_weather(city)

    print("\n")
    
    pprint(weather_data)