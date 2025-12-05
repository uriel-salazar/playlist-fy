from api_data.call import current_playlist,dict_playlist,get_uri_playlist
from api_data.interact_user import overview_logic
from OAuth.functions_oauth import generate_codes
def caller_playlist():
    """ Calls functions for knowning the playlist selected 
  If the user doesn't choose any playlist is going to ask if wants to choose another one.
  Returns:
  value_playlist (str): uri's playlist 
   
  """
    _,code_challenge=generate_codes()
    #loads client id and secret,converts scopes into lists

    sp,playlists,user_name=current_playlist()
    if sp is None:
      return None
    
    playlist_data=dict_playlist(sp,playlists)
    while True:
            #playlists availables 
            tracks,playlist_name,playlist_user,uri_playlist,name_owner=get_uri_playlist(playlist_data)   
            dict_sectlist,question=overview_logic(tracks,playlist_name,playlist_user)
            value_playlist=uri_playlist
            playlist_n=name_owner
            if question=="y":
                playlist_picked=True
                print(f"Playlist - {playlist_name}- selected !")
            else:
              again=input("Search another playlist? (y / n):")
              if again!="y": 
                validated=True
        
            return value_playlist,playlist_picked,playlist_n,validated  
                    