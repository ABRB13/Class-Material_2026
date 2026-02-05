from encryption import *

from decryption import *

def main():

    message = "hello world"

    shift = 5

    encrypted= encrypt2(message, shift)

    print(encrypted)

    decrypted = decrypt2(encrypted, shift)

    print(decrypted)

if __name__ == "__main__":
    main()


#commits

#pull requests
#push requests 

