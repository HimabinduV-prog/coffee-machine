# Coffee Machine Program

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 15
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 25
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 30
    },
    "normal coffee": {
        "ingredients": {"water": 150, "milk": 100, "coffee": 20},
        "cost": 20
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

profit = 0

def is_resource_sufficient(ingredients_needed):
    for item in ingredients_needed:
        if ingredients_needed[item] > resources.get(item, 0):
            print(f" Sorry, not enough {item} available.")
            return False
    return True

def collect_indian_coins():
    print(" Please insert Indian coins:")
    total = int(input(" How many ₹10 coins? ")) * 10
    total += int(input(" How many ₹5 coins? ")) * 5
    total += int(input(" How many ₹2 coins? ")) * 2
    total += int(input(" How many ₹1 coins? ")) * 1
    return total

def is_payment_successful(amount_given, cost):
    if amount_given >= cost:
        change = amount_given - cost
        if change > 0:
            print(f" Payment successful! Your change is ₹{change}")
        global profit
        profit += cost
        return True
    else:
        print(" Not enough money. Refunding payment.")
        return False

def make_coffee(coffee_name, ingredients_used):
    for item in ingredients_used:
        resources[item] -= ingredients_used[item]
    print(f" Here is your {coffee_name}. Enjoy!")

machine_on = True

while machine_on:
    print("\n Available options: espresso / latte / cappuccino / normal coffee")
    choice = input(" What would you like? ").lower()

    if choice == "off":
        print(" Turning off machine. Goodbye!")
        machine_on = False

    elif choice == "report":
        print(f"\n Current Machine Report:")
        print(f" Water: {resources['water']} ml")
        print(f" Milk: {resources.get('milk', 0)} ml")
        print(f" Coffee: {resources['coffee']} g")
        print(f" Money Collected: ₹{profit}")

    elif choice in MENU:
        drink = MENU[choice]
        ingredients = drink["ingredients"]
        cost = drink["cost"]

        if is_resource_sufficient(ingredients):
            payment = collect_indian_coins()
            if is_payment_successful(payment, cost):
                make_coffee(choice, ingredients)

    else:
        print(" Invalid choice. Please choose from the available options.")
