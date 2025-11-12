
import os 

def print_playlist(data):
    """
    Ask to user their playlist to work on 

    Args:
        data (dict) : Dictionary from RAW AI response

    Returns:
    """
    for index, playlist in enumerate(data, start=1):
        print(f"{index}. {playlist['playlist_name']}")

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
    tracks=playlist["tracks"]
    playlist_name=playlist["playlist_name"]
    playlist_user={}
    for i in tracks:
        name_song=i["track_name"]
        name_artist=i["artist"]
        uri_spotify=i["uri"]
        
        ###
        playlist_user[name_song]={
        "Artist":name_artist,
        "Uri":uri_spotify
            }
    return playlist_user,playlist_name,tracks,


def overview_logic(playlist,songs):
    batch_size=5
    start=0
    end = start + batch_size
    for item in songs[start:end]:
        track_name = item["track_name"] 
        artist_name = item["artist"]
        uri = item["uri"]
        start += batch_size
    return start,track_name,artist_name,uri,end

def overview_show(begin,name_song,artist,songs):
    print(f'Artist: {artist}, Name: {name_song}')
    while begin < len(songs):
        if begin >= songs:
            print("No more songs.")
            break
        
    
    
    

def display_songs(playlist):
    """ Displays first 5 songs of playlist's user selected.
    Creates a playlist's dict with information such as name of the track,artist and spotify uri.
    Args:
        playlist (_type_): _description_

    Returns:
        playlist_user(dict) : User's playlist dict 
    """
    tracks = playlist["tracks"]
    playlist_name=playlist["playlist_name"]
    batch_size = 5 
    start = 0
    playlist_user={}
    print(f" --- Playlist : {playlist_name}🎵 ---")
    
    for i in tracks:
        name_song=i["track_name"]
        name_artist=i["artist"]
        uri_spotify=i["uri"]

        playlist_user[name_song]={
        "Artist":name_artist,
        "Uri":uri_spotify
            }
    
    
    while start < len(tracks):
        end = start + batch_size
        for item in tracks[start:end]:
            track_name = item["track_name"] 
            artist_name = item["artist"]
            uri = item["uri"] 

            print(f'Artist: {artist_name}, Name: {track_name}')
             
        start += batch_size

        if start >= len(tracks):
            print("No more songs.")
            break
        
        more = input("Show more songs? (y/n): ").lower()
        if more != "y":
            break
    print(playlist_user)
    question = input("Are you going to use this playlist? (yes/no):").lower()
    if question == "yes":
        print(f" You selected {playlist_name} as your playlist !")
        return playlist_user, question
    else:
        return playlist_user, None
    
        

