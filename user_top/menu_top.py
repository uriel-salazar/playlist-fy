from user_top.artist import top_artist
from user_top.song import top_songs
import time
def select_top():
    """
    Displays menu for selecting top artists or top songs.
    
    """
    while True:
     print("- Spotify stats -")
     print("1.Top Artists (10)")
     print("2. Top Songs (10)")
     print("3. Exit ")
     choose_top=int(input("Please choose an option (1 - 3):"))
     
     if choose_top==1:
        top_artist()
        
     elif choose_top==2:
        top_songs()
        
     elif choose_top==3:
         print("Exiting...")
         time.sleep(3)
         break
     else:
        print("Please enter a valid option ")
                         
     