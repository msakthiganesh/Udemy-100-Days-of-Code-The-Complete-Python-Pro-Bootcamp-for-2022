alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

import itertools

def ceaser(plain_text:str, shift_pos:int, direction:str):
    output = ""
    cycle_alphabets = []
    for i, val in enumerate(itertools.cycle(alphabet)):
        if i <= len(alphabet) * 10:
            cycle_alphabets.append(val)
        else:
            break
    
    if direction == "encode":
        for char in plain_text:
            output += cycle_alphabets[cycle_alphabets.index(char) + shift_pos]
    elif direction == "decode":
        cycle_alphabets.reverse()
        for char in plain_text:
            output += cycle_alphabets[cycle_alphabets.index(char) + shift_pos]
    
    print(f"The {direction}d output is {output}")
    

ceaser(text, shift, direction)    
    

