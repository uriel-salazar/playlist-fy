from api_data.call import current_playlist
def top_artist():
    """ Displays  User's top artist in a list (10)
    " Calls PKCE OAuth if it's required, if its, goes back to the menu 
    Otherwise, gets the current user'artists.
    (long term top )
    """              
    sp,_,_=current_playlist()

    if sp!=None:
        
        tier_artist=sp.current_user_top_artists(limit=10,time_range="long_term")
        print(" * Top artists * :")
        
        for num,singer in enumerate(tier_artist["items"],start=1):
            artist_10=singer["name"]
            
            print(f'- {num} {artist_10}')
    else:
        return
    
        