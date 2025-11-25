from api_data.call import get_spotify,current_playlist,dict_playlist,get_uri_playlist
from api_data.interact_user import overview_logic



def caller_playlist():
    """ Calls functions for knowning the playlist selected 
  If the user doesn't choose any playlist is going to ask if wants to choose another one.
  Returns:
  value_playlist (str): uri's playlist 
   
  """
    #loads client id and secret,converts scopes into lists
    get_spotify() 
    sp,playlists=current_playlist()
    #creates a dict in base on user's playlists 
    playlist_data=dict_playlist(sp,playlists)
  
    while True:
            #playlists availables 
            tracks,playlist_name,playlist_user,uri_playlist,is_public=get_uri_playlist(playlist_data)   
            dict_sectlist,question=overview_logic(tracks,playlist_name,playlist_user)
            value_playlist=uri_playlist
            public=is_public
            if question=="yes":
                playlist_picked=True
            else:
                playlist_picked=False
  
            again=input("Search another playlist? (y / n):")
            if again!="y": 
              pass
            else:
              continue
            
            return value_playlist,public,playlist_picked
    
                    