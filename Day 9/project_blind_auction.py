from unicodedata import name
from art import logo
import os

def highest_bidder(bids: dict) -> None:
    highest_bidder, highest_value = "", 0
    for bidder, value in bids.items():
        if value > highest_value:
            highest_bidder = bidder
            highest_value = value    
    print(f"The winner is {highest_bidder} with a bid of ${highest_value}.")

def main():
    print(logo)
    print("Welcome to the secret auction program.")

    bids = {}

    another_bidder = True
    while another_bidder:
        user_name = input("What is your name? : ")
        user_bid = int(input("What is your bid? : "))
        more_bidders = input("Are there any other bidders? Type 'yes' or 'no' : ")
        
        bids[user_name] = user_bid
        another_bidder = True if more_bidders=="yes" else False
        os.system("clear")
    
    highest_bidder(bids)

if __name__ == "__main__":
    main()

