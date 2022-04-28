from art import logo
import random

HARD_ATTEMPTS = 5
EASY_ATTEMPS = 10

def set_difficulty() -> int:
    difficulty = input("Choose a diificulty. Type 'easy' or 'hard': ")
    
    if difficulty.lower() == "hard":
        trials = HARD_ATTEMPTS
    else:
        trials = EASY_ATTEMPS
        
    return trials


def main():

    play_again = True
    
    while play_again:
        
        print(logo)
        print("Welcome to the Number Guessing Game!")
        print("I'm thinking of a number between 1 and 100")

        number_to_guess = random.randint(1, 100)
        trials = set_difficulty()

        while trials > 0:
            print(f"You have {trials} attempts to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == number_to_guess:
                print(f"You've guessed the right number! It was {number_to_guess}!")
                break
            elif guess < number_to_guess:
                print("Too low")
                trials -= 1
            else:
                print("Too high")
                trials -= 1

        if trials == 0:
            print(f"You've lost the game. The number was {number_to_guess}")

        play_again = (
            True
            if input("Do you want to play again? Type 'y' or 'n': ").lower() == "y"
            else False
        )


if __name__ == "__main__":
    main()
