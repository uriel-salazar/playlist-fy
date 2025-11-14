from pprint import pprint
import os 
from validate.verify_text import get_letters

def get_uri():
    pass



def available(sp):
    """ Gets available songs 

    Args:
        sp (spotipy): SpotifyOAuth 

    Returns:
        results(spotipy): Raw dictionary of available tracks 
    """
    search=get_letters("What song do you want to search?:")
    results = sp.search(q=search, type="track", limit=5)

    items=results["tracks"]["items"]
    track_list=[]
    for index,track in enumerate(items,start=1):
        print(f' {index}  {track["name"]}  Artist : {track["artists"][0]["name"]}')
        track_list.append({
            "name":track["name"],
            "artist":track["artists"][0]["name"],
            "uri":track["uri"]
        })
    return track_list


def select_song(list_song):
    print(list_song)

       
        
        
    
        


    
    
