from spotify_api.list_songs import get_scopes

def menu_playlist():
    while True:
        print("1. Search your playlist")
        print("2. Add songs to your playlist ")
        print("3. Delete a playlist ")
        option=input("Select an option :")
        if option==1:
            get_scopes()
        elif option==2:
            pass
        elif option==3:
            pass
        else:
            pass
        
            
            
            
            
            