'''

Exercise: Validating Phone Numbers

Goal: Write a Python program using regular expressions to check if a given list of phone numbers are valid. A valid phone number:

Starts with a 7, 8, or 9.
Is exactly 10 digits long.
Contains only numeric characters.
Steps to Follow:

Import the re module, which is Python's library for handling regular expressions.

Create a list of phone numbers to validate, e.g., ['7893456789', '1234567890', '9876543210'].

Write a regular expression pattern that matches the rules for a valid phone number. 

Hint: Use ^ to match the start of the string, [789] to match the first digit, and {9} to ensure there are nine more digits.

Use the re.match() function to check each number in the list against your pattern. This function will return a match object if the pattern is found, or None if it's not.

Print out whether each phone number is valid or not.

'''

import re
phone_numbers_list = ['7893456789', '1234567890', '9876543210']

pattern = r'^[789]\d{9}$' #regex pattern

for number in phone_numbers_list:
    if re.match(pattern, number): #use the pattern and look up the numbers in the list stored in the 'number' iteration variable
        print(f'{number} is a valid number') #output if the number is valid
    
    else:
        print(f'{number} is not a valid number')  #output if the number is noy valid
        