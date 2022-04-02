import random
from re import A
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)

word = random.choice(word_list)
print(f"\nPsst, the solution is {word}")

hangman = []
for i in range(len(word)):
    hangman.append("_")
    
print(hangman)

chosen_words = []
lives = 6

while lives > 0:
    if "_" in hangman:
        user_input = input("Enter your letter: ").lower()
        if user_input in word:
            for i, char in enumerate(word):
                if char == user_input:
                    hangman[i] = char
            print(hangman)
        else:
            if user_input in chosen_words:
                print(f"You've already guessed {user_input}, that's not in the word.")
                print(hangman)
            else:    
                lives -=1
                print(f"You guessed {user_input}, that's not in the word. You lose a life")
                print(stages[lives])
                print(hangman)
        chosen_words.append(user_input)
    else:
        break


if "_" in hangman:
    print("You lost!")
else:
    print("You won!")
