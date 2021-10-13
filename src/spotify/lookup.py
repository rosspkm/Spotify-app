from src.spotify.lib.functions import build_dict, get_data


def find_author(token: str, authors: any = None):
    """
    Function to get data from spotify api
    """
    if isinstance(authors, list):
        return build_dict(token, authors=authors)

    else:
        return build_dict(token, author=authors)


def find_track(token: str, tracks: list = None):
    songs = {}
    for track in tracks:
        response = get_data(
            url=f"https://api.spotify.com/v1/tracks/{track}",
            headers={"Authorization": f"Bearer {token}"},
        )

        if response["name"] not in songs:
            songs[response["name"]] = {}

        songs[response["name"]]["artists"] = ", ".join(
            [artist["name"] for artist in response["artists"]]
        )
        songs[response["name"]]["album_type"] = response["album"]["album_type"]
        songs[response["name"]]["release_date"] = response["album"]["release_date"]
        songs[response["name"]]["song_art"] = response["album"]["images"][0]["url"]
        songs[response["name"]]["duration"] = int(response["duration_ms"]) / 1000
        songs[response["name"]]["preview_url"] = response["preview_url"]

    return songs


def find_new_music(token: str):
    songs = {}
    response = get_data(
        url=f"https://api.spotify.com/v1/playlists/37i9dQZF1DX4JAvHpjipBk",
        headers={"Authorization": f"Bearer {token}"},
    )

    for i in range(0, len(response["tracks"]["items"])):
        songs[i] = {
            "name": response["tracks"]["items"][i]["track"]["name"],
            "artists": ", ".join(
                [
                    response["tracks"]["items"][i]["track"]["artists"][j]["name"]
                    for j in range(
                        0, len(response["tracks"]["items"][i]["track"]["artists"])
                    )
                ]
            ),
            "image": response["tracks"]["items"][i]["track"]["album"]["images"][0][
                "url"
            ],
            "preview_url": response["tracks"]["items"][i]["track"]["preview_url"],
        }

    return songs


def query_search(token: str, search: str, search_type: str):

    response = get_data(
        url=f"https://api.spotify.com/v1/{'tracks' if search_type == 'track' else 'artists'}/{search}",
        headers={"Authorization": f"Bearer {token}"},
    )
    if "error" not in response:
        return (
            find_author(token=token, authors=search)
            if search_type == "artist"
            else find_track(token=token, tracks=[search])
        )

    else:
        response = get_data(
            url=f'https://api.spotify.com/v1/search?q={search.lower().replace(" ", "%20")}&type={search_type}&market=US&limit=25',
            headers={"Authorization": f"Bearer {token}"},
        )
        if "error" not in response:
            return (
                find_author(
                    token=token,
                    authors=[artist["id"] for artist in response["artists"]["items"]],
                )
                if search_type == "artist"
                else find_track(
                    token=token,
                    tracks=[track["id"] for track in response["tracks"]["items"]],
                )
            )
        else:
            return {}


def add_checker(token: str, artist: str):
    response = get_data(
        url=f"https://api.spotify.com/v1/artists/{artist}",
        headers={"Authorization": f"Bearer {token}"},
    )
    if "error" not in response:
        return True
    else:
        return False
