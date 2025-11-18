

def print_playlist(data):
    """
    Ask to user their playlist to work on 

    Args:
        data (dict) : Dictionary from RAW AI response

    Returns:
    """
    item=len(data)
    loop=5
    stop=data[:loop]
    # trying to print just 5 playlist then if the user wants more,
    #you can view the other remaining ones 
    remain=data[loop:]
    for index, playlist in enumerate(stop, start=1):
        print(f"{index}. {playlist['playlist_name']}")
    more=input(" Do you want to see  all your playlist?? (yes / no ): ")
    if more=="yes":
        for indx , playlist in enumerate(remain,start=6):
            print(f" {indx}. {playlist['playlist_name']} ")
            continue
    if more=="no":
        pass
              
    while True:
        choice = input("Select an option (or 'exit' to quit): ")

        if choice.lower() == "exit":
            print("Exiting playlist selection...")
            return  

        if not choice.isdigit():
            print(" Please enter a valid number.")
            continue 

        choice = int(choice)
        #If the output equal less or beyond the available option,applies this verification.
        if 1 <= choice <= len(data): 
            break
        else:
            print(" Number out of range. Try again.")

    selected = data[choice - 1]
    return selected


def extract_dict(playlist):
    """ Creates dict of playlist selected 

    Args:
        playlist (dict): User's playlist selected 

    Returns:
        - tracks (dict) : Playlist's songs
        - playlist_name (dict): Name of the playlist
        - playlist_user (dict): Playlist dictionary created 
        - name_song (dict): Name of the song 
        - name_artist (dict): Artist's name 
        - uri_spotify (dict): spotify uri 
    """
    tracks=playlist["tracks"]
    playlist_name=playlist["playlist_name"]
    playlist_user={}
    uri_playlist=playlist["uri"]
    
    
    for i in tracks:
        name_song=i["track_name"]
        name_artist=i["artist"]
        
        ###
        playlist_user[name_song]={
        "Uri playlist":uri_playlist,
        "Artist":name_artist,
            }
    return tracks,playlist_name,playlist_user,name_song,name_artist,uri_playlist



def overview_show(artist_n,song_n):
    """ Prints only 5 songs from the playlist 
    - connected to overview_logic function -

    Args:
        artist_n (_type_): Name of the artist
        song_n (_type_): Name of the song 
    """
    print(f'Artist: {artist_n}, Song: {song_n}')
        


def overview_logic(songs,name_playlist,dict_setlist):
    """ Prints 5 songs from the playlist selected (logic
    If user want to see more songs : user has to enter (y or n)
    If not,is going to ask to user if this is the playlist to work on

    Args:
        - songs (dict)): Playlist's songs 
        - name_playlist (str): Name of the playlist 
        - dict_setlist (dict): Dictionary with playlist selected

    Returns:
        dict_setlist :(dict) : Dictionary with playlist selected 
    """
    batch_size = 5 
    start = 0
    print(f" --- Playlist : {name_playlist}🎵 ---")
    
    while start < len(songs):
        end = start + batch_size
        for item in songs[start:end]:
            overview_show(item["track_name"],item["artist"])
             
        start += batch_size

        if start >= len(songs):
            print("No more songs.")
            break
        
        more = input("Show more songs? (y/n): ").lower()
        if more != "y":
            break
    
    question = input("Are you going to use this playlist? (yes/no):").lower()
    if question == "yes":
        print(f" You selected '{name_playlist}' as your playlist !")
        return dict_setlist, question
    else:
        return dict_setlist, None
    
        

