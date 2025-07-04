import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
# API_KEY = 'f4256ef53851a49d77f44f118a59b484'
print("OpenWeather API Key:", API_KEY)

def get_weather_by_city(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "main": data["weather"][0]["main"],  # e.g., Clear, Rain
            "description": data["weather"][0]["description"]
        }
    return None