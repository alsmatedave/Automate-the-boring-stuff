#! python 

# bulletPointAdder.py - Adds bullet points to the start of items in a list

import pyperclip
text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n') # changes the text into a list with each line an element on the list

for i in range(len(lines) - 1):
    lines[i] = '* ' + lines[i] # add star to each string in 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)