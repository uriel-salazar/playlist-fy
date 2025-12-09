from validate.verify_text import valid_words
def change_playlist():
    """ Asks user to change playlist.

    Returns:
        (bool): Answer (True / False)
    """
    while True:
        answer=valid_words("Change of playlist?? (y / n ) : ",["y",])
        if answer=="y":
           return True
        elif answer=="n":
            return False
        else:
            print("Please, select a valid option ")
        
    
    
    
    