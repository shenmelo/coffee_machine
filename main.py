MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] >= order_ingredients[item]:
            return True
        else:
            print(f"Sorry there's not enough {item}.")
            return False


def process_coins():
    print("Please insert coin.")
    total = int(input("how many quarter: ")) * 0.25
    total += int(input("how many dime: ")) * 0.1
    total += int(input("how many nickle: ")) * 0.05
    total += int(input("how many penny: ")) * 0.01
    return total


def is_payment_successful(payment_received, drink_cost):
    if payment_received >= drink_cost:
        change = payment_received - drink_cost
        print(f"Here is ${change:.2f} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's you {drink_name} ☕️ Enjoy!")


is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {resources['water']}")
    else:
        drink = MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_payment_successful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])

