
from validate.verify_text import valid_words
def add(playlist_uri,uri_track,sp):
    """ Adds new song to playlist 

    Args:
        - playlist_uri (str): Uri' playlist (Identifier for playlist)
        - uri_track (list): List of uri's songs (Identifier)
        - sp (spotipy): Spotify object 
    """
    sp.playlist_add_items(playlist_uri, uri_track)
    print("Song added!!")
    


def available_songs(sp):
    """ Gets available songs from search 
    Creates a dict from the available songs (name of the song,artist and uri)

    Args:
        sp (spotipy): SpotifyOAuth 

    Returns:
        - results (spotipy): Raw dictionary of available tracks 
        - track (dict): Songs dictionary
        - track_list (list) List of song info (name /artist / uri) 
        - song_chosen(): Song chosen by user
    """
    search=input("What song do you want to search?:")
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
        i (_type_): _description_

    Returns:
        song_chosen (_type_ ): _description_
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
    
        
    
def chosen_song(song_data):
    """ It asks to the user if they want to add the chosen song.

    Args:
        song_data (dict): song selected by index 

    Returns:
     change_song (str): ("yes or no answer ")
     uri_song (str): Song's uri (identifier for songs)
    """
    uri_song=(song_data["uri"])
    uri_song=[uri_song]
    print(f" You chose - {song_data['name']} -  by  {song_data['artist']}")
    change_song=input(" Add song ? (y/n) :")
    return change_song,uri_song


        
def go_back():
    """ Question to exit 

    Returns:
        stop (str): ( answer valid between y and n )
    """
    stop=valid_words(" Exit ? (y / n) : ",["y","n"])
    return stop
    
            
        
        
            
        
        
    


        
    
       
        
        
    
        


    
    
