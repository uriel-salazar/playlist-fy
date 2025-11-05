from search_playlist import playlist


def head():
    while True:
        print("--- PLAYLIST - FY ----")
        print("1. Search and modify songs from your playlists")
        print("2. Top Artists")
        option=input("Select an option (1-2)")
        if option==1:
            playlist()
            
        elif option==2:
            pass
        else:
            pass
            
        