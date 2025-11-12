
import os 

def get_uri():
    pass



def get_modify(sp):
    user_id=os.getenv("SPOTIPY_CLIENT_ID")
    sp.user_playlist_add_tracks(
        user=user_id,
        playlist_uri=id
        
        )
     