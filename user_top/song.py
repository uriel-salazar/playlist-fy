from api_data.call import current_playlist

def top_songs():
    sp,_,_=current_playlist()
    tier_song=sp.current_user_top_tracks(limit=10,offset=0,time_range="long_term")
    print(tier_song)
                    