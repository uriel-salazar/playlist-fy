from api_data.call import current_playlist
from add_songs.functions_add import available_songs,chosen_song,add
from wrap_playlist.playlist_function import current_playlist
from add_songs.functions_add import go_back


def wrap_songs(uri_playlist,name_user):
    """ Calls songs functions
    function for displaying the current playlists,function where shows available songs for playlist selected 
    and function for adding songs to a specific playlist 

    Args:
        uri_playlist (str): Uri's playlist
        name_user(str): Name's user
    """
    while True:
        sp,_,user_name=current_playlist()
        _,_,_,song_chosen=available_songs(sp)
        change_song,uri_song=chosen_song(song_chosen)
        if change_song=="y":
            if name_user==user_name:
                add(uri_playlist,uri_song,sp)
                stop=go_back()
                if stop=="y":
                    break
            else:
                print(" - You can't modify public playlists -")
                break
        else:
            break

            
        
        
    