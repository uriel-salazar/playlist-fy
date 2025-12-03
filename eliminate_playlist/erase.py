from api_data.call import current_playlist,dict_playlist,get_uri_playlist
from api_data.interact_user import overview_logic
from validate.verify_text import valid_words

def wipe_out():
    while True:
        sp,playlists,user_name=current_playlist()
        playlist_data=dict_playlist(sp,playlists)
        tracks,playlist_name,playlist_user,uri_playlist,_=get_uri_playlist(playlist_data)   
        _,_=overview_logic(tracks,playlist_name,playlist_user)
        ask_unfollow=valid_words(f"Eliminate {playlist_name} from your library? ( y / n )",["y","n"])
        if ask_unfollow=="y":
            sp.current_user_unfollow_playlist(uri_playlist)
            eliminate=True
            print("Playlist unfollowed ! ")
        else:
            continue
        return eliminate
         
    
         