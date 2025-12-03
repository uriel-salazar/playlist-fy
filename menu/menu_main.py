from playlist_control.playlist  import menu_playlist
from validate.verify_text import verify_number
from user_top.artist import top_artist
def head():
    """ MAIN MENU
    """
    while True:
        print("--- PLAYLIST - FY ----")
        print("1. Search and modify songs from your playlists")
        print("2. Your top")
        option=verify_number("Select an option (1-2) :")
        if option==1:
            menu_playlist()
            
        elif option==2:
             top_artist()
        else:
            pass
            
        