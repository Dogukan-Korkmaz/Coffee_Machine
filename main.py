from coffee_data import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

def print_resources(water,milk,coffee):
    return f"Water:{water}\nMilk:{milk}\nCoffee:{coffee}"

while(1):
    answer = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if answer == "off":
        break
    elif answer == "report":
        print(print_resources(water, milk, coffee))
    # elif answer == "espresso":
    #
    # elif answer == "latte":
    #
    # elif answer == "cappuccino":
print("hi")


