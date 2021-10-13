from src.spotify.lib.classes import Spotify_Auth
from src.spotify.lookup import find_author, find_new_music, query_search, add_checker
from src.genius.lookup import find_genius_link


auth = Spotify_Auth()


def call_apis(artists):
    try:
        return find_genius_link(find_author(token=auth.access_token, authors=artists))
    except:
        return []


def get_new():

    return find_new_music(token=auth.access_token)


def music_search(search_type: str, search: str):

    return query_search(token=auth.access_token, search=search, search_type=search_type)


def check_artist(artist: str):
    return add_checker(token=auth.access_token, artist=artist)
