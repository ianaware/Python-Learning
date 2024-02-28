'''
Creating a Python program that asks the user to enter numbers one at a time and then calculates the average of those numbers

'''

num_list = [] #create empty list
num_list_total = 0 #store the sum
num_list_count = 0 #store the count

while (True):
    user_input = input("Enter a number to add to the list or type 'quit' to end ")

    if user_input.lower() == 'quit':
        break
    
    try:
        user_input_float = float(user_input) #convert string to float
        num_list.append(user_input_float)
        print("The list contains: ", num_list)
    
        num_list_total = num_list_total + user_input_float  # Add just the new number to the total sum
        num_list_count = len(num_list) #calculate count

        print("The average is: ", num_list_total / num_list_count)

    except ValueError:
        print("Invalid input")