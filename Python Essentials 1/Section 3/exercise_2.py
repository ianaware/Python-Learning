'''

Estimated time
5-10 minutes

Level of difficulty
Very Easy

Objectives
becoming familiar with the input() function;
becoming familiar with comparison operators in Python.
Scenario
Using one of the comparison operators in Python, write a simple two-line program that takes the parameter n as input, which is an integer, and prints False if n is less than 100, and True if n is greater than or equal to 100.

Don't create any if blocks (we're going to talk about them very soon). Test your code using the data we've provided for you.

'''

n_value = input("Enter a value: ") #ask for input
n_int = int(n_value) #convert str to int
print(n_int >=100) #print result of calculation as True or False

price = 