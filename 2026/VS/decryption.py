def decrypt1(text, shift):
    
    result = ""
    
    for char in text:
            
            ascii_value = ord(char)

            shift_value = ascii_value + shift #5 #algorithm 

            decrypted_char = chr(shift_value)

            result += decrypted_char

    return result

#decrpt 2

def decrypt2(text, key):

    encrypt_text = ""

    for char in text:
        if char.isalpha():

                base = ord('A') if char.isupper() else ord('a')  #AKSJBDBHKJdeasefsdf

                result += chr((ord(char) - base - key) % 26 + base) #AKSNLKA

        else:
                result += char #dease 

        return result
    

    