'''

Exercise: Validating Email Addresses

Goal: Write a Python program using regular expressions to check if a given list of email addresses are valid. A valid email address, for the sake of this exercise, should:

Start with a series of alphanumeric characters (letters and numbers), which can also include periods (.) and underscores (_).
Be followed by the @ symbol.

After the @ symbol, there should be more alphanumeric characters, which can include periods.
End with a domain extension that starts with a period and then consists of 2 to 4 alphabetical characters.
Steps to Follow:

Import the re module.

Create a list of email addresses to validate, e.g., ['name@example.com', 'name2.example@sub.example.com', 'wrong-email@.com', 'another_wrong_email.com'].
Write a regular expression pattern that matches the rules for a valid email address. Hint: Use ^ to indicate the beginning, [a-zA-Z0-9._]+ to match the user name part, @[a-zA-Z0-9.-]+ for the domain name, and \.[a-zA-Z]{2,4}$ for the domain extension.
Use the re.match() function to check each email address in the list against your pattern. This function will return a match object if the pattern is found, or None if it's not.
Print out whether each email address is valid or not.

'''
import re

email_list = ['name@example.com', 'name2.example@sub.example.com', 'wrong-email@.com', 'another_wrong_email.com']

pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$' #expression, enclose in ' '

for email in email_list: #loop through list
    if re.match(pattern, email): #use the pattern to match against 'emails' - loop variable
        print(f'{email} is a valid email')
    else:
        print(f'{email} is not a valid email')
    
    