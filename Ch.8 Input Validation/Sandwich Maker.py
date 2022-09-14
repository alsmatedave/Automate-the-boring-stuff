# Sandwich Maker

import pyinputplus as pyip

BREAD_PRICE = {'white': 2.00, 'wheat': 2.50, 'sourdough': 3.00}
PROTEIN_PRICE = {'chicken': 2.50, 'turkey': 2.75, 'ham': 2.00, 'tofu': 3.25}
CHEESE_PRICE = {'cheddar': 1.00, 'swiss': 1.25, 'mozzarella': 2.00, 'none': 0.00}


# I did steal the bulk of the below from a far smarter person online
# Using a single function for all the choices is extremely clever
# My original contained way to many 'if' statements whereas this contains none

def get_sandwich_choice(category, options):
    prompt = 'Please choose your ' + category +':\n'
    choices = list(options.keys())
    choice = pyip.inputMenu(choices, prompt, numbered = True)
    return (choice, options[choice]) # this returns food choice and the food price as a list
    
bread_choice = get_sandwich_choice('bread',BREAD_PRICE)
protein_choice = get_sandwich_choice('protein', PROTEIN_PRICE)
cheese_choice = get_sandwich_choice('cheese', CHEESE_PRICE)

total_price = bread_choice[1] + protein_choice[1] + cheese_choice[1]

pyip.inputYesNo(f'The price for your sandwich is: ' + '£' + f'{total_price:.2f}' +'\nIs this okay? ')



