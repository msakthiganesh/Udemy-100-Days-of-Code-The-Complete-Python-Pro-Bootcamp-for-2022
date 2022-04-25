from art import logo
import random

def print_cards(user_cards, computer_cards):
    print(f"Your cards are: {user_cards}, Sum: {sum(user_cards)}")
    print(f"Computer first card: {computer_cards[0]}")
        
    

def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    new_game = True
    while new_game:
        print(logo)
        user_lost, computer_lost = False, False
        
        user_cards = random.choices(cards, k=2)
        computer_cards = random.choices(cards, k=2)
        print_cards(user_cards, computer_cards)
        
        pick_more_cards = True if input("Do you want to pick another card? Type 'y' or 'n': ") == "y" else False
        while pick_more_cards:
            user_cards.append(random.choice(cards))
            print_cards(user_cards, computer_cards)
            if sum(user_cards) > 21:
                user_lost = True
                break
            
            pick_more_cards = True if input("Do you want to pick another card? Type 'y' or 'n': ") == "y" else False
            
        if user_lost !=1:
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))
                if sum(computer_cards) > 21:
                    computer_lost = True
                    break
        
        if user_lost:
            print("You lose")
            print(f"Computer Cards: {computer_cards}")
            
        elif computer_lost:
            print("You win")
            print(f"Computer Cards: {computer_cards}")
            
        elif sum(user_cards) == sum(computer_cards) == 21:
            print("Its a Draw")
            print(f"Computer Cards: {computer_cards}")
            
        elif 21 - sum(user_cards) < 21 - sum(computer_cards):
            print("You win")
            print(f"Computer Cards: {computer_cards}")
            
        else:
            print("You lose")
            print(f"Computer Cards: {computer_cards}")
        
        
        new_game = True if input("Do you want to play a new game? Type 'y' or 'n': ") == 'y' else False
        
        


if __name__ == "__main__":
    main()