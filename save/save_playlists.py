import pandas as pd
import os 

def data_playlist(playlist):
    table_playlist=pd.DataFrame.from_dict(playlist,orient="index")
    table_playlist = table_playlist.reset_index().rename(columns={'index': 'Song Name'})
    print(table_playlist)
    file_playlist="user_playlist.csv"
    if not os.path.exists(file_playlist):
        table_playlist.to_csv(file_playlist,index=False,header=True)
    else:
         table_playlist.to_csv(file_playlist,mode="a",index=False,header=True)
    return table_playlist

    