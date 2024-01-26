MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

is_on = True


def print_resources_report():
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")
    print(f"Money:${profit}")


def compare(coffee_ingredients):
    not_enough = False
    for item in coffee_ingredients:
        if coffee_ingredients[item] <= resources[item]:
            print(f"{item.capitalize()}, yeterli.")
        else:
            print(f"{item.capitalize()}, yetersiz.")
            not_enough = True
    if not_enough == True:
        return False
    else:
        return True


while is_on:
    choise = input("What would you like? (espresso/latte/cappuccino)\n")
    if choise == "off":
        print("See you later!")
        is_on = False
        break
    elif choise == "report":
        print_resources_report()
    elif choise == "espresso" or "latte" or "cappuccino":
        drink = MENU[choise]
        compare(drink["ingredients"])



