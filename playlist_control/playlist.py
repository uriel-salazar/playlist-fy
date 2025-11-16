from wrap_playlist.playlist_function import caller_playlist
from validate.verify_text import verify_number
from add_playlist.add_functions import wrap_songs
def menu_playlist():
    """ Menu specialized in playlists (delete/search/add)
    """
    while True:
        print("-- Spotify playlists --")
        print("1. Search playlist")
        print("2. Add songs to your playlist ")
        print("3. Delete a playlist ")
        option=verify_number("Select an option :")
        if option==1:
            tag=caller_playlist()
            playlist_info=True
                 
        elif option==2:
            if playlist_info:
                wrap_songs()
                    
            else:
                print("First you must enter your playlist.")
        elif option==3:
            pass
        else:
            pass
        
            
            
            
            
            