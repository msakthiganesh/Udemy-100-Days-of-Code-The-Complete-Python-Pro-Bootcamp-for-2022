from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    machine_running = True
    while machine_running:
        user_choice = input(f"What would you like to have? "
                            f"Your choices are : {menu.get_items()} : ").lower()
        if user_choice == "report":
            coffee_maker.report()
            money_machine.report()
        elif user_choice == "off":
            print("Turning off!")
            machine_running = False
        else:
            drink = menu.find_drink(user_choice)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink):
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
