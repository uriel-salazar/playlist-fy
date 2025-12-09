import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyPKCE
from api_data.interact_user import print_playlist,extract_dict


def get_spotify ():
    """ Loads authorization variables and creates a list with the requited scopes to read

    Returns:
        spotipy.Spotify: Spotify Auth (spotify object)
    """
    load_dotenv()
    scopes=[
        "playlist-read-private",
        "playlist-modify-private",
        "playlist-modify-public",
    ]


    auth_manager = SpotifyPKCE(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=" ".join(scopes),
        open_browser=True,
        cache_path=".cache"
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    return sp

   
   

def log_in():
    """
    Calls to Spotify Auth and handles it  if authorization is denied.
    
    If is denied, is going to return the exception explaining the error then
    at the end returns None.
    
    Raises:
        Login failed: Received error from OAuth server: Received error from auth server: access_denied
    
    If you accept the terms, prints a message with their Spotify's username 
    and returns Spotify object 
    """
    
    sp = get_spotify()
    try:
        current_user = sp.current_user()
        print(f"Logged in as: {current_user['display_name']}")
        return sp
    except Exception as e:
        print("Login failed:", e)
        return None



def current_playlist(): 
    """  Get user's playlists 
    If user cancels pkce auth, returns None.
    
    Returns:
       - sp (spotipy.Spotify): The authenticated Spotify client object.
        - playlists (dict): The dictionary of playlists returned by Spotify.
        - user_name (str): Spotify username 
    """
    sp=validate_user()
    if sp is None:
        return None,None,None
    else:
        user=sp.current_user()
        playlists = sp.current_user_playlists() 
        user_name=user["display_name"]
        return sp,playlists,user_name
      
def validate_user():
    """ 
    Handles if spotify object is None,if it is, prints a message of returnin to main menu.
    Returns:
       sp (spotipy): Spotify object
    """
   
    while True:
        sp=log_in()
        if sp is None:
            print("⚠️ Login cancelled, going back to menu ")
            return None
        return sp
    

def dict_playlist(scope,collections):
    """ Creates a dict for extracting each data from each playlist
    
    (tracks,artists,song's name,id)

    Args:
        scope (spotipy.Spotify) Get scopes 
        collections (spotipy): Get current user playlists

    Returns:
        - playlist_data (list): (songs,music artists,id's)
    """
    playlist_data = []

    for playlist in collections["items"]:
        playlist_uri = playlist["uri"]
        playlist_name = playlist["name"]
        owner=playlist["owner"]

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
            "tracks": tracks,
            "owner name":owner
            
        })
    return playlist_data


def get_uri_playlist(playlist_data):
    """
    Docstring for get_uri_playlist
    
    :param playlist_data: Description
    """
    selected=print_playlist(playlist_data)
    tracks,playlist_name,playlist_user,uri_playlist,name_owner=extract_dict(selected)
    return tracks,playlist_name,playlist_user,uri_playlist,name_owner




    
    
    


    
   
    
    





    
    