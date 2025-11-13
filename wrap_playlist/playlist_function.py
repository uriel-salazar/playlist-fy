from get_data.call import get_spotify,current_playlist,dict_playlist
from get_data.interact_user import extract_dict,print_playlist,overview_logic,overview_show


def caller_playlist():
    """ Calls functions for knowning the playlist selected 
  If the user doesn't choose any playlist is going to ask if wants to choose another one. 
  """
    #loads client id and secret,converts scopes into lists
    get_spotify() 
    sp,playlists=current_playlist()
    #creates a dict in base on user's playlists 
    playlist_data=dict_playlist(sp,playlists)
    while True:
            #playlists availables 
            selected=print_playlist(playlist_data)
            tracks,playlist_name,playlist_user,name_song,name_artist,uri_spotify,tag=extract_dict(selected)
            dict_sectlist,question=overview_logic(tracks,playlist_name,playlist_user)
            overview_show(name_artist,name_song)
            
            if question=="yes":
               dict_playlist(sp,playlists)
               break
            else:
              again=input("Search another playlist? (yes / no):")
            if again!="yes":
                   break
                    