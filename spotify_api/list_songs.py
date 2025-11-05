import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_scopes():
    load_dotenv()
    scopes=[
        "playlist-read-private",
       " playlist-read-collaborative",
        "playlist-modify-private",
        "playlist-modify-public"
    ]
   
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=" ".join(scopes)
        )
    )
    

        
