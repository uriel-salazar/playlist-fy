from spotify_api.list_songs import get_scopes,display_playlist

def menu_playlist():
    """ Menu specialized in playlists (delete/search/add)
    """
    while True:
        print("1. Search your playlist")
        print("2. Add songs to your playlist ")
        print("3. Delete a playlist ")
        option=int(input("Select an option :"))
        if option==1:
            get_scopes()
            playlist=display_playlist()
        elif option==2:
            pass
        elif option==3:
            pass
        else:
            pass
        
            
            
            
            
            