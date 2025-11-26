from api_data.call import current_playlist
from add_songs.functions_add import available,chosen,add,handle_error
from wrap_playlist.playlist_function import current_playlist
from add_songs.functions_add import go_back


def wrap_songs(uri_playlist,name_user):
    """ Calls songs functions
    function for displaying the current playlists,function where shows available songs for playlist selected 
    and function for adding songs to a specific playlist 

    Args:
        uri_playlist (str): uri's playlist
    """
    while True:
        sp,playlist,user_name=current_playlist()
        _,_,_,song_chosen=available(sp)
        change_song,uri_song=chosen(song_chosen)
        if change_song=="yes":
            if name_user==user_name:
                add(uri_playlist,uri_song,sp)
            else:
                print(" You can't modify a playlist from another user :(")
                break
        else:
            go_back()
    
            
        
        
    