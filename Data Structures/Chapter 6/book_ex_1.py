'''

Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.

'''
sum_value = 0
count_value = 0
average_value = 0

while True:
    user_input = input("Please enter a number: ")
    if user_input == "done" or user_input == "Done":
        print("Exiting the program ")
        print(sum_value)
        print(count_value)
        print(average_value)
        break
    try:
        number = float(user_input) #convert float
        sum_value = sum_value + number #increment sum each time a number is entered
        count_value = count_value + 1 #increment count each time a number is entered
        average_value = sum_value / count_value #work out the average
    except:
        print("Invalid input")