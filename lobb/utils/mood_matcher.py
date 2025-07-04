def is_mood_matching_weather(mood, weather_main):
    mood_weather_map = {
        "happy": ["Clear", "Clouds"],
        "sad": ["Rain", "Drizzle"],
        "angry": ["Thunderstorm"],
        "relaxed": ["Clear", "Mist"],
        "gloomy": ["Rain", "Fog"],
        "energetic": ["Clear", "Windy"]
    }
    return weather_main in mood_weather_map.get(mood.lower(), [])
