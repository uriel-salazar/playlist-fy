from get_data.call import get_scopes,available_playlist,dict_playlist

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
            sp,playlists=available_playlist()
            dict_playlist(sp,playlists)
        elif option==2:
            pass
        elif option==3:
            pass
        else:
            pass
        
            
            
            
            
            