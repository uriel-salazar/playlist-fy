from get_data.call import get_spotify,current_playlist,dict_playlist,get_uri_playlist
from get_data.interact_user import extract_dict,print_playlist,overview_logic



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
            tracks,playlist_name,playlist_user,uri_playlist=get_uri_playlist(playlist_data)   
            dict_sectlist,question=overview_logic(tracks,playlist_name,playlist_user)
            value_playlist=uri_playlist
            if question=="yes":
               break
            else:
              again=input("Search another playlist? (yes / no):")

            if again!="yes":
                   break
    return value_playlist
    
                    