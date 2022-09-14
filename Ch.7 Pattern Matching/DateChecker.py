import re

# Looks for dates in the format DD/MM/YYYY in a body of text then checks
# whether all the dates are valid. Also checks for leap years!

text = 'My name is Haruto Watanabe and I was born 31/04/2005 not 29/02/1800'
dateRegex = re.compile(r'([0-3]\d)/([0-1]\d)/([1-3]\d{3})')

mo = dateRegex.findall(text)  # this returns a list of tuples


for date in mo:
    d = int(date[0])  # day
    m = int(date[1])  # month 
    y = int(date[2])  # year
    fullDate = '/'.join([date[0],date[1],date[2]])

    if d > 31 or ((m in [4,6,9,11]) and d > 30):
        print(fullDate + ' is an invalid date')
    elif m == 2:
        if d > 29:
            print(fullDate + ' is an invalid date')
        elif d == 29:     # the following checks if it's a leap year
            if y % 4 == 0:
                if y % 100 != 0:
                    print(fullDate +' is a leap year.')
                else:
                    if y % 400 == 0:
                        print(fullDate +' is a leap year.')
                    else:
                        print(fullDate + ' is an invalid date (not a leap year)')
            else:
                print(fullDate +' is an invalid date (not a leap year).')
        else:
            print(fullDate)
    else:
        print(fullDate)
    

