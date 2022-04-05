alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

import itertools

def encrypt(plain_text:str, shift_pos:int):
    encrypted_text = ""
    
    cycle_alph = itertools.cycle(alphabet)
    cycle_alphabets = []
    for i, val in enumerate(cycle_alph):
        cycle_alphabets.append(val)
        if i > 1000: break
    
    for char in plain_text:
        encrypted_text += cycle_alphabets[alphabet.index(char) + shift_pos]
    
    print(f"The encoded output is {encrypted_text}")

def decrypt(plain_text:str, shift_pos:int):
    decrypted_text = ""
    
    reverse_cycle_alpha = []
    for i, val in enumerate(itertools.cycle(alphabet)):
        reverse_cycle_alpha.insert(0, val)
        if i==len(alphabet)*10 - 1:
            break
    
    for char in plain_text:
        decrypted_text += reverse_cycle_alpha[reverse_cycle_alpha.index(char) + shift_pos]
    
    print(f"The decrypted text is {decrypted_text}")
    
    
if direction == "encode":
    encrypt(plain_text = text, shift_pos = shift)
elif direction == "decode":
    decrypt(plain_text = text, shift_pos=shift)



