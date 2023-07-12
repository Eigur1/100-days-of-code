from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    machine = True
    while machine:
        choice = input(f"Drink? type {menu.get_items()}: ")
        if choice == "off":
            machine = False
        elif choice == "report":
            report = money_machine.report()
            print(f"{coffee_maker.report()} {report}")
            return
        elif menu.find_drink(choice):
            drink = menu.find_drink(choice)
            cost = drink.cost
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost):
                cost = drink.cost

coffee_machine()