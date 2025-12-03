from api_data.call import current_playlist
def top_artist():
    sp,_,_=current_playlist()
    tier_artist=sp.current_user_top_artists(limit=30,time_range="long_term")
    for singer in tier_artist["items"]:
        print(singer["name"])