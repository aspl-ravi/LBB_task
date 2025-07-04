import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("LASTFM_API_KEY")

def get_song_by_mood(mood):
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={mood}&api_key={API_KEY}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tracks = data.get("tracks", {}).get("track", [])
        if tracks:
            return {
                "title": tracks[0]["name"],
                "artist": tracks[0]["artist"]["name"],
                "url": tracks[0]["url"]
            }
    return {"message": "No song found for this mood"}
