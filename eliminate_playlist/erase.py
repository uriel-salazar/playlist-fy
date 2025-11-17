from api_data.call import current_playlist

def eliminate(playlist_uri):
    sp,playlist=current_playlist()
    sp.playlist_remove_all_occurrences_of_items(   
    )