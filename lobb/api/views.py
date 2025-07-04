from fastapi import APIRouter, Query
from .weather_service import get_weather_by_city
from .music_service import get_song_by_mood
from utils.mood_matcher import is_mood_matching_weather

router=APIRouter(prefix="/music",tags=['recommend_music'])

@router.get("/recommend")
def recommend_song(city: str = Query(...), mood: str = Query(...)):
    weather = get_weather_by_city(city)
    if weather is None:
        return {"error": "Could not fetch weather data"}

    mood_matches = is_mood_matching_weather(mood, weather["main"])
    song = get_song_by_mood(mood)

    return {
        "city": city,
        "weather": weather["description"],
        "user_mood": mood,
        "mood_matches_weather": mood_matches,
        "recommended_song": song
    }