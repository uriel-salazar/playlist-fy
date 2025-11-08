from get_data.call import get_scopes,available_playlist,dict_playlist
from get_data.interact_user import search_playlist,show_songs,check

def call_playlist():
    get_scopes()
    sp,playlists=available_playlist() 
    playlist_data=dict_playlist(sp,playlists)
    selected=search_playlist(playlist_data)
    playlist_user=show_songs(selected)
    if show_songs==None:
        search_another=input("Do you want to search another playlist? (yes/no)")
        if search_another=="yes":
            selected=search_playlist(playlist_data)
            playlist_user=show_songs(selected)
        else:
            return
    check(playlist_user)
