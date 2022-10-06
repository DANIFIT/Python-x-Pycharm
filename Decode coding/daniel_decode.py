# Programmer: Daniel Elombi
# Encryption
# PROGRAMMING LAB
# DUE 2021-11-28
# This program will encode or decode a piece of text using Cipher. Cipher replaces one text of the alphabet
# with letters of another alphabet

MESSAGE = "BAD"
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  # regular english alphabet
AL_BHED = "YPLTAVKREZGMSHUBXNCDIJFQOWypltavkrezgmshubxncdijfqow"  # the AI Bed language from Final Fantasy X

running = True


def encode_function(value):
    message = value
    encrypted_string = ""
    for letter_index in range(len(message)):
        match_found = False
        for alphabet_index in range(len(ALPHABET)):
            if message[letter_index] == ALPHABET[alphabet_index]:
                encrypted_string += AL_BHED[alphabet_index]
                match_found = True
        if not match_found:
            encrypted_string += message[letter_index]
    return encrypted_string

def decode_function(value):
    message = value
    decrypted_string = ""
    for letter_index in range(len(message)):
        match_found = False
        for alphabet_index in range(len(ALPHABET)):
            if message[letter_index] == AL_BHED[alphabet_index]:
                decrypted_string += ALPHABET[alphabet_index]
                match_found = True
        if not match_found:
            decrypted_string += message[letter_index]
    return decrypted_string

while running:

    try:
        key = int(input("\n1) Encode text\n2) Decode text\n3) Exit program\n Please select an option (1-3): "))

        if key < 1 or key > 3:
            print("\nPlease select a valid option between 1 and 3")
        elif key == 1:
            text_to_encode = input("Please enter the text to encode: ") 
            print("Encoded text: " +  encode_function(text_to_encode))
        elif key == 2: 
            text_to_decode = input("Please enter the text to decode: ")  
            print("Decoded text: " + decode_function(text_to_decode))
        elif key == 3:
            print("Thank you, smile often Life is too short to Freight")

            running = False
            exit()
        else:
            running = True   
    except ValueError as e:
           print ('NOTE: Only integer values are allowed.No string literal')
           running = True   
