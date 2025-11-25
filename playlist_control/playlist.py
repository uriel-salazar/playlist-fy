from wrap_playlist.playlist_function import caller_playlist
from validate.verify_text import verify_number
from add_songs.add_functions import wrap_songs
from eliminate_playlist.erase import eliminate
from change_playlist.change import change_playlist

def menu_playlist():
    """ Menu specialized in playlists (delete/search/add)
    """
    public=None
    value_playlist=None
    playlist_picked=False
    
    while True:
        print("-- Spotify playlists --")
        print("1. Search playlist")
        print("2. Add songs to your playlist ")
        print("3. Delete a playlist ")
        print("4. Change of Playlist")
        option=verify_number("Select an option :")
        
        if option==1:
            value_playlist,public,playlist_picked=caller_playlist()
            playlist_picked=True
        elif option==2:
            if playlist_picked:
                wrap_songs(value_playlist,public)
                break
                   
            else:
                print("First you must enter your playlist.")
        elif option==3:
                print("-- Delete Playlist -- ") 
                eliminate()
        elif option==4:
             want_change=change_playlist()
             if want_change:
                 value_playlist,public,playlist_picked=caller_playlist()
             else:
                 print("Continuing with playlist selected ")
        else:
            pass
        
            
            
            
            
            