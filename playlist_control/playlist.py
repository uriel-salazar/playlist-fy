from wrap_playlist.playlist_function import call_playlist
def menu_playlist():
    """ Menu specialized in playlists (delete/search/add)
    """
    while True:
        print("-- Spotify playlists --")
        print("1. Search your playlist")
        print("2. Add songs to your playlist ")
        print("3. Delete a playlist ")
        option=int(input("Select an option :"))
        if option==1:
            call_playlist()
                 
        elif option==2:
            pass
        elif option==3:
            pass
        else:
            pass
        
            
            
            
            
            