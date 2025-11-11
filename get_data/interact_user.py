
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
    

def display_songs(playlist):
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
        ###
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
    
    question = input("Are you going to use this playlist? (yes/no):").lower()
    if question == "yes":
        return playlist_user, question
    else:
        return playlist_user, None
    
        
    
   
