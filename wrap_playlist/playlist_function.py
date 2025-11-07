from get_data.call import get_scopes,available_playlist,dict_playlist
from get_data.interact_user import search_playlist,show_songs

def call_playlist():
    get_scopes()
    sp,playlists=available_playlist()
    playlist_data=dict_playlist(sp,playlists)
    selected=search_playlist(playlist_data)
    show_songs(selected)

