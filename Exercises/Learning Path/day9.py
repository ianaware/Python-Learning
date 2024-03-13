'''
• Modify one of your previous programs to include try-except blocks to handle errors like division by zero and type errors.
• Write a program that repeatedly asks the user for a number until a valid number is entered



'''
user_input = input("Enter a number:")
try:
    user_int = int(user_input)
    print(f'You have entered {user_int}')
except ValueError:
    print("Enter a valid option")
    

while True:
    user_input2 = input("Enter a number: ")
    try:
        user_int2 = int(user_input2)
        print(f'You have entered {user_input2}')
        break
    except ValueError:
        print("Enter a valid option")
