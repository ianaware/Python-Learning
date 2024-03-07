'''

Day 5: Functions
• Write a function that takes two numbers as arguments and returns their sum.
• Write a function that takes a list of numbers and returns the average.



'''

def sum_function(num1, num2):
    total = num1+num2
    return total


num1 = 3
num2 = 2

print("The result of this function is ", sum_function(num1, num2))

number_list = [1, 5, 678, 34, 10]


def average_list(number_list):
        sum_list = sum(number_list)
        length_list = len(number_list)
        return sum_list / length_list
    
    
print("The average is: ", average_list(number_list))
        