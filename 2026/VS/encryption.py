def encrypt(text, shift): #keyword arguments (**kwargs, *args)
    """
    encrypt text by shifting each letter
    #doc string
    example:
    """
    
    result = ""
    
    for char in text:
        ascii_value = ord(char)
        
        shift_value = ascii_value - shift #5
        
        encrypted_char = chr(shift_value)
        
        result += encrypted_char #
        
    return result 

#encrypt 2

def ecrypt2(text, key):

    encrypt_text = ""

    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')  #AKSJBDBHKJdeasefsdf

            result += chr((ord(char) - base + key) % 26 + base) #AKSNLKA

        else:
            result += char #dease 

        return result



    
    


    





    for char in text:

#3