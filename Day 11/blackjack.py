from art import logo
import random

def print_cards(user_cards, computer_cards):
    print(f"Your cards are: {user_cards}, Sum: {sum(user_cards)}")
    print(f"Computer first card: {computer_cards[0]}")
        

def print_result(user_lost, computer_lost, user_cards, computer_cards):
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

def main():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    
    new_game = True
    while new_game:
        print(logo)
        user_lost, computer_lost, match_draw, user_won = False, False, False, False
        
        user_cards = [10, 1]
        computer_cards = random.choices(cards, k=2)
        print_cards(user_cards, computer_cards)
        
        if sum(computer_cards) == 21:
            user_lost = True
        elif sum(user_cards) == sum(computer_cards) == 21:
            match_draw = True
        elif sum(user_cards) == 21:
            computer_lost = True
        
        if not user_lost and not computer_lost and not match_draw:
            pick_more_cards = True if input("Do you want to pick another card? Type 'y' or 'n': ") == "y" else False
            while pick_more_cards:
                user_cards.append(random.choice(cards))
                if sum(user_cards) > 21:
                    if 11 in user_cards:
                        user_cards.append(1)
                        user_cards.remove(11)
                    else:
                        user_lost = True
                        print_cards(user_cards, computer_cards)
                        break
                elif sum(user_cards) == 21:
                    user_won = True
                    print_cards(user_cards, computer_cards)
                    break
                
                print_cards(user_cards, computer_cards)
                if not user_won:
                    pick_more_cards = True if input("Do you want to pick another card? Type 'y' or 'n': ") == "y" else False
            
        if user_lost !=1:
            while sum(computer_cards) < 17:
                computer_cards.append(random.choice(cards))
                if sum(computer_cards) > 21:
                    computer_lost = True
                    break
        
        print_result(user_lost, computer_lost, user_cards, computer_cards)
        
        new_game = True if input("Do you want to play a new game? Type 'y' or 'n': ") == 'y' else False
        
        


if __name__ == "__main__":
    main()