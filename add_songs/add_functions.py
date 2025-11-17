from api_data.call import current_playlist
from add_songs.functions_add import available,chosen,add
from wrap_playlist.playlist_function import current_playlist

def wrap_songs(uri_playlist):
    """ Calls songs functions
    function for displaying the current playlists,function where shows available songs for playlist selected 
    and function for adding songs to a specific playlist 

    Args:
        uri_playlist (str): uri's playlist
    """
    while True:
        sp,playlist=current_playlist()
        _,_,_,song_chosen=available(sp)
        change_song,uri_song=chosen(song_chosen)
        if change_song=="yes":
            add(uri_playlist,uri_song,sp)
            break
        else:
            continue
    
            
        
        
    