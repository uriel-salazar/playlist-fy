from user_top.artist import top_artist
from user_top.song import top_songs
def select_top():
    """
    Displays tier lists of artists and songs from the user
    
    """
    while True:
     print("- Spotify stats -")
     print("1.Top Artists (10)")
     print("2. Top Songs (10)")
     choose_top=int(input("Please choose an option (1 - 2 ):"))
     if choose_top==1:
        top_artist()
     elif choose_top==2:
        top_songs()
                         
     