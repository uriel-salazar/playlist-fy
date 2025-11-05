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
        "playlist-modify-public",
        "user-top-read"
    ]
   
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=" ".join(scopes)
            
        ))
    
def display_playlist():
    """ Shows to user available playlists 

    Returns:
        dict: Playlist dictionary
    """
    sp=get_scopes() #spotify client object 
    playlists = sp.current_user_playlists()
    for index,playlist in enumerate(playlists["items"],start=1):
        print(f'-{index} {playlist["name"]}')
    return playlist
    
    