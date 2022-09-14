import pyinputplus as pyip
import time

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0        },
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
    "profit": 0.00
}

def CoffeeChoice(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print('Sorry there is not enough water.')
    elif resources['milk'] < MENU[coffee]['ingredients']['milk'] and resources['milk'] != None:
        print('Sorry there is not enough milk.')
    elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print('Sorry there is not enough coffee.')
    else: 
        print(f'{coffee} costs ${(MENU[coffee]["cost"]):.2f}\nPlease insert coins.')
        quarters = pyip.inputInt('How many quarters? ', min=0)
        dimes = pyip.inputInt('How many dimes? ', min=0)
        pennies = pyip.inputInt('How many pennies? ', min=0)
        totalMoney = quarters*0.25 + dimes*0.1 + pennies*0.01
        if totalMoney < MENU[coffee]['cost']:
            print("Sorry that's not enough money. Money refunded.")
        elif totalMoney == MENU[coffee]['cost']:
            print(f'Thank you. Enjoy your {coffee}!')
            resources['water'] -= MENU[coffee]['ingredients']['water'] 
            resources['milk'] -= MENU[coffee]['ingredients']['milk']
            resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
            resources['profit'] += MENU[coffee]['cost']
        elif totalMoney > MENU[coffee]['cost']:
            change = totalMoney - MENU[coffee]['cost']
            print(f'Thank you. Here is ${change:.2f} in change. Enjoy your {coffee}')
            resources['water'] -= MENU[coffee]['ingredients']['water'] 
            resources['milk'] -= MENU[coffee]['ingredients']['milk']
            resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
            resources['profit'] += MENU[coffee]['cost']
            

while True:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        for key, value in resources.items():  # need the .items method to use dictionaries in a for loop
            if key in ['water', 'milk']:
                    print((key + ':').ljust(10) + f'{value}ml')
            elif key == 'coffee':
                    print((key + ':').ljust(10) + f'{value}g')
            else:
                    print((key + ':').ljust(10) + f'${value:.2f}')
        time.sleep(1)
    elif choice in ['cappuccino', 'latte', 'espresso']:
            CoffeeChoice(choice)
            time.sleep(1)
    elif choice == 'off':
        break
    else:
        print('Incorrect input. Please try again.')

            
            





                
    


                



