'''

Example 3:

It's time to complicate the code - let's find the largest of three numbers. Will it enlarge the code? A bit.


'''

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
number3 = int(input("Please enter a number: "))

largest_num = number1 #set number1 as largest to start

if number2 > largest_num:
    largest_num = number2
if number3 > largest_num:
    largest_num = number3

print(f'The largest number is: {largest_num}')

#v2

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter a number: "))
number3 = int(input("Please enter a number: "))

largest_num = max(number1, number2, number3)

print(f'The largest number is: {largest_num}')
