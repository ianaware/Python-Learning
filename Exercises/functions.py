'''

Exercise: Create a Python function called calculate_sum

The function should take two parameters, num1 and num2.
It should return the sum of these two numbers.
After defining the function, call it with two different sets of numbers and print out the results.
For example, if you call calculate_sum(5, 3), it should print out 8.


'''

def calculate_sum(num1: int, num2:int): #create function
    sum = num1 + num2 #calculation
    return sum #value to return

num1 = 5
num2 = 3

calculate_sum(num1,num2)

print("The sum is:", calculate_sum(num1, num2)) #always add the parameters when calling the function to be printed out

num1 = 6
num2 = 10

print("The new sum is:", calculate_sum(num1, num2)) #always add the parameters when calling the function to be printed out