# Udemy - 100 Days of Code: The Python Pro Bootcamp for 2022
# Project - Day 4 - Rock, Paper, and Scissors
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
opponent = random.choice(["rock", "paper", "scissors"])

if choice==0:
    user_choice = "rock"
    print(rock)
elif choice == 1:
    user_choice = "paper"
    print(paper)
else:
    user_choice = "scissors"
    print(scissors)

print("\nComputer Chooses: \n")
if opponent == "rock":
    print(rock)
elif opponent =="paper":
    print(paper)
else:
    print(scissors)


if user_choice == opponent:
    print("Draw!")
elif user_choice == "rock" and opponent == "paper":
    print("You lose!")
elif user_choice == "rock" and opponent == "scissors":
    print("You win!")
elif user_choice == "paper" and opponent == "rock":
    print("You win!")
elif user_choice == "paper" and opponent == "scissors":
    print("You lose!")
elif user_choice == "scissors" and opponent == "rock":
    print("You lose!")
elif user_choice == "scissors" and opponent == "paper":
    print("You win!")
else:
    print("Please check your input!")
    

