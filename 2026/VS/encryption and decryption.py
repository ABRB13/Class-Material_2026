
#

#simple logic 

msg = abc 

encrypt= -1

hidden_msg = zab

decrypt = +1

msg = abc


#ascii characters 

msg = he

#ogic encrypt:

ord('h') #104 - 5 (shift_key)
ord('e') #101 - 5

99
96

chr(99) #c
chr(96) #'`'

hidden_message = c`

#decrypt logic:

msg = c`

ord('c') #99
ord('`') #96

shift_key(+5)

104
101

chr(104)
chr(101)



def encrypt(text, shift):
    """
    encrypt text by shifting each letter
    
    example:
    """
    
    result = ""
    
    for char in text:
        ascii_value = ord(char)
        
        shift_value = ascii_value - shift #5
        
        encrypted_char = chr(shift_value)
        
        result += encrypted_char #
        
    return result 
    



def decrypt(text, shift):
    
    result = ""
    
    for char in text:
            
            ascii_value = ord(char)

            shift_value = ascii_value + shift #5 #algorithm 

            decrypted_char = chr(shift_value)

            result += decrypted_char

    return result



def main():

    message = "hello world"

    shift = 5

    encrypted= encrypt(message, shift)

    print(encrypted)

    decrypted = decrypt(encrypted, shift)

    print(decrypted)

if __name__ == "__main__":
    main()


