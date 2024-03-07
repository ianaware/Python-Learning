'''

• Create a list of five fruits and write a loop that prints each fruit in the list.
• Write a program that asks the user for numbers and adds them to a list until the user enters 'done'. Then, print the list.


'''
fruits = ["Apple", "Banana", "Pear", "Grapefruit", "Strawberry"]

for fruit in fruits:
    print(fruit)
        
numbers = []

program_quit = False
        
while not program_quit:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        print(numbers)
        program_quit = True
    else:
        numbers.append(user_input)
        print(f'You have added {user_input} to the list')
    
