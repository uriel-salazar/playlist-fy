from api_data.call import current_playlist,dict_playlist,get_uri_playlist
from api_data.interact_user import overview_logic

def ask_erase():
    go_delete=input("What playlist do you want to un")
    

def eliminate():
     sp,playlists,user_name=current_playlist()
     playlist_data=dict_playlist(sp,playlists)
     tracks,playlist_name,playlist_user,uri_playlist,name_owner=get_uri_playlist(playlist_data)   
     dict_sectlist,question=overview_logic(tracks,playlist_name,playlist_user)
     ask_unfollow=input(f"Eliminate {playlist_name} from your library? ")