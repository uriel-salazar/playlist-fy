from get_data.call import get_spotify,current_playlist,dict_playlist
from get_data.interact_user import extract_dict,print_playlist,overview_logic,overview_show,

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
            tracks,playlist_name,playlist_user,name_song,name_artist,uri_spotify=extract_dict(selected)
            dict_playlist,question=overview_logic(tracks,playlist_name,playlist_user)
            overview_show(start,track_name,artist_name,tracks)
            
     #       if question=="yes":
     #           table_playlist=data_playlist(playlist_user)
     #           break
      ##      else:
       #         again=input("Search another playlist? :")
       #         if again!="yes":
       #             break
                    
    
