from api_data.call import current_playlist

def top_songs():
    """
    Displays top tracks (10 songs) to the user
    
     Calls PKCE OAuth if it's required, if it is, goes back to the menu 
     Otherwise, gets the current user tracks 
    """
    sp,_,_=current_playlist()
    
    if sp!=None:   
        tier_song=sp.current_user_top_tracks(limit=10,offset=0,time_range="medium_term")
        
        song_10=tier_song
        print("* Top songs *")
        for num,song in enumerate(tier_song["items"],start=1):
            song_10=song["name"]
            
            print(f"-{num} {song_10}")
    else:
        return
    
        
        
                    