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

is_on = True


def print_resources_report():
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")
    print(f"Money:${profit}")


while is_on:
    choise = input("What would you like? (espresso/latte/cappuccino)\n")
    if choise == "off":
        print("See you later!")
        is_on = False
        break
    elif choise == "report":
        print_resources_report()



