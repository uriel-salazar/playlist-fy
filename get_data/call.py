import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_scopes():
    """ Loads authorization variables,creates lists with scopes to read

    Returns:
        spotipy.Spotify: Spotify Auth
    """
    load_dotenv()
    scopes=[
        "playlist-read-private",
       " playlist-read-collaborative",
        "playlist-modify-private",
        "playlist-modify-public",
    ]
   
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=" ".join(scopes)
            
        ))
    
    
def available_playlist():
    """  Displays the current user's available Spotify playlists.

    Returns:
       - sp (spotipy.Spotify): The authenticated Spotify client object.
        - playlists (dict): The dictionary of playlists returned by Spotify.
    """
    sp=get_scopes() #spotify client object 
    playlists = sp.current_user_playlists()

    for index,playlist in enumerate(playlists["items"],start=1):
        print(f'-{index} {playlist["name"]}')
                 
    return sp,playlists
            
    
    


def dict_playlist(scope,collections):
    """ Creates a dict for extracting each data from each playlist
    
    (tracks,artists,song's name,id)

    Args:
        scope (spotipy.Spotify) Get scopes 
        collections (_type_ ): Get current user playlists

    Returns:
        - playlist_data (list): (songs,music artists,id's)
    """
    playlist_data = []

    for playlist in collections["items"]:
        playlist_id = playlist["id"]
        playlist_name = playlist["name"]

        results = scope.playlist_items(playlist_id)

        tracks = [
            {
                "track_name": item["track"]["name"],
                "artist": item["track"]["artists"][0]["name"]  # first artist
            }
            for item in results["items"]
        ]

        playlist_data.append({
            "playlist_name": playlist_name,
            "id": playlist_id,
            "tracks": tracks
        })
        return playlist_data
    


    
   
    
    





    
    