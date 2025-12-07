from api_data.call import current_playlist,dict_playlist,get_uri_playlist
from api_data.interact_user import overview_logic
from OAuth.functions_oauth import generate_codes

def caller_playlist():
    """
    Calls functions for knowing the playlist selected.
    If the user doesn't choose any playlist, it will ask if they want another one.

    Returns:
        value_playlist (str): playlist URI
        playlist_picked (bool)
        playlist_n (str): owner name
    """
    _, code_challenge = generate_codes()

    sp, playlists,user_name = current_playlist()
    if sp is None:
        return None,None,None

    playlist_data = dict_playlist(sp, playlists)

    while True:
        tracks, playlist_name, playlist_user, uri_playlist, name_owner = get_uri_playlist(playlist_data)
        dict_sectlist, question = overview_logic(tracks, playlist_name, playlist_user)

        value_playlist = uri_playlist
        playlist_n = name_owner

        if question == "y":
            playlist_picked = True
            print(f"Playlist - {playlist_name} - selected!")
            return value_playlist, playlist_picked, playlist_n

        again = input("Search another playlist? (y / n): ")

        if again.lower() != "y":
            # user doesn't want to search more playlists
            playlist_picked = False
            return value_playlist, playlist_picked, playlist_n
                    