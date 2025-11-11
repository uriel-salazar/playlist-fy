from get_data.call import get_spotify,current_playlist,dict_playlist
from get_data.interact_user import display_songs,print_playlist

from saving.save_playlists import data_playlist
def caller_playlist():
    #loads client id and secret,converts scopes into lists
    get_spotify() 
    sp,playlists=current_playlist()
    #creates a dict in base on user's playlists 
    playlist_data=dict_playlist(sp,playlists)
    while True:
            #playlists availables 
            selected=print_playlist(playlist_data)
            playlist_user,question=display_songs(selected)
            if question=="yes":
                table_playlist=data_playlist(playlist_user)
                break
            else:
                again=input("Search another playlist? :")
                if again!="yes":
                    break
                    
    
