from platform import machine
from tkinter import Menu
from Logo import logo
print(logo)

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
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True


def report():
    for i in resources:
        print(resources,resources[i])

machine = input("what whould you like ? (espresso/latte/cappuccino)").lower()
if machine == 'report':
    report()

drink = MENU[machine]
if machine == 'espresso':
    total = process_coins()
    if total < 2.5:
        print("sorry there is not enough money")
    else:
        if is_resource_sufficient(drink["ingredients"]) == False:
               print("sorry there are no resource")
        is_resource_sufficient(drink["ingredients"])
        remaining_money = total - (MENU['espresso']['cost'])
        print(f"You remaining money is {remaining_money}")
        print("enjoy your milks")

if machine == 'latte':
    total = process_coins()
    if total <(MENU['latte']['cost']):
        print("sorry there is not enough money")
    else:
       if is_resource_sufficient(drink["ingredients"]) == False:
           print("sorry there are no resource")
       remaining_money = total - (MENU['latte']['cost']) 
       print(f"You remaining money is {remaining_money}")
       print("enjoy your milks")

if machine == 'cappuccino':
    total = process_coins(drink["ingredients"])
    if total <(MENU['cappucino']['cost']):
        print("sorry there is not enough money")
    else:
        if is_resource_sufficient(drink["ingredients"]) == False:
               print("sorry there are no resource")
        is_resource_sufficient(MENU["ingredients"])
        remaining_money = total - (MENU['cappucino']['cost'])
        print(f"You remaining money is {remaining_money}")
        print("enjoy your milks")



    



    

