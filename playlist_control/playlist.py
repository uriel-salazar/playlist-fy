from wrap_playlist.playlist_function import caller_playlist
from validate.verify_text import verify_number
from add_songs.add_functions import wrap_songs

from change_playlist.change import change_playlist
import time


def menu_playlist():
    """ Menu focused on playlists (search / add /delete /change)
    If user already chose a playlist, can select another option. 
    Otherwise, is going to ask for select a playlist.
    """
    
    # Predetermined values
    value_playlist=None
    playlist_picked=None
    
    while True:
        print("-- Your Spotify playlists   --")
        print("1. Select playlist 🎵 ")
        print("2. Add songs to your playlist ✍️ ")
        print("3. Change Playlist 🔁 ")
        print("4. Exit 🔚")
        option=verify_number("Select an option (1 - 4) :")
        
        if option==1:
            if playlist_picked==True:
                print("""⚠️ If you want change of playlist, 
                        - select option 4 (Change playlist) ⚠️ -
                      """)
            else:
                #Calls function for playlist selection  
                value_playlist,playlist_picked,playlist_n=caller_playlist()
                if value_playlist is None:
                    playlist_picked=False
                    break
                else:
                    playlist_picked=True
    
        elif option==2:
            if playlist_picked:
                #Function for adding songs : 
                wrap_songs(value_playlist,playlist_n)       
            else:
                print("First, you must enter your playlist.")
    
        elif option==3:
            if playlist_picked:
                want_change=change_playlist()
                if want_change:
                    playlist_picked=False
                    value_playlist,playlist_picked,playlist_n=caller_playlist()
                else:
                    print("Continuing with playlist selected ")
            else:
                print(" - Select a playlist first -")
        elif option==4:
            #breaks and goes to the main menu 
            print("Exiting .. ")
            time.sleep(3)
            break
        else:
            print("Please enter a valid number 🔢")
        
        
            
            
            
            
            