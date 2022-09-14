#! python

# mcb.py - Saves and loads pieces of text to the clipboard

# Run the program from the command line followed by save <keyword> - Saves clipboard to keyword
# Run the program from the command line followed by <keyword> - Loads keyword to clipboard
# Run the program from the command line followed by list - Loads all keywords to clipboard

import shelve, pyperclip, sys, os

mcbShelf = shelve.open('mcb') # this will create a new shelf file in my cmd (remember it's actually 3 files)
                              # shelf files are similar to dictionary 

# Save clipboard content: 

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()   # the keyword is now the 'key' for the copied clipboard text in the mcbShelf 'dictionary'
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))  # copies all the 'key' values in mcbShelf to the clipboard (as a list of strings)
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])   # copy the text associated with the keyword from the mcbShelf 'dictionary' 

mcbShelf.close()

