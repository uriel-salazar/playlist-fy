
import os 

def get_uri():
    pass



def ask_songs(sp):
    """ Ask to user for songs to add 

    Args:
        sp (spotipy): SpotifyOAuth 

    Returns:
        results(spotipy): Raw dictionary of available tracks 
    """
    search=input("What song you want to search?:")
    results = sp.search(q=search, type="track", limit=7)
    print(results)
    return results 


    
    
