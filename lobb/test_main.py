from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_recommend_song_valid_mood(monkeypatch):
    def mock_get(url, *args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return {
                    "tracks": {
                        "track": [{
                            "name": "Mock Song",
                            "artist": {"name": "Mock Artist"},
                            "url": "https://mockurl.com"
                        }]
                    }
                }
        return MockResponse()

    # Patch requests.get with our mock
    monkeypatch.setattr("requests.get", mock_get)

    response = client.get("/music/recommend?mood=happy")
    assert response.status_code == 200
    json_data = response.json()
    assert json_data["mood"] == "happy"
    assert "recommended_song" in json_data
    song = json_data["recommended_song"]
    assert song["title"] == "Mock Song"
    assert song["artist"] == "Mock Artist"
    assert song["url"] == "https://mockurl.com"

def test_recommend_song_no_api_key(monkeypatch):
    # Temporarily remove API key
    monkeypatch.setattr("main", "LASTFM_API_KEY", None)
    response = client.get("/music/recommend?mood=happy")
    assert response.status_code == 200
    assert response.json() == {"error": "Missing Last.fm API key"}

def test_recommend_song_no_tracks(monkeypatch):
    def mock_get_no_tracks(url, *args, **kwargs):
        class MockResponse:
            status_code = 200
            def json(self):
                return {"tracks": {"track": []}}
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get_no_tracks)

    response = client.get("/music/recommend?mood=unknownmood")
    assert response.status_code == 200
    json_data = response.json()
    assert "recommended_song" in json_data
    assert "message" in json_data["recommended_song"]
    assert json_data["recommended_song"]["message"] == "No song found for this mood or fallback."
