'''

Day 3: Control Structures

Write a program that asks the user for a number and prints whether it is positive or negative.

Extend the program to identify whether the number is even or odd.

'''

print("Enter a number: ")
user_input = input()
number_int = int(user_input)
if number_int >= 0:
    print("The number is positive")
else:
    print("The number is negative")
if number_int %2 == 0:
    print(f'{number_int} is even ')
else:
    print(f'{number_int} is odd')
    