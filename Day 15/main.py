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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# Ask user and return answer
def ask_user():
    answer = input("What would you like? (espresso/latte/cappuccino):   ").lower()
    while not answer in ["report", "off", "espresso", "latte", "cappuccino"]:
        answer = input("I don't understand. What would you like (espresso/latte/cappuccino):   ").lower()
    return answer


# Print all current resources
def show_resources():
    for key in resources:
        if key in ["water", "milk"]:
            print(f"{key.capitalize()}: {resources[key]}mL")
        elif key == "coffee":
            print(f"{key.capitalize()}: {resources[key]}g")
        else:
            print(f"{key.capitalize()}: ${resources[key]}")


# Check if enough resources in the machine
def check_resources(answer):
    choice = MENU.get(answer)
    is_enough_resources = True
    for key in choice["ingredients"]:
        if choice["ingredients"][key] > resources[key]:
            print(f"Sorry there is not enough {key}.")
            is_enough_resources = False

    return is_enough_resources


# Ask user to pay
def insert_coins():
    coins = ["quarters", "dimes", "nickels", "pennies"]
    wallet = []

    print("Please insert coins.")
    for coin in coins:
        c = int(input(f"How many {coin}?:  "))
        wallet.append(c)

    total = (0.25 * wallet[0]) + (0.1 * wallet[1]) + (0.05 * wallet[2]) + (0.01 * wallet[3])
    return total


# Compare money put in the machine and price of product
def check_transaction_successful(product, money):
    if money == MENU[product]["cost"]:
        print("Thank you!")
        return True
    elif money > MENU[product]["cost"]:
        change = round(money - MENU[product]["cost"], 2)
        print(f"Here is {change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def update_coffee_machine(choice):
    for key in MENU[choice]["ingredients"]:
        if key in resources:
            resources[key] = resources[key] - MENU[choice]["ingredients"][key]

    resources["money"] += MENU[choice]["cost"]


# Process choice made by user
def process_choice(answer):
    if answer == "report":
        show_resources()
    else:
        if check_resources(answer):
            total = insert_coins()
            if check_transaction_successful(answer, total):
                update_coffee_machine(answer)
                print(f"Here is your {answer}. Enjoy!")


def coffee_machine():
    machine_on = True
    while machine_on:
        choice = ask_user()
        if choice == "off":
            machine_on = False
        else:
            process_choice(choice)

    print("MACHINE TURNED OFF.")

coffee_machine()