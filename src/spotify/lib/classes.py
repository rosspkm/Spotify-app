import os
import requests


class Spotify_Auth:
    """Class to get authorizations from spotify"""

    def __init__(self):
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.auth_url = "https://accounts.spotify.com/api/token"
        self.headers = {}
        self.data = {}
        self.access_token = self.create_access_token()

    def create_access_token(self):
        """Function to create access token for spotify requests"""
        req = requests.post(
            self.auth_url,
            {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
            },
        )
        return req.json()["access_token"]
