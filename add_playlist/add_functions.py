from get_data.call import current_playlist
from add_playlist.functions_add import available,chosen

def wrap_songs():
    sp,playlists=current_playlist()
    index,track,track_list,song_chosen=available(sp)
    chosen(song_chosen)