from wrap_playlist.playlist_function import caller_playlist
def select_playlist():
    value_playlist,public,playlist_info=caller_playlist()
    playlist_info=True
    return value_playlist,public,playlist_info
    