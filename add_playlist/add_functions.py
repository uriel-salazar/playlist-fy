from get_data.call import current_playlist
from add_playlist.functions_add import available,chosen,add
from get_data.interact_user import extract_dict

def wrap_songs():
    sp,playlists=current_playlist()
    while True:
        index,track,track_list,song_chosen=available(sp)
        change_song,uri_song=chosen(song_chosen)
        if change_song=="yes":
            _,_,_,_,_,uri_playlist=extract_dict()
            add(uri_playlist,uri_song)
            break
        else:
            continue
    
            
        
        
    