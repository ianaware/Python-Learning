'''
Write a program to store the numbers the user enters in a list.
Use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
Print out the maximum and minimum of the numbers at the end when the user enters "done"
'''

num_list = [] #create empty list
num_list_max = 0 #variable to store max number
num_list_min = 0 #variable to store min number

while (True):
    user_input = input("Enter a number to add to the list: ")

    if user_input.lower() == "done":
        if num_list: #check if list is not empty, if not, run the code below
            num_list_max = max(num_list) #get max number
            num_list_min = min(num_list) #get min number
            print("The program will end")
            print("The max number in the list is: ", num_list_max)
            print("The min number ", num_list_min)
        else:
            print("No numbers were entered ")
        break
    try:
        user_input_float = float(user_input) #convert string to float
        num_list.append(user_input_float) #add number to list
        print ("The list contains ", num_list) #print out when number is added to the list
       
    except ValueError:
        print("Invalid Error")