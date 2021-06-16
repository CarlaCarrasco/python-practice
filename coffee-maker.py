# Coffee Machine Class

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


latte = MenuItem('latte', 100, 16, 1, 3.50)
espresso = MenuItem('espresso', 100, 16, 1, 2.50)
cappuccino = MenuItem('cappuccino', 100, 16, 1, 3.25)
coffeeMaker = CoffeeMaker()
payment = MoneyMachine()

drink = input('​What would you like? (espresso/latte/cappuccino/: ')

if(drink == 'latte'):
    drink = latte
if(drink == 'espresso'):
    drink = espresso
if(drink == 'cappuccino'):
    drink = cappuccino

resources = coffeeMaker.is_resource_sufficient(drink)

if(resources):
    print('We can totally make your drink!')
    print('This drink costs', drink.cost, '. Please enter your payment.')

    if(payment.make_payment(drink.cost)):
        print('------- REPORT -------')
        coffeeMaker.report()
        coffeeMaker.make_coffee(drink)

else:
    print(resources)
    print('Uh Oh! We are all out of resources!')
    print('Come back tomorrow!')
