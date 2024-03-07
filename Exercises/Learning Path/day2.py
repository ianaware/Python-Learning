''''

Write a program that asks the user for their name and greets them with their name.

Modify the program to convert the user’s name to uppercase and print the length of their name.

'''

print("Hello, tell me your name ")
user_name = input() #get user input
print(f'Hello, {user_name}, nice to meet you!') #output user name
print(f'Your name in uppercase is {user_name.upper()}') #convert to uppercase and output
print(f'The length of your name is {len(user_name)}') #get length and output