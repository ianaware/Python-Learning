'''

Exercise: Create a Python script that finds the largest number in a list.

The script should:

Create a list of numbers. You can hardcode this list in your script. For example: numbers = [3, 6, 2, 8, 4, 10].
Use a loop to iterate through the list.
Keep track of the largest number found as you iterate through the list. 
You can start by assuming the first number in the list is the largest.
After the loop completes, print out the largest number found.

'''

num_list = [10, 67, 523, 90] #Create list of numbers
max_num = None #store max number
min_num = None #store min number
sum = 0 # store sum

for numbers in num_list: #goes through all numbers in the list
    if max_num is None or numbers > max_num: #compares each list number with maximum number (starts with 0) 
        max_num = numbers #if it is higher each time then it becomes the maximum
    sum += numbers #calculate the sum of all numbers in the list inside the loop

min_num = min(num_list) #get the minimum number from the list
        

print("The maximum number is: ", max_num)
print("The minumum number is: ", min_num)
print("The total of all numbers in the list is: ", sum)
