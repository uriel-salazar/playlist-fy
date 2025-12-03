from user_top.artist import top_artist
from user_top.song import top_songs
def select_top():
    while True:
     choose_top=int(input("Please choose an option"))
     print("1.Top Artists (10)")
     print("2. Top Songs (10)")
     if choose_top==1:
        top_artist()
     elif choose_top==2:
        top_songs()
                         
     