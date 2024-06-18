# TODO insert the data of the resources used in every coffee required for the coffee machine
Menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,

    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3,
    }
}
# TODO 2: determine the quantity of resources present in the coffee machine
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100

}


def is_resource(order_ingredient):
    """if the ingredients are sufficient
    then the function returns true else returns false"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there are not enough {item}")
            return False
    return True


def process_coins():
    """This function returns the total coins that are inserted"""
    print("Please insert coins: ")
    total = int(input('How may quarters do you have ')) * 0.25
    total += int(input("How many dimes do you have? ")) * 0.1
    total += int(input("How many nickels do you have? ")) * 0.50
    total += int(input("How many pennies do you have? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns true if money is accepted else returns false"""
    if money_received >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_received-drink_cost, 2)
        print(f"Here is your change ${change}")
        return True
    else:
        print("Sorry that's not enough money. The money is refunded")
        return False


def make_coffee(coffe_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for o in order_ingredients:
        resources[o] -= order_ingredients[o]
    print(f"Here is your {coffe_name}. Enjoy ☕")


# empty money box of the machine
profit = 0
# TODO 1: print a statement asking the user "What would you like? (espresso/latte/cappuccino):”.
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk:  {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        if choice not in Menu:
            print("Sorry invalid input please try again.")
        else:
            drink = Menu[choice]
            if is_resource(drink['ingredients']):
                payment = process_coins()
                if is_transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])
