def verify_number(answer):
    """ Verify if is a a valid number
    If not, is going to ask the question again 

    Args:
        answer (int) User's input 


    Returns:
        int:   User's input validated 
    """
    while True:
        user_input = input(answer).strip()  
        try:
            num = int(user_input)
            
        except ValueError:
            print("Please enter a valid number")
            continue
        return num
    
    
def get_letters(prompt):
    """
    Forces user to enter only letters and spaces

    Args:
        prompt (str): message shown to the user

    Returns:
        str: validated text containing only letters and spaces
    """
    while True:
        text = input(prompt).strip()
        
        if all(word.isalpha() for word in text.split()):
            return text
        else:
            print("❌ Only letters allowed.Please try again.")
    
def valid(answer,accepted_words):
    """
    Accepts a word from a lisr of accepted words 
    example : ["yes / "no" ] = valid words 

    Args:
    
        answer(str): User's input 
        valid_words(str): Valid words in a list exampl : ["yes / "no]
    """
    #checks if the output's user is string 
    if isinstance(answer,str):
        accepted_words=[accepted_words]
        
    #Convertsthe valid words into lowercase 
    accepted_words=[word.lower() for word in accepted_words]
    while True:
        option=input(answer).strip().lower()
        if option in accepted_words:
            return option
        else:
            print(f" Please enter a valid word {accepted_words} ")
        

