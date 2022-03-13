import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Do not use random.choice() in your program
person_index = random.randint(0, len(names) - 1)
person_name = names[person_index]
print(f"{person_name} is going to buy the meal today!")