from validate.verify_text import get_letters,verify_number,valid

def print_playlist(data):
    """
    Ask to user their playlist to work on 

    Args:
        data (dict) : Dictionary from RAW AI response

    Returns:
    select()
    """
    limit = 5

    while True:
        
        for index, playlist in enumerate(data[:limit], start=1):
            print(f" * {index}. {playlist['playlist_name']}")

            
        more=get_letters("See more playlist ? yes /no : ").lower()

        
        if more == "yes" and len(data) > limit:
            print("\n All playlists :")
            for i, playlist in enumerate(data, start=1):
                print(f"{i}. {playlist['playlist_name']}")
                
        if len(data)< limit:
            pass
        
        choice =verify_number("Please select an opcion :")
        
        select=data[choice-1]

        if 1 <= choice <= len(data):
            return select
        else:
            print("Number out of range, try again.")


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
    name_owner=playlist["owner name"]["display_name"]
    
    for i in tracks:
        name_song=i["track_name"]
        name_artist=i["artist"]
        
        ###
        playlist_user[name_song]={
        "Uri playlist":uri_playlist,
        "Artist":name_artist,
        "owner":name_owner
            }
    return tracks,playlist_name,playlist_user,uri_playlist,name_owner


def overview_show(artist_n,song_n):
    """ Prints only 5 songs from the playlist 
    - connected to overview_logic function -

    Args:
        artist_n (str): Name of the artist
        song_n (str): Name of the song 
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
        
        more = valid("Show more songs? (y/n): ",["y","n"])
        if more != "y":
            break

    question = valid("Are you going to use this playlist? (y/n):",["y","n"])
    if question == "y":
        return dict_setlist, question
    else:
        return dict_setlist, None,
    

