from api_data.call import current_playlist
def top_artist():
    """ Displays  User's top artist in a list (10)
    (medium term top )
    """               
    sp,_,_=current_playlist()
    tier_artist=sp.current_user_top_artists(limit=10,time_range="medium_term")
    print("Your Top artists :")
    for num,singer in enumerate(tier_artist["items"],start=1):
        artist_10=singer["name"]
        print(f'- {num} {artist_10}')
        