from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    item = menu.get_items()
    choice = input(f"What would you like? ({item}):").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        cost = drink.cost
        resource_sufficient = coffee_maker.is_resource_sufficient(drink)
        money_sufficient = money_machine.make_payment(cost)
        if resource_sufficient and money_sufficient:
            coffee_maker.make_coffee(drink)
