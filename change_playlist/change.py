from validate.verify_text import valid
def change_playlist():
    while True:
        answer=valid("Do you want to change of playlist?? (y / n )",["y",])
        if answer=="y":
           return True
        elif answer=="n":
            return False
        else:
            print("Please, select a valid option ")
        
    
    
    
    