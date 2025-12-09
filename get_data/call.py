import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from get_data.interact_user import print_playlist,extract_dict

def get_spotify ():
    """ Loads authorization variables,creates lists with scopes to read

    Returns:
        spotipy.Spotify: Spotify Auth
    """
    load_dotenv()
    scopes=[
        "user-top-read",
        "playlist-read-private",
        "playlist-modify-private",
        "playlist-modify-public",
    ]
   
    return spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=" ".join(scopes)
            
        )
    )
    
    
def current_playlist():
    """  Gets the current user's available Spotify playlists.

    Returns:
       - sp (spotipy.Spotify): The authenticated Spotify client object.
        - playlists (dict): The dictionary of playlists returned by Spotify.
    """
    sp=get_spotify () #spotify client object 
    playlists = sp.current_user_playlists()
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
        playlist_uri = playlist["uri"]
        playlist_name = playlist["name"]
     #   name_user=playlist[""]

        results = scope.playlist_items(playlist_uri)

        tracks = [
            {
                "track_name": item["track"]["name"],
                "artist": item["track"]["artists"][0]["name"],
                "uri":item["track"]["uri"]
                
            }
            for item in results["items"] if item.get("track")
        ]

        playlist_data.append({
            "playlist_name": playlist_name,
            "uri": playlist_uri,
            "tracks": tracks
        })
    return playlist_data


def get_uri_playlist(playlist_data):
    selected=print_playlist(playlist_data)
    tracks,playlist_name,playlist_user,name_song,name_artist,uri_playlist=extract_dict(selected)
    return tracks,playlist_name,playlist_user,uri_playlist


    
    
    


    
   
    
    





    
    