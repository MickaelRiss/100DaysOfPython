import string

ascii_art = r"""
   ______                              
  / ____/___ ____  _________ ______    
 / /   / __ `/ _ \/ ___/ __ `/ ___/    
/ /___/ /_/ /  __(__  ) /_/ / /        
\____/\__,_/\___/____/\__,_/_/         
   _______       __                    
  / ____(_)___  / /_  ___  _____       
 / /   / / __ \/ __ \/ _ \/ ___/       
/ /___/ / /_/ / / / /  __/ /           
\____/_/ .___/_/ /_/\___/_/            
      /_/
"""

print(ascii_art)
alphabet = string.ascii_lowercase

def encrypt(original_text, shift_amount):
    encode = ""
    index = 0
    for letter in original_text:
        index = alphabet.find(letter) + shift_amount
        if index > 25:
            index = index - 26
        encode += list(alphabet)[index]

    print(f"Here's the code encoded result : {encode}")

def decrypt(original_text, shift_amount):
    decode = ""
    index = 0
    for letter in original_text:
        index = alphabet.find(letter) - shift_amount
        if index > 25:
            index = index - 26
        decode += list(alphabet)[index]

    print(f"Here's the code decoded result : {decode}")

def caesar(original_text, shift_amount, encode_or_decode):
    encrypt(original_text, shift_amount) if encode_or_decode == 'encode' else decrypt(original_text, shift_amount)

stop_program = False

while not stop_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    while direction != "encode" and direction != "decode":
        direction = input("Sorry, can you please type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(message, shift, direction)
    stop_program = True if input("Type 'yes' if you want to go again\n").lower() != 'yes' else 0

print("Goodbye :)")