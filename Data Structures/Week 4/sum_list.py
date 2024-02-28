'''
Steps 

Declare empty list
Start loop
Ask for user input and store it
End the program if user types 'done'
Convert user input from string to float
Add Float to list
Calculate the sum by adding up all the values in the list and / by length of the list
Print the sum output

'''

num_list = []
while (True):
    user_input = input("Enter a number: ")
    if user_input == 'done': break
    value = float(user_input)
    num_list.append(value)
    current_value = value
    sum_value = sum (num_list)
    print("Current Value: ", current_value)
    print("Sum: ", sum_value)
