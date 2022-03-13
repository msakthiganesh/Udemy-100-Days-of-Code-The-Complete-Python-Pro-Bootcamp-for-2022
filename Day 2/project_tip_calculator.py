# Udemy - 100 Days of Code: The Python Pro Bootcamp for 2022
# Day 2: Project - Bill Tip Calculator

print("Welcome to the tip calculator")
bill_amount = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
head_count = int(input("How many people to split the bill? "))
print(f"Each person should pay: {round((bill_amount * (1 + tip_percentage/100))/head_count, 2)}")

