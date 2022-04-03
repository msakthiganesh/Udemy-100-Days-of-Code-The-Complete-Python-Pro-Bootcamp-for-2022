#Write your code below this line 👇
def prime_checker(number:int):
    flag = 1

    for i in range(2, number):
        if number % i == 0:
            flag = 0
            break
            

    if flag == 1:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
