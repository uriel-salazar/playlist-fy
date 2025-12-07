from wrap_playlist.playlist_function import caller_playlist
from validate.verify_text import verify_number
from add_songs.add_functions import wrap_songs
from eliminate_playlist.erase import wipe_out
from change_playlist.change import change_playlist
import time

def menu_playlist():
    """ Menu specialized in playlists (delete/search/add)
    """
    value_playlist=None
    playlist_picked=None
    
    while True:
        print("-- Your Spotify playlists   --")
        print("1. Select playlist 🎵 ")
        print("2. Add songs to your playlist ✍️ ")
        print("3. Delete a playlist 🗑️")
        print("4. Change Playlist 🔁 ")
        print("5. Exit 🔚")
        option=verify_number("Select an option (1 - 5) :")
        
        if option==1:
            if playlist_picked==True:
                print("""⚠️ If you want change of playlist, 
                        - select option 4 (Change playlist) ⚠️ -
                      """)
            else:
                #calls function for playlist selection  
                value_playlist,playlist_picked,playlist_n=caller_playlist()
                if value_playlist is None:
                    break
                else:
                    playlist_picked=True
    
        elif option==2:
            if playlist_picked:
                wrap_songs(value_playlist,playlist_n) 
                   
            else:
                print("First, you must enter your playlist.")
        elif option==3:
                print("-- Delete Playlist -- ") 
                wipe_out()
        elif option==4:
             want_change=change_playlist()
             if want_change:
                 playlist_picked=False
                 value_playlist,playlist_picked,playlist_n=caller_playlist()
             else:
                 print("Continuing with playlist selected ")
        elif option==5:
            print("Exiting .. ")
            time.sleep(3)
            break
        else:
            print("Please enter a valid number")
        
        
            
            
            
            
            