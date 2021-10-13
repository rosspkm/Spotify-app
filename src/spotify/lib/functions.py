import json
import requests


def get_data(url, headers):
    """Function to return data from spotify request"""
    res = requests.get(url=url, headers=headers)

    return res.json()


def build_dict(
    token: str,
    author: str = None,
    authors: list = None,
):
    return_dict = {}
    if author:
        artist_data = get_data(
            url=f"https://api.spotify.com/v1/artists/{authors}",
            headers={"Authorization": f"Bearer {token}"},
        )

        if artist_data["name"] not in return_dict:
            return_dict[artist_data["name"]] = {}
            return_dict[artist_data["name"]]["artist_id"] = author
            return_dict[artist_data["name"]]["songs"] = {}

        return_dict[artist_data["name"]]["artist_image"] = artist_data["images"][0][
            "url"
        ]

        song_data = get_data(
            url=f"https://api.spotify.com/v1/artists/{author}/top-tracks?market=US",
            headers={"Authorization": f"Bearer {token}"},
        )
        for i in song_data["tracks"]:
            art = i["album"]["images"][0]["url"]
            song_name = i["name"]
            song_url = i["preview_url"]
            return_dict[artist_data["name"]]["songs"][song_name] = {
                "image": art,
                "song_url": song_url,
            }

        return return_dict

    if authors:
        for author in authors:

            artist_data = get_data(
                url=f"https://api.spotify.com/v1/artists/{author}",
                headers={"Authorization": f"Bearer {token}"},
            )

            if artist_data["name"] not in return_dict:
                return_dict[artist_data["name"]] = {}
                return_dict[artist_data["name"]]["artist_id"] = author
                return_dict[artist_data["name"]]["songs"] = {}

            return_dict[artist_data["name"]]["artist_image"] = artist_data["images"][0][
                "url"
            ]

            song_data = get_data(
                url=f"https://api.spotify.com/v1/artists/{author}/top-tracks?market=US",
                headers={"Authorization": f"Bearer {token}"},
            )
            for i in song_data["tracks"]:
                art = i["album"]["images"][0]["url"]
                song_name = i["name"]
                song_url = i["preview_url"]
                return_dict[artist_data["name"]]["songs"][song_name] = {
                    "image": art,
                    "song_url": song_url,
                }
        return return_dict
