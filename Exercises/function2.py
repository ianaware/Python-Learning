'''


Exercise: Create a Python function called compare_numbers

The function should take two parameters, num1 and num2.

The function should compare the two numbers and return:

"The numbers are equal" if num1 and num2 are equal.
"num1 is greater than num2" if num1 is greater than num2.
"num2 is greater than num1" if num2 is greater than num1.

After defining the function, call it with at least three different sets of numbers and print out the results.

'''

def compare_numbers(num1, num2):
    if num1 > num2:
        return "num1 is greater than num2"
    elif num2 > num1:
        return "num2 is greater than num1"
    elif num1 == num2:
        return "num1 and num2 are equal"
    return

num1 = 3
num2 = 7


print(compare_numbers(num1, num2))

num1 = 10
num2 = 3

print(compare_numbers(num1, num2))

num1 = 0
num2 = 5


print(compare_numbers(num1, num2))