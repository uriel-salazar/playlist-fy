
from validate.verify_text import get_letters

def add(uri_track,playlist_track):
    print(uri_track)
    print(playlist_track)
    pass
    



def available(sp):
    """ Gets available songs from search 
    Creates a dict from the available songs (name of the song,artist and uri)

    Args:
        sp (spotipy): SpotifyOAuth 

    Returns:
        results(spotipy): Raw dictionary of available tracks 
    """
    search=get_letters("What song do you want to search?:")
    results = sp.search(q=search, type="track", limit=5)

    items=results["tracks"]["items"]
    track_list=[]
    #loops for each song founded 
    for index,track in enumerate(items,start=1):
        print(f' {index} {track["name"]}  Artist : {track["artists"][0]["name"]}')
        track_list.append({
            "name":track["name"],
            "artist":track["artists"][0]["name"],
            "uri":track["uri"]
        })
    song_chosen=select_song(track_list)

        
    return index,track,track_list,song_chosen


def select_song(i):
    """ Prints the available songs and validation input 

    Args:
       indx :(int): Index songs 
        song (_type_): Founded songs 
        i (_type_): _description_

    Returns:
        _type_: _description_
    """
    while True:
        
        select=input("Please select a song (1-5) : ")

        if select.lower() == "exit":
            print("Exiting of song selection...")
            return  

        if not select.isdigit():
            print(" Please enter a valid number.")
            continue 

        select= int(select)
        
        if 1 <= select <= len(i): 
            break
        else:
        #If the output equal less or beyond the available option,applies this verification
            print(" Number out of range. Please Try again.")
        
    song_chosen=i[select-1]
    return song_chosen
    
        
    
def chosen(song):
    """ Ask to user if want to use that song 

    Args:
        song (dict): song selected by user 

    Returns:
     change_song (str): ("yes or no answer ")
     uri_song (str): Song's uri 
    """
    uri_song=song["uri"]
    print(f" You chose {song['name']} by  {song['artist']}")
    change_song=input(" Add this song ? (yes/no) :")
    return change_song,uri_song
    
       
        
        
    
        


    
    
