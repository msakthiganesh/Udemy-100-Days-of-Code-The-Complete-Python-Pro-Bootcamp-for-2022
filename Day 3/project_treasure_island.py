# Udemy - 100 Days of Code: The Python Pro Bootcamp for 2022
# Day 3 - Project : Treasure Island

print("Welcome to Treasure Island.\nYour mission is to find the trasure.")

cross_road = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")
if cross_road == "left":
    lake = input("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")
    if lake == "wait":
        door = input("You arrivee at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if  door == "blue":
            print("Congratulation! You have found the treasure!")
        else:
            print("Oops! You have been sucked into the black hole!")
    else:
        print("Oops! You have been eaten by the crocodiles!")
else:
    print("Oops! You have fallen into a manhole!")



