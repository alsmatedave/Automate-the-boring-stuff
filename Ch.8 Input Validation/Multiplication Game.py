import pyinputplus as pyip

import random, time

numberOfQuestions = 10 
correctAnswers = 0

for questionNumber in range(numberOfQuestions):
    # Pick two random numbers:
    num1 = random.randint(2, 12)
    num2 = random.randint(2, 12)
    prompt = f'Q{questionNumber + 1}: {num1} x {num2} = '
    try:
        # Right answers are handled by allowRegexes.
        # Wrong answers are handled by blockRegexes, with a custom message
        pyip.inputStr(prompt, allowRegexes = [f'^{num1*num2}'], blockRegexes= [('.*', 'Incorrect!')], timeout = 8, limit = 3)
    except pyip.TimeoutException: # if the user takes more than 8 seconds 
        #(note: doesn't automatically go on to next question- waits for input)
        print('Out of time!')
    except pyip.RetryLimitException: # if the user has more than 3 tries
        print('Out of tries!')
    else:
        # This block runs if no exceptions were raised in the try block
        print('Correct!')
        correctAnswers += 1
    time.sleep(1) # Brief pause to let the user see the result
print(f'Score: {correctAnswers} / {numberOfQuestions}')



