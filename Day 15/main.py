def start_machine():
    milk_available = int(input("Enter the quantity of milk added in ml: "))
    water_available = int(input("Enter the quantity of water added in ml: "))
    coffee_available = int(input("Enter the quantity of coffee powder added in gm: "))
    report(milk_available, water_available, coffee_available)
    return milk_available, water_available, coffee_available


def report(milk_available, water_available, coffee_available, amount_collected=None):
    print("###### REPORT ######")
    print(f"Milk remaining: {milk_available} ml")
    print(f"Water remaining: {water_available} ml")
    print(f"Coffee remaining: {coffee_available} gm")
    if amount_collected:
        print(f"Amount Collected: ${amount_collected}")


def handle_money(drink_price):
    print("Please insert coins.")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    money_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if money_inserted > drink_price:
        print(f"Here is ${round(drink_price - money_inserted, 2)} in change")
        return True
    elif money_inserted == drink_price:
        return True
    else:
        return False


def main():
    machine_data = start_machine()
    amount_collected = 0
    milk_available, water_available, coffee_available = machine_data[0], machine_data[1], machine_data[2]

    drink_data = {
        "espresso": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
            "price": 1.5
        },
        "latte": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
            "price": 2.5
        },
        "cappuccino": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
            "price": 3.0
        }
    }

    continue_serving = True
    while continue_serving:
        user_choice = input("What would you like? (Espresso/Latte/Cappuccino): ")
        if user_choice.lower() == "report":
            report(milk_available, water_available, coffee_available, amount_collected)
        elif user_choice.lower() == "espresso":
            drink = drink_data["espresso"]
            if milk_available >= drink["milk"] and water_available >= drink["water"] and coffee_available >= drink[
                "coffee"]:
                enough_money = handle_money(drink_price=drink["price"])
                if enough_money:
                    print(f"Here is your {user_choice.title()}. Enjoy!")
                    milk_available -= drink["milk"]
                    water_available -= drink["water"]
                    coffee_available -= drink["coffee"]
                    amount_collected += drink["price"]
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        elif user_choice.lower() == "latte":
            drink = drink_data["latte"]
            if milk_available >= drink["milk"] and water_available >= drink["water"] and coffee_available >= drink[
                "coffee"]:
                enough_money = handle_money(drink_price=drink["price"])
                if enough_money:
                    print(f"Here is your {user_choice.title()}. Enjoy!")
                    milk_available -= drink["milk"]
                    water_available -= drink["water"]
                    coffee_available -= drink["coffee"]
                    amount_collected += drink["price"]
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        elif user_choice.lower() == "cappuccino":
            drink = drink_data["cappuccino"]
            if milk_available >= drink["milk"] and water_available >= drink["water"] and coffee_available >= drink[
                "coffee"]:
                enough_money = handle_money(drink_price=drink["price"])
                if enough_money:
                    print(f"Here is your {user_choice.title()}. Enjoy!")
                    milk_available -= drink["milk"]
                    water_available -= drink["water"]
                    coffee_available -= drink["coffee"]
                    amount_collected += drink["price"]
                else:
                    print("Sorry, that's not enough money. Money refunded.")
        elif user_choice.lower() == "off":
            print("Turning off machine!")
            continue_serving = False
        else:
            print("Invalid entry. Please try again!")


if __name__ == "__main__":
    main()
