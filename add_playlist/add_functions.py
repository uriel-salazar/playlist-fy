from get_data.call import current_playlist
from add_playlist.functions_add import available,chosen

def wrap_songs():
    sp,playlists=current_playlist()
    while True:
        index,track,track_list,song_chosen=available(sp)
        change_song,uri_song=chosen(song_chosen)
        if change_song=="yes":
            pass
            break
        else:
            continue
    
            
        
        
    