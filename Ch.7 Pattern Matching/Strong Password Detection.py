# Function which uses Regex to check whether password is strong
# A strong password is defined as one that is at least eight characters
# long, contains both uppercase and lowercase characters, and has
# at least one digit.

import random
import re


def checkPass():
    print('Please type your password:')
    password = input()
    upperRegex = re.compile(r'[A-Z]')  # I tried doing this using one Regex and groups first of all
    lowerRegex = re.compile(r'[a-z]')  # but it didn't work e.g. re.compile(r'([A-Z])([a-z])([0-9])')
    numRegex = re.compile(r'\d')  # and using mo.group(1) etc. This didn't work because the groups
    moUp = upperRegex.search(password)  # are subgroups of the whole group. If the whole group isn't in
    moLow = lowerRegex.search(password)  # the password then the subgroups aren't either.
    moNum = numRegex.search(password)

    if moUp is not None and moLow is not None and moNum is not None and len(password) > 7:
        print('Strong Password')
    else:
        print('Weak Password; try again')
        checkPass()  # Recalls the function


checkPass()
