from src.genius.lib.functions import get_genius_link
import os


def find_genius_link(artist_dict: dict):
    for artist in artist_dict:
        for song in artist_dict[artist]["songs"]:
            artist_dict[artist]["songs"][song]["genius_link"] = get_genius_link(
                song=song,
                artist=artist,
                access_token=os.environ.get("GENIUS_ACCESS_TOKEN"),
            )
        return artist_dict
