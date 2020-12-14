from data import MENU, resources


def pay_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    money = int(input("how many quarters?: ")) * 0.25
    money += int(input("how many dimes?: ")) * 0.1
    money += int(input("how many nickles?: ")) * 0.05
    money += int(input("how many pennies?: ")) * 0.01
    return money


def check_resource(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def check_monyey(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        global profit
        change = money_received - drink_cost
        profit += drink_cost
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order_ingredients, drink_name):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink_name} ☕️. Enjoy!')


def coffee():
    is_on = True
    profit = 0

    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino):").lower()
        if choice == 'off':
            is_on = False
        elif choice == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${profit}")
        else:
            drink = MENU[choice]
            if check_resource(drink['ingredients']):
                payment = pay_money()
                if check_monyey(payment, drink['cost']):
                    make_coffee(drink['ingredients'], choice)

coffee()
