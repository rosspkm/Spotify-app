import requests
import json


def get_genius_link(song, artist, access_token):
    response = requests.get(
        "https://api.genius.com/search",
        params={"q": song},
        headers={"Authorization": f"Bearer {access_token}"},
    )
    for hit in response.json()["response"]["hits"]:
        if artist.lower() in hit["result"]["primary_artist"]["name"].lower():
            return hit["result"]["url"]
