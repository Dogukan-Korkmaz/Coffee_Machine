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
    print(f"Money:${profit}.")


def compare(coffee_ingredients):
    not_enough = False
    for item in coffee_ingredients:
        if coffee_ingredients[item] <= resources[item]:
            print(f"{item.capitalize()}, enough.")
        else:
            print(f"{item.capitalize()}, not enough.")
            not_enough = True
    if not_enough:
        return True
    else:
        return False


def prosses_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters do you want to insert ?\n")) * 0.25
    total += int(input("How many dimes do you want to insert ?\n")) * 0.10
    total += int(input("How many nickles do you want to insert ?\n")) * 0.05
    total += int(input("How many pennies do you want to insert ?\n")) * 0.01
    return round(total, 2)


def is_transaction_successful(money_received, drink_cost):
    """Return True or false for transaction outcame"""
    if money_received >= drink_cost:
        global profit
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        profit += drink_cost
        return True
    else:
        return False


def update_resources(coffee_name, coffee_resourses_cost):
    for item in coffee_resourses_cost:
        resources[item] -= coffee_resourses_cost[item]
    print(f"Here is your {coffee_name}☕")


def main_program():
    global is_on
    while is_on:
        choise = input("What would you like ? (espresso/latte/cappuccino)\n")
        if choise == "off":
            print("See you later!")
            is_on = False
        elif choise == "report":
            print_resources_report()
        elif choise == "espresso" or "latte" or "cappuccino":
            drink = MENU[choise]
            if compare(drink["ingredients"]):
                print("Sorry these ingredients need to refresh. ☹")
                is_on = False
                break

            total_cost = prosses_coins()
            print(f"Total is : ${total_cost}")
            coffee_cost = MENU[choise]["cost"]

            if is_transaction_successful(total_cost, coffee_cost):
                print("Transaction is successful.")
                coffee = MENU[choise]["ingredients"]
                update_resources(choise, coffee)
            else:
                print("Sorry that's not enough money. Money refunded.")


if is_on:
    main_program()
