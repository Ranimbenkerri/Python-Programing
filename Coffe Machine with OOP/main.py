from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
 
menu = Menu()
Coffe = CoffeeMaker()
money = MoneyMachine()
print(money.report())

is_on = True
while is_on:
    options = menu.get_items()
    machine = input(f"what whould you like ? {options} : ").lower()
    if machine == 'off':
        is_on=False 
    elif machine == 'report':
        Coffe.report()
        money.report()
    else:
        drink=menu.find_drink(machine)
        if Coffe.is_resource_sufficient(drink) and money.make_payment(drink.cost) :
             Coffe.make_coffee(drink)
 
  

