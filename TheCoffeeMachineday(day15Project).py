from art import the_coffee_machine

print(the_coffee_machine)

coffee_menu = {
    "espresso": {
        "ingredients": {
            "water": 50,      
            "coffee": 18       
        },
        "cost": 1.5            
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

profit = 0

resources = {
    "water": 300,   
    "milk": 200,   
    "coffee": 100 
}

def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, false if there's not enough ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, or false if the money is not enough"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredeints from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients
    print(f"Here is your {drink_name}. Enjoy!")

is_on = True

while is_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_type=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif coffee_type=="off":
        is_on = False
    else:
        try:
           drink = coffee_menu[coffee_type]
           if is_resource_sufficient(drink["ingredients"]):
               payment = process_coins()
               if is_transaction_successful(payment,drink["cost"]):
                   make_coffee()
        except KeyError:
            print("This option is not in the menu")
        