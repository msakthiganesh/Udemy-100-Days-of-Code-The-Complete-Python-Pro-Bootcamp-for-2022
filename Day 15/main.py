def report(milk_available, water_available, coffee_available):
    print(f"Milk remaining: {milk_available} ml")
    print(f"Water remaining: {water_available} ml")
    print(f"Coffee remaining: {coffee_available} gm")


def start_machine():
    milk_available = int(input("Enter the quantity of milk added in ml: "))
    water_available = int(input("Enter the quantity of water added in ml: "))
    coffee_available = int(input("Enter the quantity of coffee powder added in gm: "))
    report(milk_available, water_available, coffee_available)
    return milk_available, water_available, coffee_available


def main():
    machine_data = start_machine()
    milk_available, water_available, coffee_available = start_machine()[0], start_machine()[1], start_machine()[2]
    continue_serving = True
    while continue_serving:
        user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
        if user_choice.lower() == "report":
            report(milk_available, water_available, coffee_available)
        elif user_choice.lower() == "espresso":
            pass
        elif user_choice.lower() == "latte":
            pass
        elif user_choice.lower() == "cappuccino":
            pass
        else:
            print("Invalid entry. Please try again!")


if __name__ == "__main__":
    main()
