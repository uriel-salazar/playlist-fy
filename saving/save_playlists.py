import pandas as pd

def data_playlist(playlist):
    table_playlist=pd.DataFrame.from_dict(playlist,orient="index")
    table_playlist = table_playlist.reset_index().rename(columns={'index': 'Song Name'})
    print(table_playlist)
    