
def add(playlist_uri,uri_track,sp):
    """ Adds new song to playlist 

    Args:
        playlist_uri (str): _description_
        uri_track (list): List of uri's songs 
        sp (spotipy): _description_
    """
    sp.playlist_add_items(playlist_uri, uri_track)
    print("Song added!!")
    


def available(sp):
    """ Gets available songs from search 
    Creates a dict from the available songs (name of the song,artist and uri)

    Args:
        sp (spotipy): SpotifyOAuth 

    Returns:
        results(spotipy): Raw dictionary of available tracks 
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
    
        
    
def chosen(song):
    """ Ask to user if want to use that song 

    Args:
        song (dict): song selected by user 

    Returns:
     change_song (str): ("yes or no answer ")
     uri_song (str): Song's uri 
    """
    uri_song=(song["uri"])
    uri_song=[uri_song]
    print(f" You chose - {song['name']} -  by  {song['artist']}")
    change_song=input(" Add song ? (yes/no) :")
    return change_song,uri_song


def handle_error(general):
     if general==True:
         print("You can't add songs to this playlist :(")
         public=True
     else:
        public=False
     return public


def go_back():
    while True:
        no_stay=input("for exit, press 'out' ")
        if no_stay=="out":
            break
        else:
            pass
        
        



        
    
       
        
        
    
        


    
    
