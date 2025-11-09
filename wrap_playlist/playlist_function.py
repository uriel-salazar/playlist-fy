from get_data.call import get_scopes,available_playlist,dict_playlist
from get_data.interact_user import search_playlist,show_songs,check

def call_playlist():
    
    get_scopes()
    sp,playlists=available_playlist()
    playlist_data=dict_playlist(sp,playlists)
    while True:
            selected=search_playlist(playlist_data)
            playlist_user,question=show_songs(selected)
            if question=="yes":
                check(playlist_user,question)
                break
            else:
                again=input("Search another playlist? : :")
                if again!="yes":
                    break
                    
    
