#This uses lists and works out the average

numlist= list() #declare empty list
while (True): #start loop
    user_input = input("Enter a number: ") #ask for user input and store it
    if user_input == 'done': break #end the program if user types 'done'
    value = float(user_input) #convert user input from string to float
    numlist.append(value) #add float to list

    average = sum(numlist) / len(numlist) #calculate the average by summing up all values in the list, getting the length and dividing by that
    print('Average: ', average) #print out the average
