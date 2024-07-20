# To learn OOP
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()

my_money = MoneyMachine()
my_coffee_maker = CoffeeMaker()

coffee_mech_on = True

while coffee_mech_on:
    items = my_menu.get_items()
    user_want = input(f"choose one drink from below {items}").lower()
    if user_want == "off":
        coffee_mech_on = False
    elif user_want == "report":
        my_coffee_maker.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(user_want)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)