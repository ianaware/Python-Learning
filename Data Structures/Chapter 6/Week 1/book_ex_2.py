'''

Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

'''
sum_value = 0
count_value = 0
max_value = None
min_value = None

while True:
    user_input = input("Please enter a number: ")
    if user_input == "done" or user_input == "Done":
        print("Exiting the program ")
        print("Sum: ", sum_value)
        print("Max: ", max_value)
        print("Min: ", min_value)
        break
    try:
        number = float(user_input) #convert float
        sum_value = sum_value + number #increment sum each time a number is entered
        if min_value is None or number < min_value:
            min_value = number #set min value to less if less
        if max_value is None or number > max_value:
            max_value = number #set max value to number if greater
    except:
        print("Invalid input")